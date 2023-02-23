from rest_framework import views, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tools import get_serializer
import logging

logger = logging.getLogger("api")

# import/
@api_view(["POST"])
def import_records(request):
    record_creation_counter = 0
    errors = []
    for records_dict in request.data:
        model_name, data = next(iter(records_dict.items()))
        serializer = get_serializer(model_name)(data=data)
        if not serializer.is_valid():
            if set([error[0].code for error in serializer.errors.values()]) == {"unique"}:
                instance = serializer.Meta.model.objects.get(id=data["id"])
                serializer = get_serializer(model_name)(instance=instance, data=data)
                record_creation_counter += 1
            else:
                errors.append({"model": model_name, "data": data, "errors": serializer.errors})
        else:
            serializer.save()
            record_creation_counter += 1

    if record_creation_counter == 0:
        Response({"message": "No objects were uploaded", "errors": errors}, 400)

    if len(errors) > 0:
        return Response({
            "message": f"There were errors in upload. Uploaded {record_creation_counter} records.", "errors": {errors}
        }, 207)

    return Response({"message": f"Created {record_creation_counter} records."}, 201)


# detail/<model_name>
@api_view(["GET"])
def list_records(request, model_name):
    serializer_class = get_serializer(model_name)
    if not serializer_class:
        return Response({"message": "No such model found."}, 404)

    serializer = serializer_class(serializer_class.Meta.model.objects.all(), many=True)
    return Response({"message": "Data retrieved successfully.", "data": serializer.data}, 200)


# detail/<model_name>/<pk>
@api_view(["GET"])
def get_record(request, model_name, pk):
    logger.info("detail")
    serializer_class = get_serializer(model_name)
    if not serializer_class:
        return Response({"message": "No such model found."}, 404)

    try:
        serializer = serializer_class(serializer_class.Meta.model.objects.get(id=pk), many=False)
    except serializer_class.Meta.model.DoesNotExist:
        return Response({"message": f"This {model_name} record does not exist."}, 400)

    return Response({"message": "Data retrieved successfully.", "data": serializer.data}, 200)

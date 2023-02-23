from rest_framework import views, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tools import get_serializer
import logging

logger = logging.getLogger("api")


# import/
@api_view(["POST"])
def import_records(request):
    """
        An endpoint for uploading database records en-masse. The input data is mixed together,
        model selection is handled dynamically via translation method get_serializer.
        In case of duplicate pk the new record updates the old one.
    """
    record_creation_counter = 0
    errors = []
    for records_dict in request.data:
        model_name, data = next(iter(records_dict.items()))
        serializer = get_serializer(model_name)(data=data)
        if not serializer.is_valid():
            # If the only error is that the record is a duplicate, update the old record with it
            if set([error[0].code for error in serializer.errors.values()]) == {"unique"}:
                instance = serializer.Meta.model.objects.get(id=data["id"])
                serializer = get_serializer(model_name)(instance=instance, data=data)
                record_creation_counter += 1
            # Otherwise append errors to display later
            else:
                errors.append({"model": model_name, "data": data, "errors": serializer.errors})
        # If everything is alright, save data
        else:
            serializer.save()
            record_creation_counter += 1

    # Return response when everything fails
    if record_creation_counter == 0:
        logger.error(f"Import_records could not upload any of the provided data: {errors}")
        Response({"message": "No objects were uploaded", "errors": errors}, 400)

    # Return response when some of the data fails
    if len(errors) > 0:
        logger.error(f"Get_record could not upload some of the provided records: {errors}.")
        return Response({
            "message": f"There were errors in upload. Uploaded {record_creation_counter} records.", "errors": {errors}
        }, 207)

    # Return a successful response
    return Response({"message": f"Created {record_creation_counter} records."}, 201)


# detail/<model_name>
@api_view(["GET"])
def list_records(request, model_name):
    """
        An endpoint for displaying record of a given model with a given pk.
    """
    serializer_class = get_serializer(model_name)

    # If model with given model name does not exist display an error
    if not serializer_class:
        logger.error("List_records could not retrieve the model.")
        return Response({"message": "No such model found."}, 404)

    serializer = serializer_class(serializer_class.Meta.model.objects.all(), many=True)
    return Response({"message": "Data retrieved successfully.", "data": serializer.data}, 200)


# detail/<model_name>/<pk>
@api_view(["GET"])
def get_record(request, model_name, pk):
    """
        An endpoint for displaying all records of a given model.
    """
    serializer_class = get_serializer(model_name)

    # If model with given model name does not exist display an error
    if not serializer_class:
        logger.error("Get_record could not retrieve the model.")
        return Response({"message": "No such model found."}, 404)

    # If record with given pk does not exist display an error
    try:
        serializer = serializer_class(serializer_class.Meta.model.objects.get(id=pk), many=False)
    except serializer_class.Meta.model.DoesNotExist:
        logger.error(f"Get_record could not retrieve a record of model {model_name}.")
        return Response({"message": f"This {model_name} record does not exist."}, 404)

    return Response({"message": "Data retrieved successfully.", "data": serializer.data}, 200)

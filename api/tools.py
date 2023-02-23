from .serializers import *

string_to_serializer_dict = {
    "Product": ProductSerializer,
    "AttributeName": AttributeNameSerializer,
    "AttributeValue": AttributeValueSerializer,
    "Image": ImageSerializer,
    "Attribute": AttributeSerializer,
    "ProductAttributes": ProductAttributesSerializer,
    "ProductImage": ProductImageSerializer,
    "Catalog": CatalogSerializer,
}


def get_serializer(serializer_name: str):
    return string_to_serializer_dict.get(serializer_name)

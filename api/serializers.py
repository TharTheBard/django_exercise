from rest_framework import serializers
from django.db import IntegrityError
from api.models import *


class ProductSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    mena = serializers.CharField(required=False)
    published_on = serializers.DateTimeField(required=False, allow_null=True)
    is_published = serializers.BooleanField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class AttributeNameSerializer(serializers.ModelSerializer):
    kod = serializers.CharField(required=False)
    nazev = serializers.CharField(required=False)
    zobrazit = serializers.BooleanField(required=False)

    class Meta:
        model = AttributeName
        fields = '__all__'


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField(required=False)

    class Meta:
        model = Image
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeName.objects.all())
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(queryset=AttributeValue.objects.all())

    class Meta:
        model = Attribute
        fields = '__all__'


class ProductAttributesSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductAttributes
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())

    class Meta:
        model = ProductImage
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField(required=False)
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), required=False)
    products_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    attributes_ids = serializers.PrimaryKeyRelatedField(queryset=Attribute.objects.all(), many=True, required=False)

    class Meta:
        model = Catalog
        fields = '__all__'

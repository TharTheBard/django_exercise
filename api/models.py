from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=500, null=True)
    cena = models.DecimalField(max_digits=20, decimal_places=2)
    mena = models.CharField(max_length=3, null=True)
    published_on = models.DateTimeField(null=True)
    is_published = models.BooleanField(null=True)


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=150)
    kod = models.CharField(max_length=150, null=True)
    zobrazit = models.BooleanField(null=True)


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=150)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=150, null=True)
    obrazek = models.CharField(max_length=500)


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)


class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=150)


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=150, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    products_ids = models.ManyToManyField(Product)
    attributes_ids = models.ManyToManyField(Attribute)

# Generated by Django 4.1.7 on 2023-02-22 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=80)),
                ('kod', models.CharField(max_length=80, null=True)),
                ('zobrazit', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hodnota', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=80, null=True)),
                ('obrazek', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=80, null=True)),
                ('description', models.CharField(max_length=80, null=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=20)),
                ('mena', models.CharField(max_length=3, null=True)),
                ('published_on', models.DateTimeField(null=True)),
                ('is_published', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=80)),
                ('obrazek_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nazev', models.CharField(max_length=80, null=True)),
                ('attributes_ids', models.ManyToManyField(to='api.attribute')),
                ('obrazek_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.image')),
                ('products_ids', models.ManyToManyField(to='api.product')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='hodnota_atributu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.attributevalue'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='nazev_atributu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.attributename'),
        ),
    ]
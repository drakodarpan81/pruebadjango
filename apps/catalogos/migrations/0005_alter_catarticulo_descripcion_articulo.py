# Generated by Django 4.1.2 on 2022-10-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_catarticulo_catproveedor_delete_catmercancia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catarticulo',
            name='descripcion_articulo',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-08 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0012_alter_catarticulo_requisicion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catarticulo',
            name='imagen',
            field=models.ImageField(blank=True, default='default/no-image.png', null=True, upload_to='articulos/', verbose_name='Imagen del producto'),
        ),
    ]
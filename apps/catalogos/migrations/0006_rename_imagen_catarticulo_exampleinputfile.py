# Generated by Django 4.1.2 on 2022-10-31 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_alter_catarticulo_descripcion_articulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catarticulo',
            old_name='imagen',
            new_name='exampleInputFile',
        ),
    ]

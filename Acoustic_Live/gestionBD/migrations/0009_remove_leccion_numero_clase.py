# Generated by Django 3.2.8 on 2021-10-21 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionBD', '0008_alter_profesor_apellido_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leccion',
            name='numero_clase',
        ),
    ]

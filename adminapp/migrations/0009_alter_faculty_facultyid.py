# Generated by Django 4.2.4 on 2023-11-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_rename_component_type_facultycoursemapping_component_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='facultyid',
            field=models.IntegerField(unique=True),
        ),
    ]

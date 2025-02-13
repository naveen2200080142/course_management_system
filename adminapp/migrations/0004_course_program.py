# Generated by Django 4.2.4 on 2023-10-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_student_department_student_program_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech')], default='B.Tech', max_length=50),
        ),
    ]

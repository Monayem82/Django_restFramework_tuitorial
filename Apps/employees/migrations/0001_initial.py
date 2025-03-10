# Generated by Django 5.1.3 on 2025-03-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=10)),
                ('emp_name', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_to', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

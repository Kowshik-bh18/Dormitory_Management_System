# Generated by Django 5.1.2 on 2024-10-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]

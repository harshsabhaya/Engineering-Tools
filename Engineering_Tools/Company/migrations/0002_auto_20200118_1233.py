# Generated by Django 3.0.1 on 2020-01-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='c_email',
            field=models.EmailField(max_length=254),
        ),
    ]

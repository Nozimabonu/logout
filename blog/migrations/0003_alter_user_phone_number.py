# Generated by Django 5.0.6 on 2024-06-20 09:37

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_phone_number_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, validators=[blog.validators.validate_length]),
        ),
    ]

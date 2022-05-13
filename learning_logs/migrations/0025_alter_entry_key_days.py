# Generated by Django 4.0.4 on 2022-05-12 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0024_alter_entry_key_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='key_days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
    ]

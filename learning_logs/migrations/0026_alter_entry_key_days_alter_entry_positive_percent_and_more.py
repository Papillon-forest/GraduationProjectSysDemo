# Generated by Django 4.0.4 on 2022-05-12 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0025_alter_entry_key_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='key_days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='positive_percent',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_1',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_2',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_3',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_4',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_5',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating_average',
            field=models.DecimalField(decimal_places=10, max_digits=11, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
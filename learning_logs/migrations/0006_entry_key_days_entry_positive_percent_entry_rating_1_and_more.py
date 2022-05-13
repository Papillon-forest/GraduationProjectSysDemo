# Generated by Django 4.0.4 on 2022-05-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_entry_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='key_days',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='positive_percent',
            field=models.DecimalField(decimal_places=10, default=2, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_1',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_2',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_3',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_4',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_5',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='rating_average',
            field=models.DecimalField(decimal_places=10, default=2, max_digits=11),
            preserve_default=False,
        ),
    ]

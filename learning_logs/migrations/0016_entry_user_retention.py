# Generated by Django 4.0.4 on 2022-05-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0015_remove_entry_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='user_retention',
            field=models.DecimalField(decimal_places=10, default=2, max_digits=11),
            preserve_default=False,
        ),
    ]

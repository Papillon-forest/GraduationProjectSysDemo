# Generated by Django 4.0.4 on 2022-05-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0018_entry_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rule',
            field=models.CharField(choices=[(1, 1), (2, 2)], default=1, max_length=5),
        ),
    ]

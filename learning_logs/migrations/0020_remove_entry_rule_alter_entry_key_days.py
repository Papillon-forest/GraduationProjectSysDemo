# Generated by Django 4.0.4 on 2022-05-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0019_alter_entry_rule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='rule',
        ),
        migrations.AlterField(
            model_name='entry',
            name='key_days',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (14, 14), (30, 30)], default=1, max_length=5),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-21 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20210908_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamecard',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='gamecard',
            name='card_type',
        ),
    ]
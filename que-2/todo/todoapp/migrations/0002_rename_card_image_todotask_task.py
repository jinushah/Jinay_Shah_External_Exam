# Generated by Django 4.0.5 on 2022-12-16 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todotask',
            old_name='card_image',
            new_name='task',
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-21 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washing_machine', '0002_alter_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='washingmachine',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='washingmachine',
            name='using_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='washing_machine.user'),
        ),
    ]
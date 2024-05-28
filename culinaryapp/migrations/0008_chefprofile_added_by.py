# Generated by Django 5.0.6 on 2024-05-28 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinaryapp', '0007_favouritedish'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefprofile',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chefs', to='culinaryapp.userprofile'),
        ),
    ]
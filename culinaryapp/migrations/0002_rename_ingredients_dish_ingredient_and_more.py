# Generated by Django 5.0.6 on 2024-05-25 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinaryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='ingredients',
            new_name='ingredient',
        ),
        migrations.AddField(
            model_name='chefprofile',
            name='last_name',
            field=models.CharField(default='food', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chefprofile',
            name='name',
            field=models.CharField(default='food', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='title',
            field=models.CharField(default='food', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dishingredient',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_ingredients', to='culinaryapp.dish'),
        ),
    ]

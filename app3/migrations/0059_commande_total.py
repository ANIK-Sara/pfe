# Generated by Django 5.0.3 on 2024-03-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0058_alter_commande_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default=None, max_length=200),
        ),
    ]

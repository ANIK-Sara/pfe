# Generated by Django 5.0.3 on 2024-03-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0064_commande_num_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacie',
            name='items',
            field=models.CharField(default=None, max_length=300),
        ),
    ]

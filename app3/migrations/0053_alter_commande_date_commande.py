# Generated by Django 5.0.3 on 2024-03-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0052_commande_adr_mail_commande_adresse_commande_ville_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

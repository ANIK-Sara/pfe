# Generated by Django 5.0.3 on 2024-03-27 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0041_ordonnance_adresse_cabinet_ordonnance_num_tel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordonnance',
            name='prenom_medecin',
        ),
    ]

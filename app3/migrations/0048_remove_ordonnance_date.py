# Generated by Django 5.0.3 on 2024-03-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0047_remove_ordonnance_liste_produits_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordonnance',
            name='date',
        ),
    ]

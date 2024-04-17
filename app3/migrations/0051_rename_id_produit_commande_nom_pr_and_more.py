# Generated by Django 5.0.3 on 2024-03-29 23:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0050_alter_produit_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='id_produit',
            new_name='nom_pr',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_patient',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='id_pharmacie',
        ),
        migrations.AddField(
            model_name='commande',
            name='nom_utilisateur',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app3.login'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_commande',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='commande',
            name='id_commande',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

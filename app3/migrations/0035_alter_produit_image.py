# Generated by Django 5.0.3 on 2024-03-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0034_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='photos/%y/%m/%d'),
        ),
    ]

# Generated by Django 5.2.4 on 2025-07-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/evenements/'),
        ),
        migrations.AlterField(
            model_name='imageevenement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/evenements/'),
        ),
        migrations.AlterField(
            model_name='imagelieu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/lieux/'),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/lieux/'),
        ),
    ]

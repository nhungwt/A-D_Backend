# Generated by Django 4.1.7 on 2023-04-16 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='producCtDetailUrl',
            new_name='productDetailUrl',
        ),
    ]

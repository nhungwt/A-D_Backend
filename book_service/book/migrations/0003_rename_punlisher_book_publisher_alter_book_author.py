# Generated by Django 4.1.7 on 2023-04-15 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='punlisher',
            new_name='publisher',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.author'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-07 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]

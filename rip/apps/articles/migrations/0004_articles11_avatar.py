# Generated by Django 3.2.8 on 2021-10-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211013_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles11',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

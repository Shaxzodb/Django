# Generated by Django 3.2.2 on 2021-06-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maqola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

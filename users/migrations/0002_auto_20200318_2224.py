# Generated by Django 3.0.3 on 2020-03-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepictures/de.jpg', upload_to='profilepictures'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-21 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sem', '0003_sem1_sem2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sem2',
            name='user',
        ),
        migrations.DeleteModel(
            name='Sem1',
        ),
        migrations.DeleteModel(
            name='Sem2',
        ),
    ]

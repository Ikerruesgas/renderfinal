# Generated by Django 5.1.2 on 2024-10-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTop100Django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='ranking',
            field=models.IntegerField(unique=True),
        ),
    ]
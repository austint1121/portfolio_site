# Generated by Django 3.2.3 on 2021-07-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0022_auto_20210713_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='spoiler',
            field=models.BooleanField(default=False),
        ),
    ]

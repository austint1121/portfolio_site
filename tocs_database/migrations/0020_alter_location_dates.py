# Generated by Django 3.2.3 on 2021-07-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0019_location_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='dates',
            field=models.CharField(help_text='Enter Dates at Location', max_length=20),
        ),
    ]

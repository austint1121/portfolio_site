# Generated by Django 3.2.3 on 2021-06-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0010_auto_20210622_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='uploads'),
        ),
    ]
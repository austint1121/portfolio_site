# Generated by Django 3.2.3 on 2021-07-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0015_auto_20210708_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enemy',
            name='skills',
            field=models.ManyToManyField(blank=True, help_text='Enemy skills', to='tocs_database.Skill'),
        ),
    ]
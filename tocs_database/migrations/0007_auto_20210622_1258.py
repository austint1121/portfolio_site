# Generated by Django 3.2.3 on 2021-06-22 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0006_auto_20210622_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enemy',
            name='items',
        ),
        migrations.AddField(
            model_name='enemy',
            name='items',
            field=models.OneToOneField(default=0, help_text='Item Drops for enemy', on_delete=django.db.models.deletion.PROTECT, to='tocs_database.itemdrop'),
            preserve_default=False,
        ),
    ]

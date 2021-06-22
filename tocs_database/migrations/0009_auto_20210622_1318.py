# Generated by Django 3.2.3 on 2021-06-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0008_alter_enemy_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enemy',
            name='items',
        ),
        migrations.AddField(
            model_name='enemy',
            name='items',
            field=models.ManyToManyField(help_text='Item Drops for enemy', to='tocs_database.ItemDrop'),
        ),
    ]

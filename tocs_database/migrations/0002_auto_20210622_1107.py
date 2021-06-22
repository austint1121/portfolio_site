# Generated by Django 3.2.3 on 2021-06-22 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enemy',
            old_name='item',
            new_name='items',
        ),
        migrations.RemoveField(
            model_name='elementalefficacy',
            name='enemy',
        ),
        migrations.RemoveField(
            model_name='sepithdropped',
            name='enemy',
        ),
        migrations.RemoveField(
            model_name='statusefficacy',
            name='enemy',
        ),
        migrations.RemoveField(
            model_name='unbalanceefficacy',
            name='enemy',
        ),
        migrations.AddField(
            model_name='enemy',
            name='elemental_efficacy',
            field=models.OneToOneField(default=100, on_delete=django.db.models.deletion.PROTECT, to='tocs_database.elementalefficacy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enemy',
            name='sepith_dropped',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='tocs_database.sepithdropped'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enemy',
            name='status_efficacy',
            field=models.OneToOneField(default=100, on_delete=django.db.models.deletion.PROTECT, to='tocs_database.statusefficacy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enemy',
            name='unbalance_efficacy',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='tocs_database.unbalanceefficacy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='elementalefficacy',
            name='earth',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='elementalefficacy',
            name='fire',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='elementalefficacy',
            name='water',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='elementalefficacy',
            name='wind',
            field=models.IntegerField(default=100),
        ),
    ]

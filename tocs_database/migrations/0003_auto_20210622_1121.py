# Generated by Django 3.2.3 on 2021-06-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocs_database', '0002_auto_20210622_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enemy',
            name='elemental_efficacy',
        ),
        migrations.RemoveField(
            model_name='enemy',
            name='sepith_dropped',
        ),
        migrations.RemoveField(
            model_name='enemy',
            name='status_efficacy',
        ),
        migrations.RemoveField(
            model_name='enemy',
            name='unbalance_efficacy',
        ),
        migrations.AddField(
            model_name='enemy',
            name='Time_efficacy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='at_delay_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='blind_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='burn_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='confuse_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='deathblow_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='earth_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='earth_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='faint_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='fire_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='fire_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='freeze_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='mass_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='mirage_efficacy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='mirage_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='mute_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='nightmare_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='petrify_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='pierce',
            field=models.IntegerField(choices=[('1/5', 1), ('2/5', 2), ('3/5', 3), ('4/5', 4), ('5/5', 5)], default=1),
        ),
        migrations.AddField(
            model_name='enemy',
            name='poision_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='s_down_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='seal_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='slash',
            field=models.IntegerField(choices=[('1/5', 1), ('2/5', 2), ('3/5', 3), ('4/5', 4), ('5/5', 5)], default=1),
        ),
        migrations.AddField(
            model_name='enemy',
            name='sleep_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='space_efficacy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='space_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='strike',
            field=models.IntegerField(choices=[('1/5', 1), ('2/5', 2), ('3/5', 3), ('4/5', 4), ('5/5', 5)], default=1),
        ),
        migrations.AddField(
            model_name='enemy',
            name='thrust',
            field=models.IntegerField(choices=[('1/5', 1), ('2/5', 2), ('3/5', 3), ('4/5', 4), ('5/5', 5)], default=1),
        ),
        migrations.AddField(
            model_name='enemy',
            name='time_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='vanish_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='water_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='water_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enemy',
            name='wind_efficacy',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='enemy',
            name='wind_sepith',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ElementalEfficacy',
        ),
        migrations.DeleteModel(
            name='SepithDropped',
        ),
        migrations.DeleteModel(
            name='StatusEfficacy',
        ),
        migrations.DeleteModel(
            name='UnbalanceEfficacy',
        ),
    ]

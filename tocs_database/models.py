from django.db import models

# Create your models here.
class Location(models.Model):
    """Locations/Dungeons in game"""
    name = models.CharField(max_length=50, help_text='Locations with enemies')
    def __str__(self):
        return self.name

class Enemy(models.Model):
    """Model for an enemy in the game."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text='Enter enemy name/title')
    profile_pic = models.ImageField(upload_to='', null=True)
    location = models.ForeignKey('Location', on_delete=models.RESTRICT)
    level = models.IntegerField(help_text= 'Enter enemy Level')
    HP = models.IntegerField()
    EXP = models.IntegerField()
    STR = models.IntegerField()
    DEF = models.IntegerField()
    ATS = models.IntegerField()
    ADF = models.IntegerField()
    SPD = models.IntegerField()
    bio = models.TextField(help_text='Enter enemy biography')

    # Elemental efficacy
    earth_efficacy = models.IntegerField(default=100)
    water_efficacy = models.IntegerField(default=100)
    fire_efficacy = models.IntegerField(default=100)
    wind_efficacy = models.IntegerField(default=100)
    #  Time, space, and mirage weakness are not present for all enemies.
    time_efficacy = models.IntegerField(null=True, blank=True)
    space_efficacy = models.IntegerField(null=True, blank=True)
    mirage_efficacy = models.IntegerField(null=True, blank=True)

    #skills
    skills = models.ManyToManyField('Skill', help_text='Enemy skills')

    #Sepith Dropped
    earth_sepith = models.IntegerField(default=0)
    water_sepith = models.IntegerField(default=0)
    fire_sepith = models.IntegerField(default=0)
    wind_sepith = models.IntegerField(default=0)
    time_sepith = models.IntegerField(default=0)
    space_sepith = models.IntegerField(default=0)
    mirage_sepith = models.IntegerField(default=0)
    mass_sepith = models.IntegerField(default=0)

    #items
    items = models.ManyToManyField('ItemDrop', help_text='Item Drops for enemy')

    #Unbalance Efficacy
    efficacy = (
        ('1/5', '1'),
        ('2/5', '2'),
        ('3/5', '3'),
        ('4/5', '4'),
        ('5/5', '5'),
    )

    slash = models.CharField(choices=efficacy, default='1', max_length=10)
    thrust = models.CharField(choices=efficacy, default='1', max_length=10)
    pierce = models.CharField(choices=efficacy, default='1', max_length=10)
    strike = models.CharField(choices=efficacy, default='1', max_length=10)

    #status_efficacy
    poison_efficacy = models.IntegerField(default=100)
    seal_efficacy = models.IntegerField(default=100)
    mute_efficacy = models.IntegerField(default=100)
    blind_efficacy = models.IntegerField(default=100)
    sleep_efficacy = models.IntegerField(default=100)
    burn_efficacy = models.IntegerField(default=100)
    freeze_efficacy = models.IntegerField(default=100)
    petrify_efficacy = models.IntegerField(default=100)
    faint_efficacy = models.IntegerField(default=100)
    confuse_efficacy = models.IntegerField(default=100)
    deathblow_efficacy = models.IntegerField(default=100)
    nightmare_efficacy = models.IntegerField(default=100)
    at_delay_efficacy = models.IntegerField(default=100)
    vanish_efficacy = models.IntegerField(default=100)
    s_down_efficacy = models.IntegerField(default=100)


    def __str__(self):
        return self.name

# class ElementalEfficacy(models.Model):
#     """Model for elemental efficacy for a paticular monster"""
#     earth = models.IntegerField(default=100)
#     water = models.IntegerField(default=100)
#     fire = models.IntegerField(default=100)
#     wind = models.IntegerField(default=100)
#     #  Time, space, and mirage weakness are not present for all enemies.
#     Time = models.IntegerField(null=True, blank=True)
#     space = models.IntegerField(null=True, blank=True)
#     mirage = models.IntegerField(null=True, blank=True)

# class SepithDropped(models.Model):
#     """Model for sepith drop for a monster"""
#     earth = models.IntegerField(null=True, blank=True)
#     water = models.IntegerField(null=True, blank=True)
#     fire = models.IntegerField(null=True, blank=True)
#     wind = models.IntegerField(null=True, blank=True)
#     Time = models.IntegerField(null=True, blank=True)
#     space = models.IntegerField(null=True, blank=True)
#     mirage = models.IntegerField(null=True, blank=True)
#     mass = models.IntegerField(null=True, blank=True)


class ItemDrop(models.Model):
    """Model for Item drops"""
    name = models.CharField(max_length=50, help_text='Name of item')
    drop_chance = models.FloatField(help_text='Enter drop chance as decimal')
    def __str__(self):
        return self.name

# class UnbalanceEfficacy(models.Model):
#     """Model for a monster's unbalance chance"""
#     efficacy = (
#         ('1/5', 1),
#         ('2/5', 2),
#         ('3/5', 3),
#         ('4/5', 4),
#         ('5/5', 5),
#     )
#
#     slash = models.IntegerField(choices=efficacy, default=1)
#     thrust = models.IntegerField(choices=efficacy, default=1)
#     pierce = models.IntegerField(choices=efficacy, default=1)
#     strike = models.IntegerField(choices=efficacy, default=1)

# class StatusEfficacy(models.Model):
#     """Status ailement for a monster"""
#     poision = models.IntegerField(default=100)
#     seal = models.IntegerField(default=100)
#     mute = models.IntegerField(default=100)
#     blind = models.IntegerField(default=100)
#     sleep = models.IntegerField(default=100)
#     burn = models.IntegerField(default=100)
#     freeze = models.IntegerField(default=100)
#     petrify = models.IntegerField(default=100)
#     faint = models.IntegerField(default=100)
#     confuse = models.IntegerField(default=100)
#     deathblow = models.IntegerField(default=100)
#     nightmare = models.IntegerField(default=100)
#     at_delay = models.IntegerField(default=100)
#     vanish = models.IntegerField(default=100)
#     s_down = models.IntegerField(default=100)

class Skill(models.Model):
    """Arts / skills for enemies"""
    name = models.CharField(max_length=50)
    ability_type_choices = (
        ('Art', 'A'),
        ('Craft', 'C'),
    )
    ability_type = models.CharField(choices=ability_type_choices, max_length=20)
    desc = models.TextField(max_length=100, help_text='Description of art or ability')
    def __str__(self):
        return self.name
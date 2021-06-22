from django.db import models

# Create your models here.
class Location(models.Model):
    """Locations/Dungeons in game"""
    name = models.CharField(max_length=50, help_text='Locations with enemies')
    def __str__(self):
        return self.name

class Enemy(models.Model):
    """Model for an enemy in the game."""
    name = models.CharField(max_length=50, help_text='Enter enemy name/title')
    profile_pic = models.ImageField(upload_to='uploads', null=True)
    location = models.ForeignKey('Location', on_delete=models.RESTRICT)
    level = models.IntegerField(help_text= 'Enter enemy Level')
    bio = models.TextField(help_text='Enter enemy biography')
    item = models.ManyToManyField('ItemDrops', help_text='Item Drops for enemy')
    skills = models.ManyToManyField('Skills', help_text='Enemy skills')
    HP = models.IntegerField()
    EXP = models.IntegerField()
    STR = models.IntegerField()
    DEF = models.IntegerField()
    ATS = models.IntegerField()
    ADF = models.IntegerField()
    SPD = models.IntegerField()

class ElementalEfficacy(models.Model):
    """Model for elemental efficacy for a paticular monster"""
    enemy = models.OneToOneField('Enemy', on_delete=models.PROTECT)
    earth = models.IntegerField()
    water = models.IntegerField()
    fire = models.IntegerField()
    wind = models.IntegerField()
    #  Time, space, and mirage weakness are not present for all enemies.
    Time = models.IntegerField(null=True, blank=True)
    space = models.IntegerField(null=True, blank=True)
    mirage = models.IntegerField(null=True, blank=True)

class SepithDropped(models.Model):
    """Model for sepith drop for a monster"""
    enemy = models.OneToOneField('Enemy', on_delete=models.PROTECT)
    earth = models.IntegerField(null=True, blank=True)
    water = models.IntegerField(null=True, blank=True)
    fire = models.IntegerField(null=True, blank=True)
    wind = models.IntegerField(null=True, blank=True)
    Time = models.IntegerField(null=True, blank=True)
    space = models.IntegerField(null=True, blank=True)
    mirage = models.IntegerField(null=True, blank=True)
    mass = models.IntegerField(null=True, blank=True)

class ItemDrops(models.Model):
    """Model for Item drops"""
    name = models.CharField(max_length=50, help_text='Name of item')
    drop_chance = models.FloatField(help_text='Enter drop chance as decimal')

class UnbalanceEfficacy(models.Model):
    """Model for a monster's unbalance chance"""
    enemy = models.OneToOneField('Enemy', on_delete=models.PROTECT)
    efficacy = (
        ('1/5', 1),
        ('2/5', 2),
        ('3/5', 3),
        ('4/5', 4),
        ('5/5', 5),
    )

    slash = models.IntegerField(choices=efficacy, default=1)
    thrust = models.IntegerField(choices=efficacy, default=1)
    pierce = models.IntegerField(choices=efficacy, default=1)
    strike = models.IntegerField(choices=efficacy, default=1)

class StatusEfficacy(models.Model):
    """Status ailement for a monster"""
    enemy = models.OneToOneField('Enemy', on_delete=models.PROTECT)
    poision = models.IntegerField(default=100)
    seal = models.IntegerField(default=100)
    mute = models.IntegerField(default=100)
    blind = models.IntegerField(default=100)
    sleep = models.IntegerField(default=100)
    burn = models.IntegerField(default=100)
    freeze = models.IntegerField(default=100)
    petrify = models.IntegerField(default=100)
    faint = models.IntegerField(default=100)
    confuse = models.IntegerField(default=100)
    deathblow = models.IntegerField(default=100)
    nightmare = models.IntegerField(default=100)
    at_delay = models.IntegerField(default=100)
    vanish = models.IntegerField(default=100)
    s_down = models.IntegerField(default=100)

class Skills(models.Model):
    """Arts / skills for enemies"""
    name = models.TextField(max_length=50)
    desc = models.TextField(max_length=50, help_text='Description of art or ability')
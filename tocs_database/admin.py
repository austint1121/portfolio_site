from django.contrib import admin
from .models import Location, Enemy, Skill, ItemDrop

# Register your models here.
admin.site.register(Location)
# admin.site.register(Enemy)
admin.site.register(Skill)
admin.site.register(ItemDrop)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class ItemInline(admin.TabularInline):
    model = ItemDrop
    extra = 0

@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['boss', 'spoiler']
        }),
        (None, {
            'fields': ('name', 'location', 'profile_pic','bio')
        }),
        ('Stats', {
            'fields': [('level', 'HP', 'EXP'), ('STR', 'DEF', 'ATS', 'ADF', 'SPD')]
        }),
        ('Elemental Efficacy',{
            'fields':('earth_efficacy','water_efficacy', 'fire_efficacy', 'wind_efficacy', 'time_efficacy', 'space_efficacy', 'mirage_efficacy')
        }),
        ('Skills', {
            'fields': ['skills']
        }),
        ('Sepith Dropped', {
            'fields':(('earth_sepith', 'water_sepith', 'fire_sepith', 'wind_sepith'), ('time_sepith', 'space_sepith', 'mirage_sepith', 'mass_sepith'))
        }),

        ('Unbalance Efficacy', {
            'fields': [('slash', 'thrust', 'pierce', 'strike')]
        }),
        ('Status Efficacy', {
            'fields': (('poison_efficacy', 'burn_efficacy', 'deathblow_efficacy'), ('seal_efficacy','freeze_efficacy', 'nightmare_efficacy'), ('mute_efficacy', 'petrify_efficacy', 'at_delay_efficacy'), ('blind_efficacy', 'faint_efficacy', 'vanish_efficacy'), ('sleep_efficacy', 'confuse_efficacy','s_down_efficacy'))
        }),
        ('Boss Notes', {
            'fields': ['boss_notes']
        }),
    )
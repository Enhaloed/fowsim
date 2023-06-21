# Generated by Django 4.0.4 on 2023-06-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0042_attributepickrate_cardtotalcostpickrate_cardtypepickrate_mostpickedcardpickrate_pickperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Regalia', 'Regalia'), ('Chant', 'Chant'), ('Rune', 'Rune'), ('Master Rune', 'Master Rune'), ('Magic Stone', 'Magic Stone'), ('Basic Magic Stone', 'Basic Magic Stone'), ('Special Magic Stone', 'Special Magic Stone'), ('True Magic Stone', 'True Magic Stone'), ('Ruler', 'Ruler'), ('Basic J-Ruler', 'Basic J-Ruler'), ('J-RulerSpell:Chant-Standby', 'J-RulerSpell:Chant-Standby'), ('Resonator', 'Resonator'), ('Sub-ruler', 'Sub-ruler')], max_length=200),
        ),
    ]

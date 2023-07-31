# Generated by Django 3.2.6 on 2023-07-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0043_alter_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Regalia', 'Regalia'), ('Chant', 'Chant'), ('Rune', 'Rune'), ('Master Rune', 'Master Rune'), ('Magic Stone', 'Magic Stone'), ('Basic Magic Stone', 'Basic Magic Stone'), ('Special Magic Stone', 'Special Magic Stone'), ('True Magic Stone', 'True Magic Stone'), ('Ruler', 'Ruler'), ('Basic J-Ruler', 'Basic J-Ruler'), ('J-RulerSpell:Chant-Standby', 'J-RulerSpell:Chant-Standby'), ('Resonator', 'Resonator'), ('Sub-ruler', 'Sub-ruler'), ('Extension Rule', 'Extension Rule')], max_length=200),
        ),
    ]
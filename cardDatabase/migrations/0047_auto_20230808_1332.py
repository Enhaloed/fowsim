# Generated by Django 3.2.6 on 2023-08-08 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardDatabase', '0046_auto_20230802_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExceptionAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('technical_name', models.CharField(max_length=50)),
                ('applying_to_cards', models.ManyToManyField(blank=True, related_name='exceptions', to='cardDatabase.Card')),
            ],
        ),
        migrations.AlterField(
            model_name='restriction',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restriction_tag', to='cardDatabase.tag'),
        ),
        migrations.CreateModel(
            name='RestrictionException',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_zone_restriction', models.CharField(blank=True, max_length=50, null=True)),
                ('exception_action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardDatabase.exceptionaction')),
                ('exception_applying_card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardDatabase.card')),
                ('restriction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardDatabase.restriction')),
            ],
        ),
    ]
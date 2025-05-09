# Generated by Django 5.2 on 2025-04-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('four_wheeler_price', models.CharField(blank=True, default='FREE', max_length=10)),
                ('two_wheeler_price', models.CharField(blank=True, default='FREE', max_length=10)),
                ('four_wheeler_available_slots', models.IntegerField(default=0)),
                ('two_wheeler_available_slots', models.IntegerField(default=0)),
            ],
        ),
    ]

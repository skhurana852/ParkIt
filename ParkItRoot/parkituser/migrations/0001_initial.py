# Generated by Django 3.2.6 on 2022-02-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkItSpaceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('space_available_for', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]

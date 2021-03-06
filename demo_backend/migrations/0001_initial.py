# Generated by Django 3.1.1 on 2020-09-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('name', models.CharField(max_length=500)),
                ('photo', models.FileField(upload_to='')),
                ('email', models.EmailField(max_length=300)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('age', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pathname', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_backend', '0003_auto_20200924_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]

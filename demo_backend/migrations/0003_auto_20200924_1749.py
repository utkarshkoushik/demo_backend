# Generated by Django 3.1.1 on 2020-09-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_backend', '0002_auto_20200924_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]

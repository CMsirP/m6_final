# Generated by Django 3.2.5 on 2021-07-03 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='club_manager.member'),
        ),
    ]
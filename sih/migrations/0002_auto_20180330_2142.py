# Generated by Django 2.0.3 on 2018-03-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('GENERAL', 'GENERAL'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], default='GENERAL', max_length=10),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='location',
            field=models.CharField(default='Delhi', max_length=100),
        ),
    ]

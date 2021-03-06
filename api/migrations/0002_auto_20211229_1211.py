# Generated by Django 3.2.10 on 2021-12-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='name',
            new_name='en_name',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='slug',
            new_name='ko_name',
        ),
        migrations.AddField(
            model_name='companies',
            name='category',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='industry',
            field=models.CharField(max_length=16, null=True),
        ),
    ]

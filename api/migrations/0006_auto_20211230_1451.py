# Generated by Django 3.2.10 on 2021-12-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211229_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='id',
        ),
        migrations.AlterField(
            model_name='companies',
            name='en_name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]

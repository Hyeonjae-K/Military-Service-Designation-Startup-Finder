# Generated by Django 3.2.10 on 2021-12-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211229_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='update_date',
            field=models.DateTimeField(null=True),
        ),
    ]

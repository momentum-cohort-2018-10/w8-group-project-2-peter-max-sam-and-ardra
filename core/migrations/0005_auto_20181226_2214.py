# Generated by Django 2.1.4 on 2018-12-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181220_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
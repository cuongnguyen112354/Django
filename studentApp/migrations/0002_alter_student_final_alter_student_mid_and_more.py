# Generated by Django 5.0.6 on 2024-05-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='final',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='mid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='qt1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='qt2',
            field=models.FloatField(default=0),
        ),
    ]

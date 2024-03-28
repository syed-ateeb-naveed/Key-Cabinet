# Generated by Django 5.0.2 on 2024-03-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='keyname',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='level',
            field=models.CharField(choices=[('Read', 'Read'), ('Write', 'Write')], max_length=10, unique=True),
        ),
    ]

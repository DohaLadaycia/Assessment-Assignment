# Generated by Django 5.0.6 on 2024-09-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='category',
            field=models.CharField(default='general', max_length=50),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='country',
            field=models.CharField(default='us', max_length=50),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

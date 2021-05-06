# Generated by Django 3.2 on 2021-04-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_newsmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='surname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

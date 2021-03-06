# Generated by Django 3.0.6 on 2020-05-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200518_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20200414_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='goodtext',
            field=models.CharField(blank=True, default='a', max_length=200, null=True),
        ),
    ]

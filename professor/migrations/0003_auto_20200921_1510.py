# Generated by Django 3.1.1 on 2020-09-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_auto_20200921_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_5',
            field=models.CharField(default='-', max_length=50),
            preserve_default=False,
        ),
    ]
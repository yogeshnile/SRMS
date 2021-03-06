# Generated by Django 3.1.1 on 2020-09-21 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0003_auto_20200921_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='first_year',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('roll_no', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('enrollment_no', models.CharField(max_length=20)),
                ('sub_1', models.IntegerField(default=0)),
                ('sub_2', models.IntegerField(default=0)),
                ('sub_3', models.IntegerField(default=0)),
                ('sub_4', models.IntegerField(default=0)),
                ('sub_5', models.IntegerField(default=0)),
                ('sub_6', models.IntegerField(default=0)),
                ('timeStamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.subject')),
            ],
        ),
    ]

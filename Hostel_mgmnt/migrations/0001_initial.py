# Generated by Django 2.0.3 on 2018-08-05 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomNo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('floorNo', models.IntegerField()),
                ('blkid', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('availability', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stdent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('tzid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('institute', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='stdent',
            name='tzid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hostel_mgmnt.Student'),
        ),
    ]

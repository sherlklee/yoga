# Generated by Django 2.2.1 on 2019-06-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.AutoField(primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=20)),
                ('trainer', models.CharField(max_length=20)),
                ('courseprice', models.FloatField(default=0)),
                ('coursevalid', models.BooleanField(default=True)),
                ('introdution', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customerinformation',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sex', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=11)),
                ('birthday', models.DateField(default='1990/01/01')),
                ('profession', models.CharField(max_length=20)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('bust', models.FloatField(default=0)),
                ('waistline', models.FloatField(default=0)),
                ('hipline', models.FloatField(default=0)),
                ('shoulderwidth', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trainerinformation',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.BooleanField(default=True)),
                ('professionaltitle', models.CharField(max_length=30)),
                ('introdution', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=25)),
            ],
        ),
    ]
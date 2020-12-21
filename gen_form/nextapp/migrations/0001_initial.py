# Generated by Django 2.2 on 2020-12-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='re_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('l_band', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=40)),
                ('num_mem', models.CharField(max_length=40)),
                ('num_band_mem', models.CharField(max_length=40)),
                ('establi_date', models.DateField(max_length=20)),
                ('link_social', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=60)),
                ('ca', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'reg',
            },
        ),
    ]
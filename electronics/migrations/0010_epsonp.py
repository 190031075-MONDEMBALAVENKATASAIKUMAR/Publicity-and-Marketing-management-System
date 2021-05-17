# Generated by Django 3.2.2 on 2021-05-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0009_applep'),
    ]

    operations = [
        migrations.CreateModel(
            name='epsonp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('height', models.IntegerField()),
                ('width', models.CharField(max_length=1001)),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
    ]

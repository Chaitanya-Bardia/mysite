# Generated by Django 5.0.6 on 2024-07-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=100)),
                ('rdescription', models.TextField()),
                ('rimage', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]

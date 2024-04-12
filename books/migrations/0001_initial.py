# Generated by Django 5.0.4 on 2024-04-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=512)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=30)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
    ]

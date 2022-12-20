# Generated by Django 4.1.4 on 2022-12-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
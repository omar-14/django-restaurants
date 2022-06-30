# Generated by Django 4.0.5 on 2022-06-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
            ],
        ),
    ]

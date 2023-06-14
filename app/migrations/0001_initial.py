# Generated by Django 4.2.2 on 2023-06-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image_url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

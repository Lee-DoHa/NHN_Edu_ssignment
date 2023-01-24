# Generated by Django 4.0.4 on 2023-01-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('published_datetime', models.DateTimeField(blank=True, null=True)),
                ('attachment_list', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
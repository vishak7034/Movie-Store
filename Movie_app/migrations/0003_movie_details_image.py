# Generated by Django 5.0.6 on 2024-09-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_app', '0002_movie_details_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_details',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

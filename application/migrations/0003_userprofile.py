# Generated by Django 3.1.6 on 2021-03-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_alter_profile_profileimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bia',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images'),
        ),
    ]

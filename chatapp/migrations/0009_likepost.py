# Generated by Django 4.2.7 on 2023-11-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0008_rename_post_post_caption_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]

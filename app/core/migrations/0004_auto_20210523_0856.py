# Generated by Django 3.2.3 on 2021-05-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210523_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_image', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

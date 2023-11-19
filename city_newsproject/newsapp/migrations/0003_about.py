# Generated by Django 4.2.5 on 2023-11-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Текст')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('position', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'контент о сайте',
                'verbose_name_plural': 'контент о сайте',
                'ordering': ['position'],
            },
        ),
    ]

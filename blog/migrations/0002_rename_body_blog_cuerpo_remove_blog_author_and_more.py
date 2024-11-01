# Generated by Django 5.1.2 on 2024-10-30 01:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='cuerpo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(default='Administrador', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='Titulo por defecto', max_length=100),
            preserve_default=False,
        ),
    ]

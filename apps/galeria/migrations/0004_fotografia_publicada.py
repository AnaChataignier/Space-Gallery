# Generated by Django 4.2.2 on 2023-07-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_alter_fotografia_descricao_alter_fotografia_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='legenda',
            field=models.CharField(max_length=150),
        ),
    ]

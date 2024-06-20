# Generated by Django 5.0.6 on 2024-06-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('titre', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='bureau')),
            ],
            options={
                'verbose_name': 'Bureau',
                'verbose_name_plural': 'Bureau',
            },
        ),
    ]

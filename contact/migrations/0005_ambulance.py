# Generated by Django 3.2.3 on 2021-05-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_plasma_last_donated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('organization', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
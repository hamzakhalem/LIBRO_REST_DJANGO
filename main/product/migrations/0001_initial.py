# Generated by Django 5.1.1 on 2024-09-22 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('brand', models.CharField(default='', max_length=200)),
                ('categoty', models.CharField(choices=[('computer', 'Computer'), ('food', 'Food'), ('home', 'Home'), ('kids', 'Kids')], max_length=40)),
                ('ratings', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('stock', models.IntegerField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

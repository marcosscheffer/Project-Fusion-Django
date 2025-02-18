# Generated by Django 5.0.7 on 2024-07-22 13:53

import core.models
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ceated at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ceated at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ')),
                ('service', models.CharField(max_length=100, verbose_name='Service')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-stats-up', 'Graphical'), ('lni-users', 'Users'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ceated at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active ')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(max_length=255, verbose_name='Bio')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='team', variations={'thumb': {'crop': True, 'height': 450, 'width': 450}}, verbose_name='Image')),
                ('facebook', models.CharField(max_length=255, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=255, verbose_name='Instagram')),
                ('twitter', models.CharField(max_length=255, verbose_name='Twitter')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.position', verbose_name=core.models.Position)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]

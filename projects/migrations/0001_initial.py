# Generated by Django 3.0.4 on 2020-04-24 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_name', models.CharField(max_length=50)),
                ('pub_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=50)),
                ('comment_text', models.CharField(max_length=300)),
                ('Publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Publication')),
            ],
        ),
    ]

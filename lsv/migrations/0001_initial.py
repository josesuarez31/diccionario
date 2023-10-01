# Generated by Django 4.2.4 on 2023-09-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video', models.CharField(max_length=200)),
                ('numbers', models.ManyToManyField(blank=True, to='lsv.word')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsv.type')),
            ],
        ),
    ]
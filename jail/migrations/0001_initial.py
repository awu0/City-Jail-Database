# Generated by Django 4.2.11 on 2024-04-16 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('criminal_id', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=10)),
                ('v_status', models.CharField(default='N', max_length=1)),
                ('p_status', models.CharField(default='N', max_length=1)),
            ],
        ),
    ]

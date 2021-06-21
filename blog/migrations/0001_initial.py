# Generated by Django 3.2.3 on 2021-05-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('timeStamp', models.DateField(auto_now=True)),
            ],
        ),
    ]

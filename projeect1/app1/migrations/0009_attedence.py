# Generated by Django 2.1.3 on 2018-11-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attedence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('jan', models.CharField(max_length=150)),
                ('feb', models.CharField(max_length=150)),
                ('mar', models.CharField(max_length=150)),
                ('apr', models.CharField(max_length=150)),
                ('may', models.CharField(max_length=150)),
                ('june', models.CharField(max_length=150)),
                ('july', models.CharField(max_length=150)),
                ('aug', models.CharField(max_length=150)),
                ('sep', models.CharField(max_length=150)),
                ('oct', models.CharField(max_length=150)),
                ('nov', models.CharField(max_length=150)),
                ('dec', models.CharField(max_length=150)),
            ],
        ),
    ]

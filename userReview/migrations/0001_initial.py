# Generated by Django 3.1.3 on 2021-07-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('createdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('reviewto', models.CharField(max_length=30)),
                ('reviewdesc', models.CharField(max_length=30)),
                ('reviewdate', models.DateTimeField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userReview.users')),
            ],
        ),
    ]

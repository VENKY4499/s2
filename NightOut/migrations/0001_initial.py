# Generated by Django 4.0.5 on 2022-06-19 21:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NightOut.creator')),
                ('event_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_email', models.EmailField(max_length=100)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NightOut.creator')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NightOut.event')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('event_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NightOut.event')),
                ('event_location1', models.CharField(max_length=50)),
                ('event_location2', models.CharField(max_length=50)),
                ('event_location3', models.CharField(max_length=50)),
                ('event_time1', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_time2', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_time3', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='NightOut.creator')),
            ],
        ),
    ]
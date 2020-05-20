# Generated by Django 3.0.6 on 2020-05-19 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('Home', 'Home')], max_length=255)),
                ('problem', models.TextField()),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

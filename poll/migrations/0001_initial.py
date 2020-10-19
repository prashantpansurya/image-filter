# Generated by Django 3.1 on 2020-08-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('action', models.CharField(choices=[('NO_FILTER', 'NO_FILTER'), ('COLORIZED', 'COLORIZE'), ('GRAYSCALE', 'GRAYSCALE'), ('BLURRED', 'BLURRED'), ('BINARY', 'BINARY'), ('INVERT', 'INVART')], default='no_filter', max_length=10)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

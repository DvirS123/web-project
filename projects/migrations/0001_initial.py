# Generated by Django 2.2 on 2020-03-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Date', models.DateTimeField()),
                ('Body', models.TextField()),
                ('uploaded', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='projects_images/')),
            ],
        ),
    ]

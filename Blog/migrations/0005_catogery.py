# Generated by Django 3.2 on 2022-08-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catogery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
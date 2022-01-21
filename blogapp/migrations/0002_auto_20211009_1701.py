# Generated by Django 3.1.7 on 2021-10-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=1000)),
                ('gold', models.IntegerField(default=0)),
                ('silver', models.IntegerField(default=0)),
                ('bronze', models.IntegerField(default=0)),
                ('platinum', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
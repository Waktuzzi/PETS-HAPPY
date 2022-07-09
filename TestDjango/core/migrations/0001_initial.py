# Generated by Django 4.0.5 on 2022-07-08 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('stock', models.IntegerField(null=True)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('descuento', models.CharField(max_length=2)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
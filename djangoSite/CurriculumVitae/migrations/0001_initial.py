
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('surname', models.CharField(max_length=100, verbose_name='Soyisim')),
                ('placeofbirth', models.CharField(max_length=100, verbose_name='Doğum Yeri')),
                ('dateofbirth', models.DateField(verbose_name='Doğum Tarihi')),
                ('maritalstatu', models.CharField(max_length=10, verbose_name='Medeni Hal')),
                ('militarystatu', models.CharField(max_length=100, verbose_name='Askerlik Durumu')),
                ('driverlicense', models.CharField(max_length=100, verbose_name='Sürücü Belgesi')),
                ('job', models.CharField(max_length=100, verbose_name='Meslek')),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('language', models.CharField(max_length=100, verbose_name='Dil')),
                ('lgdegree', models.CharField(max_length=50, verbose_name='Deneyim')),
                ('hobby', models.TextField()),
                ('careerobjective', models.TextField(verbose_name='Kariyer Hedefi')),
                ('university', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('unistartdate', models.DateField(verbose_name='Başlama Tarihi')),
                ('uniduedate', models.DateField(verbose_name='Bitiş Tarihi')),
                ('highschool', models.CharField(max_length=250)),
                ('highstartdate', models.DateField(verbose_name='Başlama Tarihi')),
                ('highduedate', models.DateField(verbose_name='Bitiş Tarihi')),
                ('referencename', models.CharField(blank=True, max_length=100, verbose_name='Referans İsim Soyisim')),
                ('referencephone', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Referans Telefon')),
                ('ability', models.TextField(verbose_name='Yetenekler')),
                ('github', models.CharField(blank=True, max_length=250)),
                ('linkedin', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

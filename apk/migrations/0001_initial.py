# Generated by Django 4.1.7 on 2024-08-24 16:07

import apk.models
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
            name='Coopérative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=apk.models.Coopérative.user_default_image, upload_to='cooperative/logos/', verbose_name='Logo de la coopérative')),
                ('nom', models.CharField(help_text='Nom de la coopérative.', max_length=100, verbose_name='Nom')),
                ('type_cooperative', models.CharField(help_text='Type de la coopérative (SCOOPS, COOP-CA, UCOOP, GIC).', max_length=50, verbose_name='Type')),
                ('siege_social', models.CharField(help_text='Adresse du siège social de la coopérative.', max_length=100, verbose_name='Siège Social')),
                ('nom_responsable', models.CharField(help_text='Nom du responsable de la coopérative.', max_length=100, verbose_name='Nom du Responsable')),
                ('contact_responsable', models.CharField(help_text='Numéro de téléphone ou email du responsable de la coopérative.', max_length=100, verbose_name='Contact du Responsable')),
                ('region', models.CharField(help_text='Région où se trouve la coopérative.', max_length=100, verbose_name='Région')),
                ('departement', models.CharField(help_text='Département où se trouve la coopérative.', max_length=100, verbose_name='Département')),
                ('arrondissement', models.CharField(help_text='Arrondissement où se trouve la coopérative.', max_length=100, verbose_name='Arrondissement')),
                ('village', models.CharField(help_text='Village où se trouve la coopérative.', max_length=100, verbose_name='Village')),
                ('coordonnees_gps', models.CharField(help_text='Coordonnées GPS du siège social de la coopérative.', max_length=100, verbose_name='Coordonnées GPS')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
            ],
            options={
                'verbose_name': 'Coopérative',
                'verbose_name_plural': 'Coopératives',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_lot', models.CharField(help_text='Numéro unique identifiant le lot de cacao.', max_length=100, unique=True, verbose_name='Numéro de Lot')),
                ('quantite', models.FloatField(help_text='Quantité de cacao dans le lot en kilogrammes.', verbose_name='Quantité')),
                ('type_commercial', models.CharField(help_text='Type commercial du cacao.', max_length=100, verbose_name='Type Commercial')),
                ('taux_humidite', models.FloatField(help_text="Taux d'humidité du cacao dans le lot.", verbose_name="Taux d'Humidité")),
                ('date_recolte', models.DateField(help_text='Date à laquelle le cacao a été récolté.', verbose_name='Date de Récolte')),
                ('date_livraison', models.DateField(help_text='Date à laquelle le lot de cacao a été livré à la coopérative.', verbose_name='Date de Livraison')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('cooperative', models.ForeignKey(help_text='Coopérative où le lot a été déposé.', on_delete=django.db.models.deletion.CASCADE, to='apk.coopérative', verbose_name='Coopérative')),
            ],
            options={
                'verbose_name': 'Lot',
                'verbose_name_plural': 'Lots',
            },
        ),
        migrations.CreateModel(
            name='Producteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifiant_unique', models.CharField(help_text='Identifiant unique généré à partir des trois premières lettres du nom, de la localité, et de la date de naissance.', max_length=100, unique=True, verbose_name='Identifiant Unique')),
                ('nom', models.CharField(help_text='Nom de famille du producteur.', max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(help_text='Prénom du producteur.', max_length=100, verbose_name='Prénom')),
                ('date_naissance', models.DateField(help_text='Date de naissance du producteur.', verbose_name='Date de Naissance')),
                ('lieu_naissance', models.CharField(help_text='Lieu de naissance du producteur.', max_length=100, verbose_name='Lieu de Naissance')),
                ('genre', models.CharField(help_text='Genre du producteur (Homme/Femme).', max_length=10, verbose_name='Genre')),
                ('nci', models.CharField(help_text="Numéro de la carte d'identité nationale du producteur.", max_length=100, verbose_name="Numéro de Carte d'Identité")),
                ('identifiant_fodecc_cicc', models.CharField(help_text='Identifiant du producteur au sein des organisations FODECC/CICC.', max_length=100, verbose_name='Identifiant FODECC/CICC')),
                ('numero_telephone', models.CharField(help_text='Numéro de téléphone du producteur.', max_length=20, verbose_name='Numéro de Téléphone')),
                ('region', models.CharField(help_text='Région où réside le producteur.', max_length=100, verbose_name='Région')),
                ('departement', models.CharField(help_text='Département où réside le producteur.', max_length=100, verbose_name='Département')),
                ('arrondissement', models.CharField(help_text='Arrondissement où réside le producteur.', max_length=100, verbose_name='Arrondissement')),
                ('village', models.CharField(help_text='Village où réside le producteur.', max_length=100, verbose_name='Village')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
            ],
            options={
                'verbose_name': 'Producteur',
                'verbose_name_plural': 'Producteurs',
            },
        ),
        migrations.CreateModel(
            name='Sac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.CharField(help_text="QR code permettant de tracer le sac et les lots qu'il contient.", max_length=255, verbose_name='QR Code')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('lots', models.ManyToManyField(help_text='Lots de cacao contenus dans le sac.', related_name='sacs', to='apk.lot', verbose_name='Lots')),
            ],
            options={
                'verbose_name': 'Sac',
                'verbose_name_plural': 'Sacs',
            },
        ),
        migrations.CreateModel(
            name='Parcelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_titre_foncier', models.CharField(help_text='Numéro de titre foncier de la parcelle.', max_length=100, verbose_name='Numéro de Titre Foncier')),
                ('statut', models.CharField(help_text='Statut légal de la parcelle.', max_length=100, verbose_name='Statut')),
                ('coordonnees_polygonale', models.TextField(help_text='Coordonnées géographiques en forme de polygone définissant les limites de la parcelle.', verbose_name='Coordonnées Polygonale')),
                ('superficie', models.FloatField(help_text='Superficie de la parcelle en hectares.', verbose_name='Superficie')),
                ('nombre_arbres', models.IntegerField(help_text="Nombre total d'arbres sur la parcelle.", verbose_name="Nombre d'Arbres")),
                ('age_moyen_arbres', models.FloatField(help_text='Âge moyen des arbres sur la parcelle.', verbose_name='Âge Moyen des Arbres')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('producteur', models.ForeignKey(help_text='Producteur auquel appartient cette parcelle.', on_delete=django.db.models.deletion.CASCADE, to='apk.producteur', verbose_name='Producteur')),
            ],
            options={
                'verbose_name': 'Parcelle',
                'verbose_name_plural': 'Parcelles',
            },
        ),
        migrations.AddField(
            model_name='lot',
            name='parcelle',
            field=models.ForeignKey(help_text='Parcelle auquel appartient ce lot.', on_delete=django.db.models.deletion.CASCADE, to='apk.parcelle', verbose_name='Parcelle'),
        ),
        migrations.AddField(
            model_name='lot',
            name='producteur',
            field=models.ForeignKey(help_text="Producteur à l'origine du lot de cacao.", on_delete=django.db.models.deletion.CASCADE, to='apk.producteur', verbose_name='Producteur'),
        ),
        migrations.AddField(
            model_name='coopérative',
            name='producteurs',
            field=models.ManyToManyField(help_text='Liste des producteurs membres de la coopérative.', related_name='cooperatives', to='apk.producteur', verbose_name='Producteurs'),
        ),
        migrations.AddField(
            model_name='coopérative',
            name='user',
            field=models.OneToOneField(help_text='Identifiant unique de la coopérative.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Identifiant Unique'),
        ),
        migrations.CreateModel(
            name='Acheteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(help_text="Nom de l'acheteur.", max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(help_text="Prénom de l'acheteur.", max_length=100, verbose_name='Prénom')),
                ('type_acheteur', models.CharField(help_text="Type de l'acheteur (LBA, Exportateur, etc.).", max_length=50, verbose_name='Type')),
                ('numero_cni', models.CharField(help_text="Numéro de la carte nationale d'identité de l'acheteur.", max_length=100, verbose_name='Numéro de CNI')),
                ('numero_oncc', models.CharField(help_text="Numéro ONCC de l'acheteur.", max_length=100, verbose_name='Numéro ONCC')),
                ('contact', models.CharField(help_text="Numéro de téléphone ou email de l'acheteur.", max_length=100, verbose_name='Contact')),
                ('filiale', models.CharField(help_text="Filiale à laquelle l'acheteur est rattaché.", max_length=100, verbose_name='Filiale')),
                ('coordonnees_geographiques', models.CharField(help_text="Coordonnées géographiques du lieu de résidence ou d'activité de l'acheteur.", max_length=255, verbose_name='Coordonnées Géographiques')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('sacs', models.ManyToManyField(help_text="Sacs de cacao achetés par l'acheteur.", related_name='acheteurs', to='apk.sac', verbose_name='Sacs')),
            ],
            options={
                'verbose_name': 'Acheteur',
                'verbose_name_plural': 'Acheteurs',
            },
        ),
    ]

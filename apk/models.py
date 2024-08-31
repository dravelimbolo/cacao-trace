from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import string

def generate_unique_id( ):
    unique_digits = ''.join(random.choices(string.digits, k=4))
    return f"{unique_digits}"


class Producteur(models.Model):
    identifiant_unique = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Identifiant Unique",
        help_text="Identifiant unique généré à partir des trois premières lettres du nom, de la localité, et de la date de naissance.",
    )
    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Nom de famille du producteur."
    )
    prenom = models.CharField(
        max_length=100, verbose_name="Prénom", help_text="Prénom du producteur."
    )
    date_naissance = models.DateField(
        verbose_name="Date de Naissance", help_text="Date de naissance du producteur."
    )
    lieu_naissance = models.CharField(
        max_length=100,
        verbose_name="Lieu de Naissance",
        help_text="Lieu de naissance du producteur.",
    )
    genre = models.CharField(
        max_length=10,
        verbose_name="Genre",
        help_text="Genre du producteur (Homme/Femme).",
    )
    nci = models.CharField(
        max_length=100,
        verbose_name="Numéro de Carte d'Identité",
        help_text="Numéro de la carte d'identité nationale du producteur.",
    )
    identifiant_fodecc_cicc = models.CharField(
        max_length=100,
        verbose_name="Identifiant FODECC/CICC",
        help_text="Identifiant du producteur au sein des organisations FODECC/CICC.",
    )
    numero_telephone = models.CharField(
        max_length=20,
        verbose_name="Numéro de Téléphone",
        help_text="Numéro de téléphone du producteur.",
    )
    region = models.CharField(
        max_length=100,
        verbose_name="Région",
        help_text="Région où réside le producteur.",
    )
    departement = models.CharField(
        max_length=100,
        verbose_name="Département",
        help_text="Département où réside le producteur.",
    )
    arrondissement = models.CharField(
        max_length=100,
        verbose_name="Arrondissement",
        help_text="Arrondissement où réside le producteur.",
    )
    village = models.CharField(
        max_length=100,
        verbose_name="Village",
        help_text="Village où réside le producteur.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )

    def save(self, *args, **kwargs):
        if not self.identifiant_unique:
            self.identifiant_unique = generate_unique_id()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Producteur"
        verbose_name_plural = "Producteurs"


class Parcelle(models.Model):
    producteur = models.ForeignKey(
        Producteur,
        on_delete=models.CASCADE,
        verbose_name="Producteur",
        help_text="Producteur auquel appartient cette parcelle.",
    )
    numero_titre_foncier = models.CharField(
        max_length=100,
        verbose_name="Numéro de Titre Foncier",
        help_text="Numéro de titre foncier de la parcelle.",
    )
    statut = models.CharField(
        max_length=100, verbose_name="Statut", help_text="Statut légal de la parcelle."
    )
    coordonnees_polygonale = models.TextField(
        verbose_name="Coordonnées Polygonale",
        help_text="Coordonnées géographiques en forme de polygone définissant les limites de la parcelle.",
    )
    superficie = models.FloatField(
        verbose_name="Superficie", help_text="Superficie de la parcelle en hectares."
    )
    nombre_arbres = models.IntegerField(
        verbose_name="Nombre d'Arbres",
        help_text="Nombre total d'arbres sur la parcelle.",
    )
    age_moyen_arbres = models.FloatField(
        verbose_name="Âge Moyen des Arbres",
        help_text="Âge moyen des arbres sur la parcelle.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )


    class Meta:
        verbose_name = "Parcelle"
        verbose_name_plural = "Parcelles"


class Coopérative(models.Model):


    def user_default_image():
        return "cooperative/logo.png"
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Identifiant Unique",
        help_text="Identifiant unique de la coopérative.",
    )
    image =   models.ImageField(
        upload_to='cooperative/logos/',
        verbose_name="Logo de la coopérative",
        default=user_default_image
    )
    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Nom de la coopérative."
    )
    type_cooperative = models.CharField(
        max_length=50,
        verbose_name="Type",
        help_text="Type de la coopérative (SCOOPS, COOP-CA, UCOOP, GIC).",
    )
    siege_social = models.CharField(
        max_length=100,
        verbose_name="Siège Social",
        help_text="Adresse du siège social de la coopérative.",
    )
    nom_responsable = models.CharField(
        max_length=100,
        verbose_name="Nom du Responsable",
        help_text="Nom du responsable de la coopérative.",
    )
    contact_responsable = models.CharField(
        max_length=100,
        verbose_name="Contact du Responsable",
        help_text="Numéro de téléphone ou email du responsable de la coopérative.",
    )
    region = models.CharField(
        max_length=100,
        verbose_name="Région",
        help_text="Région où se trouve la coopérative.",
    )
    departement = models.CharField(
        max_length=100,
        verbose_name="Département",
        help_text="Département où se trouve la coopérative.",
    )
    arrondissement = models.CharField(
        max_length=100,
        verbose_name="Arrondissement",
        help_text="Arrondissement où se trouve la coopérative.",
    )
    village = models.CharField(
        max_length=100,
        verbose_name="Village",
        help_text="Village où se trouve la coopérative.",
    )
    coordonnees_gps = models.CharField(
        max_length=100,
        verbose_name="Coordonnées GPS",
        help_text="Coordonnées GPS du siège social de la coopérative.",
    )
    producteurs = models.ManyToManyField(
        Producteur,
        related_name="cooperatives",
        verbose_name="Producteurs",
        help_text="Liste des producteurs membres de la coopérative.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )

    class Meta:
        verbose_name = "Coopérative"
        verbose_name_plural = "Coopératives"


class Lot(models.Model):
    producteur = models.ForeignKey(
        Producteur,
        on_delete=models.CASCADE,
        verbose_name="Producteur",
        help_text="Producteur à l'origine du lot de cacao.",
    )
    cooperative = models.ForeignKey(
        Coopérative,
        on_delete=models.CASCADE,
        verbose_name="Coopérative",
        help_text="Coopérative où le lot a été déposé.",
    )
    parcelle = models.ForeignKey(
        Parcelle,
        on_delete=models.CASCADE,
        verbose_name="Parcelle",
        help_text="Parcelle auquel appartient ce lot.",
    )
    numero_lot = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Numéro de Lot",
        help_text="Numéro unique identifiant le lot de cacao.",
    )
    quantite = models.FloatField(
        verbose_name="Quantité",
        help_text="Quantité de cacao dans le lot en kilogrammes.",
    )
    type_commercial = models.CharField(
        max_length=100,
        verbose_name="Type Commercial",
        help_text="Type commercial du cacao.",
    )
    taux_humidite = models.FloatField(
        verbose_name="Taux d'Humidité",
        help_text="Taux d'humidité du cacao dans le lot.",
    )
    date_recolte = models.DateField(
        verbose_name="Date de Récolte",
        help_text="Date à laquelle le cacao a été récolté.",
    )
    date_livraison = models.DateField(
        verbose_name="Date de Livraison",
        help_text="Date à laquelle le lot de cacao a été livré à la coopérative.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )

    class Meta:
        verbose_name = "Lot"
        verbose_name_plural = "Lots"


class Sac(models.Model):
    lots = models.ManyToManyField(
        Lot,
        related_name="sacs",
        verbose_name="Lots",
        help_text="Lots de cacao contenus dans le sac.",
    )
    qr_code = models.CharField(
        max_length=255,
        verbose_name="QR Code",
        help_text="QR code permettant de tracer le sac et les lots qu'il contient.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )

    class Meta:
        verbose_name = "Sac"
        verbose_name_plural = "Sacs"


class Acheteur(models.Model):
    nom = models.CharField(
        max_length=100, verbose_name="Nom", help_text="Nom de l'acheteur."
    )
    prenom = models.CharField(
        max_length=100, verbose_name="Prénom", help_text="Prénom de l'acheteur."
    )
    type_acheteur = models.CharField(
        max_length=50,
        verbose_name="Type",
        help_text="Type de l'acheteur (LBA, Exportateur, etc.).",
    )
    numero_cni = models.CharField(
        max_length=100,
        verbose_name="Numéro de CNI",
        help_text="Numéro de la carte nationale d'identité de l'acheteur.",
    )
    numero_oncc = models.CharField(
        max_length=100,
        verbose_name="Numéro ONCC",
        help_text="Numéro ONCC de l'acheteur.",
    )
    contact = models.CharField(
        max_length=100,
        verbose_name="Contact",
        help_text="Numéro de téléphone ou email de l'acheteur.",
    )
    filiale = models.CharField(
        max_length=100,
        verbose_name="Filiale",
        help_text="Filiale à laquelle l'acheteur est rattaché.",
    )
    coordonnees_geographiques = models.CharField(
        max_length=255,
        verbose_name="Coordonnées Géographiques",
        help_text="Coordonnées géographiques du lieu de résidence ou d'activité de l'acheteur.",
    )
    sacs = models.ManyToManyField(
        Sac,
        related_name="acheteurs",
        verbose_name="Sacs",
        help_text="Sacs de cacao achetés par l'acheteur.",
    )

    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de Création"
    )
    date_modification = models.DateTimeField(
        auto_now=True, verbose_name="Date de Modification"
    )

    class Meta:
        verbose_name = "Acheteur"
        verbose_name_plural = "Acheteurs"

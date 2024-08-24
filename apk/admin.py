from django.contrib import admin
from .models import *

@admin.register(Producteur)
class ProducteurAdmin(admin.ModelAdmin):
    list_display = ('identifiant_unique', 'nom', 'prenom', 'date_naissance', 'region', 'departement', 'arrondissement', 'village', 'date_creation')
    search_fields = ('nom', 'prenom', 'identifiant_unique', 'numero_telephone')
    list_filter = ('region', 'departement', 'genre', 'date_creation')
    ordering = ('-date_creation',)
    readonly_fields = ('identifiant_unique', 'date_creation', 'date_modification')


@admin.register(Parcelle)
class ParcelleAdmin(admin.ModelAdmin):
    list_display = ('producteur', 'numero_titre_foncier', 'superficie', 'nombre_arbres', 'age_moyen_arbres', 'date_creation')
    search_fields = ('numero_titre_foncier', 'producteur__nom', 'producteur__prenom')
    list_filter = ('superficie', 'statut', 'date_creation')
    ordering = ('-date_creation',)
    readonly_fields = ('date_creation', 'date_modification')


@admin.register(Coopérative)
class CooperativeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nom_responsable', 'type_cooperative', 'region', 'date_creation')
    search_fields = ('nom', 'nom_responsable', 'region')
    list_filter = ('region', 'type_cooperative', 'date_creation')
    ordering = ('-date_creation',)
    readonly_fields = ('date_creation', 'date_modification')


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('numero_lot', 'producteur', 'cooperative', 'quantite', 'date_recolte', 'date_livraison', 'date_creation')
    search_fields = ('numero_lot', 'producteur__nom', 'cooperative__nom')
    list_filter = ('cooperative', 'date_recolte', 'date_livraison')
    ordering = ('-date_creation',)
    readonly_fields = ('date_creation', 'date_modification')


@admin.register(Sac)
class SacAdmin(admin.ModelAdmin):
    list_display = ('qr_code', 'date_creation')
    search_fields = ('qr_code',)
    ordering = ('-date_creation',)
    readonly_fields = ('date_creation', 'date_modification')


@admin.register(Acheteur)
class AcheteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'type_acheteur', 'contact', 'filiale', 'date_creation')
    search_fields = ('nom', 'prenom', 'numero_cni', 'contact')
    list_filter = ('type_acheteur', 'filiale', 'date_creation')
    ordering = ('-date_creation',)
    readonly_fields = ('date_creation', 'date_modification')

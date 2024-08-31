from django.urls import path
from rest_framework.authtoken import views as AuthTokenView

from . import views

urlpatterns = [

    # path('change-password/', views.change_password, name='change_password'),
    # path('create-user/', views.UserCreateView.as_view(), name='user-signup'),
    # path('client-list/', views.ClientListView.as_view(), name='client-detail'),
    path('api-token-auth/', AuthTokenView.obtain_auth_token, name='user-signin'),
    # path('change-client-image/', views.ClientImageUpdateView.as_view(), name='change-client-image'),

    path('producteur-list/', views.ListView.as_view(), name='tout-producteur'),
    # path('create-user-producteur/', views.ProducteurCreateView.as_view(), name='create-producteur'),
    # path('producteur-list/<int:id>/delete-producteur/', views.ProducteurDeleteView.as_view(), name='delete-producteur'),
    # path('producteur-list/<int:id>/update-producteur/', views.ProducteurUpdateView.as_view(), name='update-producteur'),
    # path('producteur-list/<int:id>/producteur-details/', views.ProducteurDetailsView.as_view(), name='producteur-details'),


    # path('propriete-list/', views.ProprieteListView.as_view(), name='tout-propriete'),
    # path('sauvegarde-list/', views.ProprieteSauvListView.as_view(), name='sauvegarde-propriete'),
    # path('propriete-recherche/', views.ProprieteRechListView.as_view(), name='propriete_recherche'),

]
from django.urls import path

from . import views


urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('patient/', views.index, name='index'),
    path('medecin/', views.indexmed, name='indexmed'),
  

    path('pharmacies/', views.liste_pharmacies, name='liste_pharmacies'),
    path('pharmacies_details/<int:pharmacie_id>/', views.pharmacie_details, name='pharmacie_details'),
    path('medecins/', views.liste_medecins, name='liste_medecins'),
    path('medecin_details/<int:medecin_id>/', views.medecin_details, name='medecin_details'),
    path('footer', views.footer, name='footer'),
    path('patient_commandes', views.commande_patient, name='commande_patient'),
    path('get_products/', views.get_products, name='get_products'),
    path('indexx/', views.indexx, name='indexx'),
    path('details_produit/<int:myid>/', views.details, name='details'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkoutout/', views.checkoutout, name='checkoutout'),

    path('confirmation/', views.confirmation, name='confirmation'),
    path('confirmationpharm/', views.confirmationpharm, name='confirmationpharm'),






    path('connexion', views.connexion, name='connexion'),
]

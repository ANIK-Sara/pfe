from django.contrib import admin
from django.shortcuts import redirect

# Register your models here.

from .models import Commande, Ordonnance, Produit, ProduitPharmaceutique, Medicament , PharmaCommandes 

from .models import HistoriqueMedical, HistoriquePharmaceutique, Livreur , Medecin, Patient, Pharmacie , Login
# Register your models here.
admin.site.register(Patient),
admin.site.register(Medecin),
admin.site.register(Pharmacie),
admin.site.register(HistoriqueMedical),
admin.site.register(HistoriquePharmaceutique),
admin.site.register(ProduitPharmaceutique),
admin.site.register(Medicament),
admin.site.register(Livreur),
admin.site.register(Login)





admin.site.unregister(ProduitPharmaceutique)
admin.site.unregister(Medicament)
class ProduitAdmin(admin.ModelAdmin):
    model = Produit

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['type'].widget.choices = [('Pharmaceutique', 'Produit Pharmaceutique'), ('Medicament', 'Médicament')]
        return form

    def response_add(self, request, obj, post_url_continue=None):
        # Redirection vers l'interface d'ajout appropriée en fonction du type de produit
        if "_addanother" in request.POST:
            if obj.type == 'Pharmaceutique':
                return redirect('http://127.0.0.1:8000/admin/app3/produitpharmaceutique/add/')
            elif obj.type == 'Medicament':
                return redirect('admin:app3_medicament_add')
        return super().response_add(request, obj, post_url_continue)

admin.site.register(ProduitPharmaceutique)
admin.site.register(Medicament)

class AdminProduit(admin.ModelAdmin):
    list_display= ('nom_pr' , 'prix_unitaire', 'type', 'marque_produit' , 'dosage' )
    search_fields = ('nom_pr',)
    list_editable = ('prix_unitaire' ,)

class AdminCommande(admin.ModelAdmin):
    list_display=('nom_utilisateur' , 'prenom_utilisateur' , 'date_commande' , 'total' , 'adr_mail' , 'num_tel' ,  'adresse' , 'ville' , 'items')
    search_fields = ('nom_utilisateur', )
admin.site.register(Commande , AdminCommande)
admin.site.register(Produit , AdminProduit )
class AdminCommande(admin.ModelAdmin):
    list_display=('nom_utilisateur' , 'prenom_utilisateur' , 'date_commande' , 'total' , 'adr_mail' , 'num_tel' ,  'adresse' , 'ville' , 'items')
    search_fields = ('nom_utilisateur', )
admin.site.register(PharmaCommandes , AdminCommande)
class AdminOrdonnance(admin.ModelAdmin):
    list_display=('nom_medecin' , 'adresse_cabinet' , 'specialite' , 'nom_patient' , 'prenom_patient' , 'num_tel' ,  'liste_produits' )
    search_fields = ('nom_medecin', )
admin.site.register(Ordonnance , AdminOrdonnance)

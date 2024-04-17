from django.shortcuts import render, redirect , get_object_or_404
from django.core.exceptions import ValidationError
from .models import Login, Medecin, Patient, Pharmacie , Produit , Ordonnance , Commande , PharmaCommandes
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.http import JsonResponse
from .models import Pharmacie
from django.core.paginator import Paginator 
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)

import json
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Login, Patient, Medecin, Pharmacie
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm

def inscription(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom')
        prenom_utilisateur = request.POST.get('prenom')
        password = request.POST.get('psww')
        adr_mail = request.POST.get('mail')
        num_tel = request.POST.get('tel')
        date = request.POST.get('date')
        sexe = request.POST.get('sexe')
        adresse = request.POST.get('adress')
        role = request.POST.get('role')

        specialite = request.POST.get('specialite', '')
        adresse_cabinet = request.POST.get('adresse_cabinet', '')
        nom_responsable = request.POST.get('nom_responsable', '')
        heure_ouverture = request.POST.get('heure_ouverture', '')
        heure_fermeture = request.POST.get('heure_fermeture', '')

        # Récupérer les images téléchargées
        avatar = request.FILES.get('avatar', '')
        avatar2 = request.FILES.get('avatar2', '')

        try:
            if Login.objects.filter(nom_utilisateur=nom_utilisateur).exists():
                raise ValidationError(
                    "Le nom d'utilisateur est déjà pris par quelqu'un d'autre ! Veuillez choisir un autre")

            # Enregistrer l'image sur le serveur
            if avatar:
                fs = FileSystemStorage()
                nom_fichier = fs.save(avatar.name, avatar)
                chemin_fichier = fs.url(nom_fichier)
            else:
                # Si aucun avatar n'a été téléchargé, utiliser une valeur par défaut
                chemin_fichier = "static/image/lieu2.jpg"

            # Créer un nouvel utilisateur
            nouvel_utilisateur = Login.objects.create(
                nom_utilisateur=nom_utilisateur,
                prenom_utilisateur=prenom_utilisateur,
                password=password,
                adr_mail=adr_mail,
                num_tel=num_tel,
                date=date,
                sexe=sexe,
                adresse=adresse,
                role=role,
                avatar=chemin_fichier  # Enregistrer le chemin de l'image dans la base de données
            )
            nouvel_utilisateur.save()

            # Enregistrer les données spécifiques au rôle dans la base de données
            if role == 'patient':
                data2 = Patient.objects.create(
                    nom_patient=nom_utilisateur,
                    prenom_patient=prenom_utilisateur,
                    adr_mail=adr_mail,
                    num_tel=num_tel,
                    date=date,
                    sexe=sexe,
                    adressePa=adresse,
                )
                data2.save()
                context = {'message': 'Utilisateur créé avec succès'}

            elif role == 'med':
                medecin = Medecin.objects.create(
                    nom_medecin=nom_utilisateur,
                    prenom_medecin=prenom_utilisateur,
                    adr_mailM=adr_mail,
                    num_telM=num_tel,
                    date=date,
                    sexe=sexe,
                    specialite=specialite,
                    adresse_cabinet=adresse_cabinet,
                    signature=avatar2, 
                )
                medecin.save()
                context = {'message': 'Utilisateur créé avec succès',
                           'role_data': medecin}

            elif role == 'pharma':
                pharmacie = Pharmacie.objects.create(
                    nom=nom_utilisateur,
                    adresse=adresse,
                    nom_responsable=nom_responsable,
                    tel=num_tel,
                    mail=adr_mail,
                    heure_ouverture=heure_ouverture,
                    heure_fermeture=heure_fermeture,
                    avatar=avatar,
                )
                pharmacie.save()
                context = {'message': 'Utilisateur créé avec succès',
                           'role_data': pharmacie}

            return render(request, 'app3/success_page.html', context)

        except ValidationError as e:
            return render(request, 'app3/sign_up.html', {'error_message': e.message})
    else:
        return render(request, 'app3/login.html')



def connexion(request):
    print("salut")
    if request.method == 'POST':
        print("post")
        print("Données reçues dans la requête POST :", request.POST)

        username = request.POST['uname']
        password = request.POST['psw']
        print("Valeurs des champs username et password avant l'appel à authenticate :")
        print("Nom d'utilisateur :", username)
        print("Mot de passe :", password)
        user = authenticate(request, nom_utilisateur=username, password=password)
        print("authetnicate")
         
        if user is not None:
            print("is not none")
            login(request, user)
            # Redirection en fonction du rôle de l'utilisateur
            if user.role == 'patient':
                return redirect('interface_patient')
            elif user.role == 'med':
                return redirect('interface_medecin')
            elif user.role == 'pharma':
                return redirect('interface_pharma')
            else:
                # Gérer d'autres rôles ou cas ici
                return redirect('page_accueil')  # Rediriger vers une page par défaut
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'app3/index.html', {'error_message': error_message})
    
    return render(request, 'app3/index.html')




def index(request ):
    return render(request , 'app3/interface_patient.html' ) 

def indexmed(request ):
    if request.method == "POST":
        print("la méthode est post")
        print("ça marche ")
        nom_medecin = request.POST.get('doctorName')
        specialite = request.POST.get('specialty')
        adresse_cabinet = request.POST.get('hospital')
        
        nom_patient = request.POST.get('patientName')
        prenom_patient = request.POST.get('patientfirstname')
        num_tel = request.POST.get('phoneNumber')
        liste_produits = request.POST.get('medicinesList')

        # Vérifier que les champs requis ne sont pas vides
      
            # Créer l'objet Ordonnance seulement si tous les champs sont remplis
        ord = Ordonnance(nom_medecin=nom_medecin , adresse_cabinet=adresse_cabinet , specialite=specialite ,
                             nom_patient=nom_patient , prenom_patient=prenom_patient , num_tel=num_tel , liste_produits=liste_produits)
        ord.save() 
        print("ordonnance ajoutée :")
        return redirect('confirmationpharm')
    else: 
        print("le problleme est dans post je crois")
    return render(request , 'app3/interface_medecin.html' ) 

def footer(request):
    return render(request , 'app3/footer.html')
def commande_patient(request):
    produits = Produit.objects.all()
    return render(request , 'app3/patient_commandes.html' , {'produits': produits})

def get_products(request):
    produits = Produit.objects.all().values('id', 'nom_pr', 'prix_unitaire', 'image')
    return JsonResponse(list(produits), safe=False)

def liste_pharmacies(request):
    return render (request , 'app3/pharmacies.html' ,
{'pharma':Pharmacie.objects.all()})





def indexx(request):
    all_products = Produit.objects.all().order_by('nom_pr')
    item_name = request.GET.get('item-name') 
    if item_name and item_name != '':
        all_products = all_products.filter(nom_pr__icontains=item_name)
    
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)

    return render(request, 'app3/index.html', {'product_object': product_object})



def details(request , myid):
    product_object = Produit.objects.get(id_produit=myid)
    return render(request , 'app3/details.html' , {'product': product_object})

def checkout(request):
    if request.method == "POST":
        nom_utilisateur = request.POST.get('nom')
        total = request.POST.get('total')
        prenom_utilisateur = request.POST.get('prenom')
        adr_mail = request.POST.get('email')
        num_tel = request.POST.get('tel')
        adresse = request.POST.get('address')
        ville = request.POST.get('ville')
        items = request.POST.get('items') 
        com = Commande(nom_utilisateur=nom_utilisateur, prenom_utilisateur=prenom_utilisateur, total=total ,   adr_mail=adr_mail, num_tel=num_tel ,   adresse=adresse, ville=ville , items=items )
        
        com.save() 
        return redirect('confirmation')
    return render(request , 'app3/checkout.html')

def confirmation (request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom_utilisateur 
    
    return render (request , 'app3/confirmation.html' , {'name' : nom })


def confirmationpharm (request):
    info = PharmaCommandes.objects.all()[:1]
    for item in info:
        nom = item.nom_utilisateur 
    
    return render (request , 'app3/confirmationphar.html' , {'nameph' : nom })




def liste_medecins(request):
    return render (request , 'app3/medecins.html' ,
{'medecins':Medecin.objects.all()})

def get_pharmacie_details(request, pharmacie_id):

    try:
        pharmacie = Pharmacie.objects.get(pk=pharmacie_id)
        data = {
            'nom': pharmacie.nom,
            'adresse': pharmacie.adresse,
            'heure_ouverture': pharmacie.heure_ouverture.strftime('%H:%M'),
            'heure_fermeture': pharmacie.heure_fermeture.strftime('%H:%M')
        }
        return JsonResponse(data)
    except Pharmacie.DoesNotExist:
        return JsonResponse({'error': 'Pharmacie non trouvée'}, status=404)
    

def pharmacie_details(request, pharmacie_id):
    pharmacie = get_object_or_404(Pharmacie, pk=pharmacie_id)
    product_objectt = pharmacie.produits.all()  # Utilisation de la relation avec le modèle de produit
    
    item_namee = request.GET.get('item-namee')
    print("Valeur de item_namee:", item_namee)  # Afficher la valeur de item_namee
    
    if item_namee and item_namee.strip():  # Vérifie si item_namee n'est pas vide
        product_objectt = product_objectt.filter(nom_pr__icontains=item_namee)
    
    print("Produits filtrés:", product_objectt)  # Afficher les produits filtrés
    
    return render(request, 'app3/pharmacie_details.html', {'pharmacie': pharmacie, 'product_objectt': product_objectt,})


def checkoutout(request):
    if request.method == "POST":
        nom_utilisateur = request.POST.get('nom')
        total = request.POST.get('total')
        prenom_utilisateur = request.POST.get('prenom')
        adr_mail = request.POST.get('email')
        num_tel = request.POST.get('tel')
        adresse = request.POST.get('address')
        ville = request.POST.get('ville')
        items = request.POST.get('items') 
        pharcom = PharmaCommandes(nom_utilisateur=nom_utilisateur, prenom_utilisateur=prenom_utilisateur, total=total ,   adr_mail=adr_mail, num_tel=num_tel ,   adresse=adresse, ville=ville , items=items )

        pharcom.save() 
        return redirect('confirmationpharm')
    return render(request , 'app3/checkoutout.html')
def get_medecin_details(request, medecin_id):
    try:
        medecin= Medecin.objects.get(id_medecin=medecin_id)
        data = {
            'nom': medecin.nom_medecin,
            'prenom': medecin.prenom_medecin,
            'spéciallité': medecin.specialite , 
            'adresse_cabinet': medecin.adresse_cabinet
        }
        return JsonResponse(data)
    except Medecin.DoesNotExist:
        return JsonResponse({'error': 'Médecin non trouvée'}, status=404)


def medecin_details(request, medecin_id):
        medecin = get_object_or_404(Medecin, id_medecin=medecin_id)
        return render(request, 'app3/medecin_details.html', {'medecin': medecin})


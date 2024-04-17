from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class Login (models.Model):
    nom_utilisateur = models.CharField(max_length=100, null=True)
    prenom_utilisateur = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    adr_mail = models.EmailField(null=True)
    num_tel = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True)
    sexe = models.CharField(max_length=1, null=True)
    adresse = models.CharField(max_length=1, null=True)
    role = models.CharField(max_length=10, null=True)

    def __str__(self):
        if self.nom_utilisateur:
            return self.nom_utilisateur
        else:
            return "Utilisateur sans nom"

class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True, default=None)
    nom_patient = models.CharField(max_length=100)
    prenom_patient = models.CharField(max_length=100)
    adressePa = models.CharField(max_length=255)
    adr_mail = models.EmailField()
    num_tel = models.CharField(max_length=20)
    date = models.DateField(null=True)
    sexe = models.CharField(max_length=1)

class Medecin(models.Model):
    id_medecin = models.AutoField(primary_key=True, default=None)
    nom_medecin = models.CharField(max_length=100, default=None)
    prenom_medecin = models.CharField(max_length=100, default=None)
    specialite = models.CharField(max_length=100, default=None)
    num_telM = models.CharField(max_length=20, default=None)
    adr_mailM = models.EmailField(default=None)
    adresse_cabinet = models.CharField(max_length=255, default=None)
    date = models.DateField(null=True, default=None)
    sexe = models.CharField(max_length=1, null=True, default=None)
    signature = models.CharField(max_length=255, null=True, blank=True)




class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_pr = models.CharField(max_length=100)
    

    prix_unitaire = models.DecimalField(
        max_digits=10, decimal_places=2, default=None)
    
    image = models.CharField( max_length=2000   , default=None, null=True)

    TYPE_CHOICES = [
        ('Pharmaceutique', 'Produit Pharmaceutique'),
        ('Medicament', 'Médicament'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    # Attributs spécifiques aux médicaments
    marque_produit = models.CharField(max_length=100, blank=True, null=True)
    # Attributs spécifiques aux produits pharmaceutiques
    dosage = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.type == 'Pharmaceutique':
            # Assurez-vous que la marque est remplie pour les médicaments
            if not self.marque_produit:
                raise ValueError("La marque du produit est requise pour les produits pharmaceutiques..")
            # Effacez le dosage si le produit n'est pas un médicament
            self.marque_produit = None
        elif self.type == 'Medicament':
            # Assurez-vous que le dosage est rempli pour les produits pharmaceutiques
            if not self.dosage:
                raise ValueError("Le dosage est requis pour les médicaments..")
            # Effacez la marque si le produit n'est pas pharmaceutique
            self.dosage = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_pr

class Pharmacie(models.Model):
    id_pharmacie = models.AutoField(primary_key=True, default=None)
    nom = models.CharField(max_length=100, default=None)
    adresse = models.CharField(
        max_length=255,  null=True, default="valeur par défaut")
    nom_responsable = models.CharField(max_length=100, default=None)
    tel = models.CharField(max_length=20, default=None)
    mail = models.EmailField(default=None)
    produits = models.ManyToManyField(Produit)
    heure_ouverture = models.TimeField(default=None)
    heure_fermeture = models.TimeField(default=None)
    avatar = models.ImageField( default='image/pharma.jpg')
    def __str__(self):
        return self.nom
class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=100 , default=None)
    prenom_utilisateur = models.CharField(max_length=100 , default=None)
    total = models.CharField(max_length=200 , default=None)
    date_commande = models.DateTimeField(auto_now=True)
    ville = models.CharField(max_length=100 )
    adr_mail = models.CharField(max_length=100 , default=None)
    adresse =  models.CharField(max_length=100 , default=None)
    num_tel = models.CharField(max_length=15, null=True)

    items = models.CharField(max_length=300 , default=None)
   
    class Meta:
        ordering = ['-date_commande']
    def __str__(self):
        return self.nom_utilisateur 

    def clean(self):
        
        
        # Vérification pour nom_utilisateur non null
        if self.nom_utilisateur is None:
            raise ValidationError("Le nom d'utilisateur ne peut pas être vide.")
        

class PharmaCommandes(models.Model):
    id_commandepharm = models.AutoField(primary_key=True)
    nom_utilisateur = models.CharField(max_length=100 , default=None)
    prenom_utilisateur = models.CharField(max_length=100 , default=None)
    total = models.CharField(max_length=200 , default=None)
    date_commande = models.DateTimeField(auto_now=True)
    ville = models.CharField(max_length=100 )
    adr_mail = models.CharField(max_length=100 , default=None)
    adresse =  models.CharField(max_length=100 , default=None)
    num_tel = models.CharField(max_length=15, null=True)

    items = models.CharField(max_length=300 , default=None)
   
    class Meta:
        ordering = ['-date_commande']
    def __str__(self):
        return self.nom_utilisateur 

    def clean(self):
        
        
        # Vérification pour nom_utilisateur non null
        if self.nom_utilisateur is None:
            raise ValidationError("Le nom d'utilisateur ne peut pas être vide.")
        
        

class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True, default=None)
    
    nom_medecin = models.CharField(max_length=100, default=None)
   
    adresse_cabinet = models.CharField(max_length=255, default=None)
    specialite = models.CharField(max_length=100, default=None)

    nom_patient = models.CharField(max_length=100, default=None)
    prenom_patient = models.CharField(max_length=10, default=None)
    num_tel = models.CharField(max_length=20 , default = None)
    
    liste_produits = models.CharField(max_length=1000 , default = None)


class ProduitPharmaceutique(Produit):
    marque_produitpha = models.CharField(max_length=100, default=None)
    produit_ptr = models.OneToOneField(
        Produit, on_delete=models.CASCADE, parent_link=True, primary_key=True, default=None)

class Medicament(Produit):
    dosage_edicaent = models.CharField(max_length=100, default=None)
    produit_ptr = models.OneToOneField(
        Produit, on_delete=models.CASCADE, parent_link=True, primary_key=True, default=None)

class HistoriqueMedical(models.Model):
    id_historiqueM = models.AutoField(primary_key=True, default=None)
    id_patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, default=None)
    id_ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, default=None)

class HistoriquePharmaceutique(models.Model):
    id_historiqueP = models.AutoField(primary_key=True, default=None)
    id_ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, default=None)
    id_pharmacie = models.ForeignKey(
        Pharmacie, on_delete=models.CASCADE, default=None)
    dateP = models.DateField(default=None)
    descriptionP = models.TextField(default=None)
    id_patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, default=None)

class Livreur(models.Model):
    id_livreur = models.AutoField(primary_key=True, default=None)
    nom_liv = models.CharField(max_length=100, default=None)
    prenom_liv = models.CharField(max_length=100, default=None)
    tel_liv = models.CharField(max_length=20, default=None)

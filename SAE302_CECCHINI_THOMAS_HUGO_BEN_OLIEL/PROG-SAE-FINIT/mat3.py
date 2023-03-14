#définit tout les import et modules utilisés 
import kivy 
from kivy.uix.widget import Widget 
from kivy.app import App 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
import base64
import io
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooser
from kivy.uix.image import AsyncImage
import mysql.connector
import requests
import json

#url vers ma page php   
url = "https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php"

#Permet d'avoir une taille de fenetre type smartphone
Config.set('graphics', 'width', '370')
Config.set('graphics', 'height', '700')

#importe le module pour faire des listes 
from kivy.uix.spinner import Spinner

#Classe qui permet de set et get les données des identifiant pour les utilisés dans d'autres  classe plus tard 
class recup:
    
    def __init__(self):

        self.__identifiant= ""
        self.__idetu=""
        

    def get_identifiant(self):
        print(self.__identifiant)
        print("1")
        return self.__identifiant

    def set_identifiant(self,identifiant):
        print("2",identifiant)
        self.__identifiant=str(identifiant.replace(" ",""))

    def get_idetu(self):
        return self.__idetu

    def set_idetu(self,idetu):
        self.__idetu=str(idetu.replace(" ",""))
        
Ratio = recup()


#Ecran d'authentifiaction premeir page quand on lance le programme
class Authentification(Screen):
    pass


#Ecran de connexion deuxieme page quand on lance le programme et qu'on clique sur connexion
class Connexion(Screen):

    idetu=ObjectProperty(None)
    mdp=ObjectProperty(None)
    affi=ObjectProperty(None)
    button=ObjectProperty(None)

    #Pemret de cacher/affiché le mot de passe en caractere étoilé 
    def togglevisibility(self):
        if self.mdp.password == True:
            self.mdp.password = False
            self.button.text = 'Hide'

        elif self.mdp.password == False:
            self.mdp.password = True
            self.button.text = 'Show'
    
    #Permet de récupérer la valuer rentrer par l'user dans le champ identifiant et mdp puis de les comparer à une liste récupérant toutes les infos de la bd 
    #Et de si l'identifiant et mdp est bon alors afficher Identifiant/mdp correct sinon afficher Identifiant/mdp incorrect et ressayer
    def login(self):

        Ratio.set_idetu(self.idetu.text)
        mdp=self.mdp.text
        affi=self.affi.text

        etudiant={'table':'etudiants'}
        response = requests.get('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant)
        data = response.json()
        # print(data)
        liste= []


        for student in data:
            liste.append(student["id"])
        
        #print (liste)
        
        if self.idetu.text not in liste:
            print("Identifiant/mdp Incorrect")
            self.affi.text="Identifiant/mdp Incorrecte"
            self.idetu.text=""
            self.mdp.text=""
            
        else:
            print("Identifiant correcte")
            self.affi.text="Identifiant correcte"

#cette class permet la gestion de fenetre 
class WindowManager(ScreenManager):
    pass

#Cette class permet à l'utilisateur de s'inscire à l'aide de champs input
#Puis d'envoyer toutes ces données à la bd quand le bouton est appuyer
class FirstWindow(Screen):

    spinner=ObjectProperty(None)
    identifiant=ObjectProperty(None)
    annee=ObjectProperty(None)
    nom=ObjectProperty(None)
    prenom=ObjectProperty(None)
    matiere1=ObjectProperty(None)
    matiere2=ObjectProperty(None)
    matiere3=ObjectProperty(None)
    matiere4=ObjectProperty(None)
    mdp=ObjectProperty(None)

    def press(self):

        #url de ma page php         
        url = "https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php"

        #définit les input
        spinner=self.spinner.text
        Ratio.set_identifiant(self.identifiant.text)
        # identifiant=self.identifiant.text
        annee=self.annee.text
        nom=self.nom.text
        prenom=self.prenom.text
        matiere1=self.matiere1.text
        matiere2=self.matiere2.text
        matiere3=self.matiere3.text
        matiere4=self.matiere4.text
        mdp=self.mdp.text

        #Verifie que tout est bien récuperé
        print({spinner,self.identifiant.text,annee,nom,prenom,matiere1,matiere2,matiere3,matiere4,mdp})

        #connexion à la base de données 
        insert_etudiants = {
            "table": "etudiants", # La table qu'on veut affecté
            "id": self.identifiant.text,  #la clef et sa valeur
            "nom": nom, # la clef et sa valeur 
            "prenom": prenom,  # la clef et sa valeur 
            "annee": annee,  # la clef et sa valeur 
            "password": mdp,   # la clef et sa valeur
            "statut":spinner # la clef et sa valeur
        }

        insert_matieres = {
            "table": "matieres", # La table qu'on veut affecté 
            "id_etu": self.identifiant.text, # la clef et sa valeur 
            "matiere1": matiere1,  # la clef et sa valeur 
            "matiere2": matiere2,  # la clef et sa valeur 
            "matiere3": matiere3,  # la clef et sa valeur 
            "matiere4": matiere4  # la clef et sa valeur 
        }

        """Toutes les conditions d'enregistrement"""


        # if identifiant.isdigit():
        #     identifiant = int(identifiant)
        # else:
        #     print("identifiant doit etre un nombre entier")

        if annee.isdigit():
            annee = int(annee)
        else:
            print("Annee doit etre un nombre entier")

        if matiere1.isdigit():
            matiere1 = float(matiere1)
        else:
            print("La note d'Anglais doit etre un chiffre/nombre")

        if matiere2.isdigit():
            matiere2 = float(matiere2)
        else:
            print("La note de Mathématiques doit etre un chiffre/nombre")

        if matiere3.isdigit():
            matiere3 = float(matiere3)
        else:
            print("La note d'Informatique doit etre un chiffre/nombre")


        if matiere4.isdigit():
            matiere4 = float(matiere4)
        else:
            print("La note de Reseaux doit etre un chiffre/nombre")

        response_etudiants = requests.post(url, json=insert_etudiants) # requests.post() pour faire une requêtes SQL INSERT INTO 
        respose_matieres = requests.post(url, json=insert_matieres) # requests.post() pour faire une requêtes SQL INSERT INTO 

        #Partie Vérifiactions / Debug si renvoie 404 alors erreur si renvoie 200 alors succes
        print(response_etudiants.status_code)
        print(response_etudiants.text)                       
        print(respose_matieres.status_code)
        print(respose_matieres.text)

        self.spinner.text=""
        self.identifiant.text=""
        self.annee.text=""
        self.nom.text=""
        self.prenom.text=""
        self.matiere1.text=""
        self.matiere2.text=""
        self.matiere3.text=""
        self.matiere4.text=""
        self.mdp.text=""


#Class permettant de choisir l'image et de l'envoyer à la db par la suite avec le même identifiant
class SecondWindow(Screen):
    
    identifiant=ObjectProperty(None)
    

    def selected(self, filename):

        #Récupere la valeur de l'identifiant rentré dans la fenetre d'inscription
        identifiant=Ratio.get_identifiant()

        #Récupère le chemin de l'image sur la quelle on clique 
        self.ids.my_image.source = filename[0]
        chemin = filename[0]
        print(filename[0])

        # Url de mon site php / API
        url = "https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php"

        #Ouvrir l'image est lire son contenu puis la transformer en base 64 pour par la suite l'envoyer à la bd 
        with open(chemin, "rb") as image_file:
            print (image_file)
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        #Définit la table utilisé dans ma bd
        data = {
            "table": "profile", 
            "id_etu": identifiant,
            "image": encoded_string
        }


        #On réalise une requete post pour insérer les données tout comme INSERT INTO 
        response = requests.post(url, json=data)

        #print qui sert de debug si 404 alors erreur si 200 alors succes
        print(response.status_code)
        print(response.text)



#Définit la class intéroger la bd qui est la fenêtre qui s'ouvre quand on clique sur le bouton se connecter dans la class connexion
class Interroger_la_bd(Screen):
    idetu=ObjectProperty(None)
    annee=ObjectProperty(None)
    nom=ObjectProperty(None)
    prenom=ObjectProperty(None)
    mdp=ObjectProperty(None)
    statut=ObjectProperty(None)
    image=ObjectProperty(None)

    #Récupère l'image depuis la bd pour l'afficher dans la fenetre
    def intero_photo(self):
        
        #Trille correspond à la valeur de l'identifiant rentré dans le champs connexion
        trille=Ratio.get_idetu()
        
        #Définit la table dans la qu'elle est contenu l'info 
        #Et dans la qu'elle on va cherche l'image correspondant à l'id sélectionne
        etudiant={'table':'profile','id':trille}
        #On fait une requete requests.get pour récupérer le contenu tout comme SELECT * FROM profile WHERE ID=valeur_de_trille
        response = requests.get('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant)

        #Print de debug
        # print(response)

        data = response.json()

        #print de debug
        # print(data)


        #Récupére le contenu du champs "image" dans notre table qui contient notre blob sous forme encode en base 64
        blob=data["image"]


        #Ducoup on cherche à décoder l'image avec les lignes suivantes dans la quelle on va lui re donne la texture d'une vraie image au format jpg
        self.image.source=""
        self.image.data= io.BytesIO(base64.b64decode(blob))
        self.image.coreimage=CoreImage(self.image.data, ext ="jpg")
        self.image.texture=self.image.coreimage.texture


    #méthod pemrettant de récupérer les infos de la table etudiants 
    def intero(self):
        
        #Trille est égale à la valeur de l'id rentré dans le champ connexion
        trille=Ratio.get_idetu()

        # self.idetu.text=Ratio.get_idetu()
        idetu=self.idetu.text
        annee=self.annee.text
        nom=self.nom.text
        prenom=self.prenom.text
        statut=self.statut.text
        
        #On définit la table ainsi que la facons d'ou on veux récupérer l'information
        #ici on va récupérer les infos de la table etudiants pour l'id rentré dans la page connexion
        etudiant={'table':'etudiants','id':trille}

        #On fait une requête get correspondant à uen requet SELECT * FROM etudiants WHERE id=valeur de l'id rentré dans le champs connexion
        response = requests.get('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant)
        data = response.json()

        #Print pour débug
        #print(data)

        #Assigne les valeurs en fonction du résultat de notre liste
        self.idetu.text=data["id"]
        self.nom.text=data["nom"]
        self.prenom.text=data["prenom"]
        self.annee.text=data["annee"]
        self.statut.text=data["statut"]

        #On appelle la methode intero_photo initialisé au dessus 
        self.intero_photo()

        


"""Je cherche à si l'identifiant de la page connexion ets bon alors afficher toutes les valeurs de l'identifiant x sinon rien afficher"""
"""afficher en focntion de l'id les infos de la tables """


#Class dasn la quelle est appelle la methode intero_mat
class FourWindow(Screen):

    matiere1=ObjectProperty(None)
    matiere2=ObjectProperty(None)
    matiere3=ObjectProperty(None)
    matiere4=ObjectProperty(None)
    average=ObjectProperty(None)

    #mathod dans la quelle on récupère les valeurs de table matieres pour les afficher par la suite
    def intero_mat(self):
        
        trille=Ratio.get_idetu()
        # self.idetu.text=Ratio.get_idetu()
        matiere1=self.matiere1.text
        matiere2=self.matiere2.text
        matiere3=self.matiere3.text
        matiere4=self.matiere4.text
        label=self.label.text
        
        #Définit la table matieres dans la quelle on va récupérer en fonction de la valeur de l'id entrer dans la page connexion
        etudiant={'table':'matieres','id':trille}
        #Requête requests.get dans la qu'elle on va récupérer les infos de la table matieres en fonction de l'identifiant rentrer
        #cela correspond a une requte SELECT * FROM matieres WHERE id=valeur de l i dnetifiant rentrer dnas la fenetre connexion en SQL de base
        response = requests.get('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant)
        data = response.json()
        #Print pour débug
        #print(data)

        #Attribue les valeurs en fonction de la liste récupérer
        self.matiere1.text=data["matiere1"]
        self.matiere2.text=data["matiere2"]
        self.matiere3.text=data["matiere3"]
        self.matiere4.text=data["matiere4"]
        
        #Calcul de la moyenne générale en focntion des valeurs rentrer dans la bd 
        average= (int(self.matiere1.text) + int(self.matiere2.text) + int(self.matiere3.text)+ int(self.matiere4.text)) / 4
        #Afficher cette moyenne générale dans un label
        self.label.text = str(average)


        
    """Partie qui ne fonctionen pas mais qui devrait fonctionner / Dans la quelle on definit un bouton sur le quelle quand il est appuyer permet à 
       l'utilisateur de se désinscrire et de supprimer l'user de la bd avec une request requests.delete qui correspond à une requête DELETE FROM ...
    """
    
    # def remove_bd(self):

    #     trille=Ratio.get_idetu()

    #     etudiant={'table':'matieres','id':trille}
    #     response = requests.delete('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant)
    #     # data1=response.json()
    #     print(response.text)


    #     etudiant1={'table':'etudiants','id':trille}
    #     response1 = requests.delete('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant1)
    #     data1=response1.json()

    #     etudiant2={'table':'profile','id':trille}
    #     response2= requests.delete('https://thomas-cecchini-etu.pedaweb.univ-amu.fr/extranet/base.php',params=etudiant2)
    #     data2=response2.json()
        



#Relis le fichier kv et python/kivy
kv = Builder.load_file("My.kv")

class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()

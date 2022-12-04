from django.db import models
import string,random


class UrlManager(models.Manager):
    """
    Modèle du Manager des SimplifiedUrl, afin de les manipuler correctement avec Django sans passer par le constructeur
    """
    def create_url(self, url_to_redirect, redirection_shortcut=None):
        if redirection_shortcut is None:
            # Boucle permettant d'obtenir un raccourci qui n'existe pas encore dans la BDD
            while True:
                # Génération aléatoire de 10 caractères avec des chiffres et lettres minuscules et majuscules
                letters_and_digits = string.ascii_letters + string.digits
                redirection_shortcut = ''.join(random.choice(letters_and_digits) for _ in range(10))
                if SimplifiedUrl.objects.filter(redirection_shortcut=redirection_shortcut).exists():
                    continue
                else:
                    break
        url_object = self.create(url_to_redirect=url_to_redirect, redirection_shortcut=redirection_shortcut)
        return url_object

class SimplifiedUrl(models.Model):
    """
    Modèle des urls simplifiés
    """
    redirection_shortcut = models.CharField(max_length=10, unique=True)
    url_to_redirect = models.URLField(max_length=200)
    objects = UrlManager()

    def __str__(self):
        return 'Url simplifié du site ' + str(self.url_to_redirect) + ' avec le raccourci ' + str(self.redirection_shortcut)

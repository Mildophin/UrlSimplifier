from django.db import models
import string,random

class SimplifiedUrl(models.Model):
    """
    Modèle des urls simplifiés
    """
    redirection_shortcut = models.CharField(max_length=10, unique=True)
    url_to_redirect = models.URLField(max_length=200)

    def __init__(self, url_to_redirect, redirection_shortcut=None):
        # Constructeur qui créé une URL simplifiée avec la possibilité de spécifier le raccourci voulu
        super().__init__(url_to_redirect, redirection_shortcut=None)
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
        self.url_to_redirect=url_to_redirect
        self.redirection_shortcut=redirection_shortcut

    def __str__(self):
        return 'Url simplifié du site ' + str(self.url_to_redirect) + ' avec le raccourci ' + str(self.redirection_shortcut)

from django.db import models
import string,random

class SimplifiedUrl(models.Model):
    """
    Modèle des urls simplifiés
    """
    redirection_path = models.CharField(max_length=10,unique=True)
    url_to_redirect = models.URLField(max_length=200)

    @classmethod
    def create(cls, url_to_redirect, redirection_path=None):
        # Créé une URL simplifiée avec la possibilité de spécifier le raccourci voulu
        if redirection_path is None:
            # Boucle permettant d'obtenir un raccourci qui n'existe pas encore dans la BDD
            while True:
                # Génération aléatoire de 10 caractères avec des chiffres et lettres minuscules et majuscules
                letters_and_digits = string.ascii_letters + string.digits
                redirection_path = ''.join(random.choice(letters_and_digits) for _ in range(10))
                if SimplifiedUrl.objects.filter(redirection_path=redirection_path).exists():
                    continue
                else:
                    break
        simplified_url_object = cls(url_to_redirect=url_to_redirect, redirection_path=redirection_path)
        return simplified_url_object

    def __str__(self):
        return 'Url simplifié du site ' + str(self.url_to_redirect) + ' avec le raccourci ' + self.redirection_path
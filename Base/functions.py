import string
import random
from Base.models import SimplifiedUrl


def clean_url_maker(given_url):
    # Création d'une url aléatoire de 10 caractères avec des chiffres et lettres minuscules et majuscules
    letters_and_digits = string.ascii_letters + string.digits
    simplified_url = ''.join(random.choice(letters_and_digits) for _ in range(10))
    # Vérifie que la redirection n'existe pas
    if SimplifiedUrl.objects.filter(redirection_path=simplified_url).exists():
        clean_url_maker(given_url)
    else:
        url_object = SimplifiedUrl(redirection_path=simplified_url, url_to_redirect=given_url)
        url_object.save()
        return url_object

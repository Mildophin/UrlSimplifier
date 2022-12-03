from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from Base.models import SimplifiedUrl


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        # Recupère la variable given_url dans le template main.html
        given_url = request.POST.get('given_url')
        url_validator = URLValidator()
        # Verification si la variable est une url valide
        try:
            url_validator(given_url)
        except ValidationError:
            return render(request, 'main.html', context={"is_given_url_right": False})
        # Appel de la fonction qui créé une url aléatoire et qui n'existe pas encore
        simplified_url_object = SimplifiedUrl.create(url_to_redirect=given_url)
        simplified_url = simplified_url_object.redirection_path
        return render(request, 'main.html', context={"simplified_url": simplified_url})

    else:
        return HttpResponse("C'est interdit mon ami", status=403)


def url_shorten(request, redirection_path):
    url = get_object_or_404(SimplifiedUrl, redirection_path=redirection_path)
    return redirect(url.url_to_redirect)
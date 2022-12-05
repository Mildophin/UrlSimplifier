from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from Base.models import SimplifiedUrl


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        # Récupère la variable given_url dans le template main.html
        given_url = request.POST.get('given_url')
        url_validator = URLValidator()
        # Verification si la variable est une url valide
        try:
            url_validator(given_url)
        except ValidationError:
            return render(request, 'main.html', context={"is_given_url_right": False})
        # Création d'une instance dans le cas ou l'url est valide en passant par le Manager
        simplified_url_object = SimplifiedUrl.objects.create_url(url_to_redirect=given_url)
        return render(request, 'main.html', context={"simplified_shortcut": simplified_url_object.redirection_shortcut})
    else:
        return HttpResponse("C'est interdit mon ami", status=403)


def url_shorten(request, redirection_shortcut):
    url_object = get_object_or_404(SimplifiedUrl, redirection_shortcut=redirection_shortcut)
    return redirect(url_object.url_to_redirect)

def administration(request, redirection_shortcut=None):
    if request.method == 'GET':
        url_queryset = SimplifiedUrl.objects.all()
        if redirection_shortcut is not None:
            url_object_to_delete = get_object_or_404(SimplifiedUrl, redirection_shortcut=redirection_shortcut)
            url_object_to_delete.delete()
            return redirect('administration')
        else:
            return render(request, "administration.html", context={"url_queryset": url_queryset})
    else:
        return HttpResponse("C'est interdit mon ami", status=403)
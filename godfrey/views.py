from django.shortcuts import render
from .models import Names
# Create your views here.

def index(request):
    # Return home.html
    return render(request, "godfrey/index.html")

def return_name(request, number_of_names, quantity):
    """
    number_of_names: How many names should make up the randomly generated name
    quantity: How many randomly generated names do you want
    returns: A list of randomly generated names
    """
    names = []
    for i in range(quantity):
        generated_name = ""
        for n in range(number_of_names):
            # Get random number between 0 - Max number of entries in table, use that to get random name
            name = Names.objects.order_by("?").first()
            generated_name += name
        names.append(generated_name)

    return render(request, 'godfrey/index.html', {"names": names})
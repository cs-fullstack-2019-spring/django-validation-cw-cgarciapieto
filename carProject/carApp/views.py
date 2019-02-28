from django.shortcuts import render
from .forms import CarForm
from .models import CarModel
from django.shortcuts import HttpResponse



# function that takes a validated POST that saves  to the database and also renders in Browser
def index(request):
    if (request.method == 'POST'):
        form = CarForm(request.POST)

        if (form.is_valid()):
            CarModel.objects.create(make=request.POST['make'], model=request.POST['model'], year=request.POST['year'],
                                    mpg=request.POST['mpg'])
        else:
            allEntries = CarModel.objects.all()
            context = {
                'errors': form.errors,
                'allEntries': allEntries,
                'form': CarForm,
            }
            return render(request, 'carApp/index.html', context)

    allEntries = CarModel.objects.all()
    form = CarForm()
    context = {
        "allEntries": allEntries,
        "form": form,
    }
    return render(request, "carApp/index.html", context)

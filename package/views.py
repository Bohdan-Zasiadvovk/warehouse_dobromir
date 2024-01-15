from django.shortcuts import render, redirect, get_object_or_404
from .forms import PackageForm
from .models import Package


def package(request):
    return render(request, 'package/package.html')

def create_package(request):
    if request.method == 'GET':
        return render(request, 'package/createpackage.html', {'form': PackageForm()})
    else:
        try:
            form = PackageForm(request.POST)
            new_package = form.save(commit=False)
            new_package.save()
            return redirect('all_packages')
        except ValueError:
            return render(request, 'package/createpackage.html', {'form': PackageForm(), 'error': 'Bad data passed in. Try again'})

def get_all_packages(request):
    if request.method == "GET":
        packages = Package.objects.all()
        return render(request, 'package/allpackages.html', {'packages': packages})

def update_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == "POST":
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('all_packages')
    else:
        form = PackageForm(instance=package)

    return render(request, 'package/updatepackage.html', {'form': form, 'package': package})

def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)

    if request.method == 'POST':
        package.delete()
        return redirect('all_packages')

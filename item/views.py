from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


def item(request):
    return render(request, 'item/item.html')


def create_item(request):
    if request.method == 'GET':
        return render(request, 'item/createitem.html', {'form': ItemForm()})
    else:
        try:
            form = ItemForm(request.POST)
            new_item = form.save(commit=False)
            new_item.save()
            return redirect('all_items')
        except ValueError:
            return render(request, 'item/createitem.html', {'form': ItemForm(), 'error': 'Bad data passed in. Try again'})


def get_all_items(request):
    if request.method == "GET":
        items = Item.objects.all()
        return render(request, 'item/allitems.html', {'items': items})


def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "GET":
        return render(request, 'item/updateitem.html', {'item': item, 'form': ItemForm(instance=item)})
    else:
        try:
            form = ItemForm(request.POST, instance=item)
            form.save()
            return redirect('all_items')

        except ValueError:
            return render(request, 'item/updateitem.html', {'item': item, 'form': ItemForm(instance=item)})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('all_items')


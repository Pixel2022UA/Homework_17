from django.shortcuts import render, HttpResponse, redirect
from .forms import PictureForm
from .models import Picture


def upload_pic(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pic-list")
    else:
        form = PictureForm()
    context = {"form": form}
    return render(request, "upload_pic.html", context)


def pic_list(request):
    pictures = Picture.objects.all()
    context = {'pictures': pictures}
    return render(request, 'pic_list.html', context)

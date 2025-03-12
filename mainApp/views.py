from re import search

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request

from mainApp.models import Talaba


def Talabalar_view(request, ism=None):
    if request.method == "Post":
        Talaba.object.create(
            ism-request.Post.get("ism"),
            guruh=request.Post.get("guruh"),
            kurs=request.Post.get("kurs"),
            kitob_soni=request.Post.get('kitob_soni')
        )
        return redirect('talabalar')
    talabalar = Talaba.object.all()

    search=request.GET.get('search')
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)

    context = {
        "talabalar": talabalar,
        'search': search,
    }
    return render(request, 'talabalar.html',context)
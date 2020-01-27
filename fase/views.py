from email.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import Mixer
from .models import Ty_pe
from .forms import ModelMixer
from .forms import SendMailUser
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings


def template(request):
    Contact_form = SendMailUser
    if request.method == 'POST':
        form = Contact_form(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_description = request.POST.get('contact_description')
            template = get_template('santex/contact_forms.txt')
            context = {
                'contact_name' : request.POST.get('contact_name'),
                'contact_email' : request.POST.get('contact_email'),
                'contact_description' : request.POST.get('contact_description'),
                        }


            email = EmailMessage(' New massage from email')


    return render(request, 'The_main_page.html')


def delivery(request):
    return render(request, 'delivery.html')


def buy(request):
    form = ModelMixer(request.POST)
    context = {
        'form': form
    }
    return render(request, 'buy.html', context)


def firstPage(request):
    new = Mixer.objects.all()
    context = {
        'items': Ty_pe.objects.all(),
        'new': new,
        'item2': Mixer.objects.all()
    }
    return render(request, 'firstPage.html', context)


def mixer(request):
    bathtubs = Mixer.objects.filter(typ_e__ty_pe='для ванны')

    context = {
        'bathtubs': bathtubs,
    }
    return render(request, 'mixer/bathtubs.html', context)


def shower(request):
    shower = Mixer.objects.filter(typ_e__ty_pe='для душа')

    context = {
        'shower': shower,
    }
    return render(request, 'mixer/shower.html', context)


def bidet(request):
    bidet = Mixer.objects.filter(typ_e__ty_pe='для биде')

    context = {
        'bidet': bidet,
    }
    return render(request, 'mixer/bidet.html', context)


def sink(request):
    sink = Mixer.objects.filter(typ_e__ty_pe='для раковины')

    context = {
        'sink': sink,
    }
    return render(request, 'mixer/sink.html', context)


def aboutTheStore(request):
    return render(request, 'About_the_store.html')


def plumbing_installation(request):
    return render(request, 'plumbing_installation.html')


def contact(request):
    return render(request, 'contact.html')


def about_mixer(request, mix_id):
    mix_get = Mixer.objects.get(id=mix_id)
    context = {
        'mix_get':mix_get,
    }
    return render(request,'mixer/about_mixer.html', context)
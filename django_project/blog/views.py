from django.shortcuts import render
from .models import FypaperPdf
from .models import FybookPdf
from .models import SypaperPdf
from .models import SybookPdf
from .models import TypaperPdf
from .models import TybookPdf


def home(request):
    return render(request, 'blog/home.html')

def sy(request):
    return render(request, 'blog/sy.html', {'title': 'sy'})

def base(request):
    return render(request,'blog/base.html',{'title': 'Base'})

def studymaterial(request):
    return render(request,'blog/studymaterial.html',{'title': 'studymaterial'})

def fy(request):
    return render(request,'blog/fy.html',{'title': 'fy'})

def ty(request):
    return render(request,'blog/ty.html',{'title': 'ty'})


def fypaper(request):
    pdf=FypaperPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/fypaper.html',{"pdf":pdf})

def fybook(request):
    pdf=FybookPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/fybook.html',{"pdf":pdf})


def sypaper(request):
    pdf=SypaperPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/sypaper.html',{"pdf":pdf})

def sybook(request):
    pdf=SybookPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/sybook.html',{"pdf":pdf})

def typaper(request):
    pdf=TypaperPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/typaper.html',{"pdf":pdf})

def tybook(request):
    pdf=TybookPdf.objects.all()
    # caption=pdf.objects.all()

    return render(request, 'blog/tybook.html',{"pdf":pdf})

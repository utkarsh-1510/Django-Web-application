from django.shortcuts import render , HttpResponse,redirect
from .forms import Myfilescryptoform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import file_upload
# Create your views here.
def crypto(request):
    if request.method == 'POST':
        form = Myfilescryptoform(request.POST, request.FILES)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            file_upload(file_name=name, my_file=the_files).save()
            messages.success(request,'Uploaded')
            return redirect('blog-home')
        else:
            form = Myfilescryptoform()
            return render(request, 'crypto/cryptography.html', {'form': form})

    context = {
        'form':Myfilescryptoform()
    }
    return render(request, 'crypto/cryptography.html',context)
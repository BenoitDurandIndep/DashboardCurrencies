from django.shortcuts import render,HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,"currencies/index.html", context={"test":5})
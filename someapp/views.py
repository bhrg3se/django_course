from django.shortcuts import render,HttpResponse

# Create your views here.
def show_hello(request):
    return render(request,'someapp/profile.html')

def my_cv(request):
    name=request.GET.get("name")
    data={
        "name":name,
        "skills":["python","java","js","golang"]
    }
    return render(request,'someapp/mycv.html',data)


def add(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    return HttpResponse(int(a)+int(b))

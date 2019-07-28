from django.shortcuts import render,HttpResponse
from someapp import models
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


def comments(req):
    if(req.method=="POST"):
        has_commeted=req.session.get("has_commented")
        if(not has_commeted):
            req.session["has_commented"]=True
            user=req.POST.get("user")
            comment=req.POST.get("content")
            c=models.Comment(user=user,content=comment)
            c.save()
            return HttpResponse("comment submitted")
        else:
            return HttpResponse("You have already commented")
    elif (req.method=="GET"):
        comments=models.Comment.objects.all()
        d={
            "comments":comments
        }
        return render(req,'someapp/comments.html',d)


def test_session(req):
    c=req.session.get("count")
    if(c==None):
        req.session["count"]=1
    else:
        c=c+1
        req.session["count"] = c
    return HttpResponse("You have visited this page "+str(c)+" times")


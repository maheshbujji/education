from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView,RedirectView
from app1.functions import handle_uploaded_file
from app1.forms import studentForms
from django.http import  HttpResponse,HttpResponseRedirect



from .models import Student, Faculty, Attedence


def showindex(request):
    return render(request,"index.html")


def display(request):
    name=request.POST.get("username")
    upass=request.POST.get("pass")
    if name == 'mahesh' and upass == '123456':
        return render(request,"register.html")
    else:
        return render(request,"index.html",{'msg':'invalide password and username'})

def save(request):
    fname=request.POST.get("t1")
    lname=request.POST.get("t2")
    email=request.POST.get("t3")
    phone=request.POST.get("t4")
    clas=request.POST.get('t5')
    uname=request.POST.get("t6")
    upass=request.POST.get("t7")
    gender=request.POST.get("work")
    g=Student(fname=fname,lname=lname,email=email,cno=phone,uname=uname,upass=upass,gender=gender,clas=clas)
    g.save()
    return render(request,"register.html",{"m1":'details saved'})
class viewlist(ListView):
    model = Student

class Maheshupdate(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('name')
class maheshdelete(DeleteView):
    model = Student
    success_url = reverse_lazy('name')

def register(request):
    return render(request,"register.html")


def registerfaculty(request):
    return render(request,"facultylogin.html")

def Facuityregister(request):
    fname = request.POST.get("t1")
    lname = request.POST.get("t2")
    email = request.POST.get("t3")
    phone = request.POST.get("t4")
    subject=request.POST.get('t5')
    clas = request.POST.get('t6')
    uname = request.POST.get("t7")
    upass = request.POST.get("t8")
    gender = request.POST.get("work")
    g = Faculty(fname=fname, lname=lname, email=email, cno=phone, uname=uname, upass=upass, gender=gender, clas=clas,subject=subject)
    g.save()
    return render(request,"facultregistion.html")
class Facultysave(ListView):
    model = Faculty


def Books(request):
    if request.method=="POST":
        student=studentForms(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            from  .models import BookInfo
            bname=request.POST.get('Bookname')
            bnumber=request.POST.get('BookNo')
            bfile=request.FILES['file']
            booksave=BookInfo(Bookname=bname,BookNo=bnumber,file=bfile)
            booksave.save()
            booklist=BookInfo.objects.all()
            return render(request, "Library.html", {"form": student,"mesg":"inserted successfully","booklist":booklist})

    else:
        student=studentForms()
        return render(request,"Library.html",{"form":student,"mesg":"insert failed"})


def search(request):
    name=request.POST.get("h1")
    hh=Student.objects.get(fname=name)
    if hh:
        return  render(request,"app1/student_list.html",{"cc":hh})
    else:
        return render(request,"app1/student_list.html",{"ma":"Not matched"})


def Openlibrary(request):
    from .forms import studentForms
    ss=studentForms()
    from .models import BookInfo
    booklist = BookInfo.objects.all()
    return render(request,"Library.html",{"form":ss,"booklist":booklist})


def Suggestions(request):
    return render(request,"suggestions.html")


def studentlogin(request):
    return render(request,"sudentlogin.html")


def loginstudent(request):
    name=request.POST.get("studentname")
    password=request.POST.get("studentpassword")
    try:
        gg = Student.objects.get(uname=name,upass=password)
        if gg:
            return render(request,"register.html")
        #else:
            #return render(request,"sudentlogin.html",{"masg":"not match"})
    except:
        return render(request,"sudentlogin.html",{"masg":"Invalid details"})


def facultylogin(request):
    email=request.POST.get("email")
    upass=int(request.POST.get("pass"))
    ll=Faculty.objects.get(email=email,upass=upass)
    if ll:
        return render(request,"facultregistion.html")
    else:
        return render(request,"facultylogin.html",{"msg":"invalide password and username"})


def reports(request):
    return render(request,"stdentattencesheet.html")


def AttedenceSave(request):
    name=request.POST.get("name")
    jan=request.POST.get("s1")
    feb=request.POST.get("s2")
    mar=request.POST.get("s3")
    apr=request.POST.get("s4")
    may=request.POST.get("s5")
    jun=request.POST.get("s6")
    july=request.POST.get("s7")
    aug=request.POST.get("s8")
    sep=request.POST.get("s9")
    oct=request.POST.get("s10")
    nov=request.POST.get("s11")
    dec=request.POST.get("s12")
    SAA=Attedence(name=name,jan=jan,feb=feb,mar=mar,may=may,june=jun,july=july,aug=aug,sep=sep,oct=oct,nov=nov,dec=dec)
    SAA.save()
    return render(request,"stdentattencesheet.html",{"mas":"save"})

from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Book
from django import forms


class BookForm(forms.Form):
    name=forms.CharField()
    author=forms.CharField()
    language=forms.CharField()
    price=forms.IntegerField()
    genre=forms.CharField()
    yearofpublication=forms.IntegerField()

class BookListView(View):

    def get(self,request,*args,**kwargs):
        qs=Book.objects.all()
        return render (request,"book_list.html",{"data":qs})

class BookDetailView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})

class BookDeleteView(View):

     def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id).delete()
        return redirect("book-list")
     
class BookCreateView(View):
    
    def get(self,request,*args,**kwargs):
        form=BookForm()
        return render (request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Book.objects.create(**data)
            return redirect("book-list")
        else:
            return render(request,"book_add.html",{"form":form})

        # data={k:v for k,v in request.post.items()}
        # data.pop("csrfmiddlewaretoken")
        # Book.objects.create(**data)
        # return redirect("book-list")


class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book_object=Book.objects.get(id=id)
        data={
            "name":book_object.name,
            "author":book_object.author,
            "language":book_object.language,
            "price":book_object.price,
            "genre":book_object.genre,
            "yearofpublication":book_object.yearofpublication    
        }

        form=BookForm(initial=data)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Book.objects.filter(id=id).update(**data)
            return redirect("book-list")
        else:
            return render(request,"book_edit.html",{"form":form})

    



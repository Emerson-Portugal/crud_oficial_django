from django.shortcuts import render, redirect
from django.contrib import messages
from .models import blog_crud

# Create your views here.

template_name = "blog/index.html"

def lista_blog_crud(request):
    objetos = blog_crud.objects.all()
    return render(request, template_name, {'objetos': objetos})



def registrar_blog(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = blog_crud.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'BLOG registrado!')
    return redirect('/blog')



def eliminar_blog(request, codigo):

    curso = blog_crud.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, 'BLOG elimnado!')
    return redirect('/blog')





def edicionBlog(request, codigo):
    objeto = blog_crud.objects.get(codigo=codigo)
    return render(request, "blog/edition.html", {'objeto': objeto})


def editar_blog(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = blog_crud.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()


    messages.success(request, 'BLOG editado!')
    return redirect('/blog')

from django.urls import path
from .views import(
    lista_blog_crud,
    registrar_blog,
    eliminar_blog,
    edicionBlog,
    editar_blog
)

app_name = 'blog'

urlpatterns = [
    path('', lista_blog_crud, name='home'),
    path('registrar/', registrar_blog, name='registrar'),
    path('eliminar/<codigo>', eliminar_blog, name='eliminar'),
    path('edicion/<codigo>', edicionBlog, name='edicion'),
    path('editar/', editar_blog, name='editar'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('empresa/<int:empresa_id>/cadastrar-funcionario/', views.funcionarios, name='funcionarios'),
    path('empresa/<int:empresa_id>/', views.pagina_empresa, name='pagina_empresa'),
    path('empresa/<int:empresa_id>/registrar-batida/', views.registrar_ponto, name='registrar_batida'),
    path('empresa/<int:empresa_id>/registro-batidas/', views.registro_batidas, name='registro_batidas'),

]

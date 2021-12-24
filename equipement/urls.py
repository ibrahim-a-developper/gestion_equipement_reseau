from django.urls import path
from . import views
from .views import EquipementDeleteView

app_name='equipement'

urlpatterns = [
    path('',views.home,name='home'),
    path('table/',views.table_equipement,name='table_equipement'),

    #equipement
    path('add_equipement/' ,views.EquipementCreate,  name='add_equipement'),
    path('detail_equipement/<int:equipement_id>/', views.EquipementDetail, name='detail_equipement'),
    path('update_equipement/<int:equipement_id>/update', views.EquipementUpdate, name='update_equipement'),
    # path('update_equipement/slug:pk>/update', views.PostUpdateView.as_view(), name='update_equipement'),
    path('detail_equipement/<int:equipement_id>/delete/', views.EquipementDeleteView, name='delete_equipement'),
    # path('detail_equipement/<slug:pk>/delete/', EquipementDeleteView.as_view(), name='delete_equipement'),
    # fin equipement

    #categorie
    path('category_table/', views.category_table, name='category_table'),
    path('add_categorie/', views.CategorietCreate, name='add_categorie'),
    path('update_categorie/<int:categorie_id>/update', views.CategoryUpdate, name='update_categorie'),

    #direction
    path('add_direction/', views.DirectionCreate, name='add_direction'),
    path('update_direction/<int:direction_id>/update', views.DirectionUpdate, name='update_direction'),

    path('table_user', views.tableuser, name='table_user'),

]
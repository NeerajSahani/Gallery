from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('image/<slug:slug>/', views.ImageView.as_view(), name='view-image'),
    path('add-tag/', views.TagFormView.as_view(), name='add-tag'),
    path('add-image/', views.ImageFormView.as_view(), name='add-image'),
    path('rotate-image/<slug:slug>/<int:angle>/', views.rotate, name='rotate-image'),
    path('filter', views.search, name='search'),
    path('tag-create-popup/', views.tag_create_popup, name='add-tag-popup')
]

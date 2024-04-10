from django.urls import path
from . import views

app_name = 'photographs'

urlpatterns = [
    # PhotographUserContributions
    path('usercontribution-create/', views.PhotographUserContributionCreateView.as_view(), name='usercontribution-create'),
    path('usercontribution-create-success/', views.PhotographUserContributionCreateSuccessTemplateView.as_view(), name='usercontribution-create-success'),
    # Photographs
    path('', views.PhotographListView.as_view(), name='list'),
    path('<pk>/', views.PhotographDetailView.as_view(), name='detail'),
]

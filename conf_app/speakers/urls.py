from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_speakers, name='home'),
    path('create/', views.create_speaker, name='add'),
    path('update/<int:speaker_id>', views.update_speaker, name='update'),
    path('delete/<int:speaker_id>', views.delete_speaker, name='delete')
]

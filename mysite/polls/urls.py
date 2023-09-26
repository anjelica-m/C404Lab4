from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('api/question/<int:pk>', views.update_question, name='update_question'),
    path('api/questions/', views.get_questions, name='get_questions'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
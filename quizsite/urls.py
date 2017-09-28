from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
	path("", views.startpage, name="start_page"),
	path("quiz/<int:quiz_number>/", views.quiz, name="quiz_page"),
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
	path("quiz/<int:quiz_number>/completed/", views.completed, name="completed_page"),
	path("admin/", admin.site.urls),
	path("quiz/<int:quiz_number>/question/<int:question_number>/answer/", views.answer, name="answer_page"),
	]

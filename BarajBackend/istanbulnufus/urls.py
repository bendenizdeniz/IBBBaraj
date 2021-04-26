from django.urls import path


from .views import istanbulNufusList, istanbulNufusDetail


urlpatterns = [
    path('<int:pk>', istanbulNufusDetail.as_view()),
    path('', istanbulNufusList.as_view())

]

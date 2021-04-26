from django.urls import path


from .views import kisiBasiCekilenSuList,kisiBasiCekilenSuDetail


urlpatterns = [
    path('<int:pk>/', kisiBasiCekilenSuDetail.as_view()),
    path('', kisiBasiCekilenSuList.as_view())

]

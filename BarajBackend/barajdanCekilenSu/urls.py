from django.urls import path


from .views import damVolumeList,damVolumeDetail


urlpatterns = [
    path('<int:pk>/', damVolumeDetail.as_view()),
    path('', damVolumeList.as_view())

]

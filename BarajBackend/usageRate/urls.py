from django.urls import path


from .views import usageRateList,usageRateDetail


urlpatterns = [
    path('<int:pk>/', usageRateDetail.as_view()),
    path('', usageRateList.as_view())

]

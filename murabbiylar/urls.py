from django.urls import path
from .views import AllTrenerView, TrenerView
urlpatterns=[
    path('all', AllTrenerView.as_view()),
    path('trener/<int:pk>', TrenerView.as_view())
]
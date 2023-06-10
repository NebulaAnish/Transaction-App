from .views import CustomListView, CustomCreateView, CustomDetailView, CustomUpdateView
from .views import CustomDeleteView, CustomLoginView, CustomLogoutView, CustomRegisterView
from .views import ProfileEditView
from django.urls import path

urlpatterns = [
    # path("register/", CustomRegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("logout/", CustomLogoutView.as_view(), name='logout'),
    path('', CustomListView.as_view(), name='listview'),
    path("create/", CustomCreateView.as_view(), name='createview'),
    path("transaction/<int:pk>/", CustomDetailView.as_view(), name='detailview'),
    path('transaction/<int:pk>/update/',
         CustomUpdateView.as_view(), name='updateview'),
    path('transaction/<int:pk>/delete/',
         CustomDeleteView.as_view(), name='deleteview'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profileedit/<int:pk>/', ProfileEditView.as_view(), name='profileEdit'),
]

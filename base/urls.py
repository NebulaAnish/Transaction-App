from .views import CustomListView, CustomCreateView, CustomDetailView, CustomUpdateView
from .views import CustomDeleteView, CustomLoginView, CustomLogoutView, CustomRegisterView
from .views import ProfileEditView, ForbiddenView
from .views import profile
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

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
    path('fobidden/', ForbiddenView.as_view(), name='forbidden'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

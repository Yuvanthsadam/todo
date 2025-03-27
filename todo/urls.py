from django.urls import path
from .views import TodoListCreateView, TodoDetailView,RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[
    
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    
    path('todos/',TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>',TodoDetailView.as_view(), name='todo-detail'),
]
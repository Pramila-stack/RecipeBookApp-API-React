from django.shortcuts import render


# Create your views here.
from django.contrib.auth.models import Group, User
import django_filters
from rest_framework import permissions, viewsets, filters

from api.models import Recipe
from api.serializers import GroupSerializer, RecipeSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecipePagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 50



class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Recipe.objects.all().order_by("-created_at")
    serializer_class = RecipeSerializer
    pagination_class = RecipePagination
    permission_classes = [permissions.AllowAny]

    filter_backends = [
    django_filters.rest_framework.DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]

    # Search fields
    search_fields = ["name", "category", "ingredients"]

     # Ordering fields
    ordering_fields = ["created_at", "name"]

    # Default ordering
    ordering = ["-created_at"]

    filterset_fields = ["category"]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    
    



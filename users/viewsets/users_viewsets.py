from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers.serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
#Create a new user and get token
    @action(detail=False, methods=['post'], url_path='register', permission_classes=[])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data) #takes incoming data and binds to the serializer
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Get token using credentials
    @action(detail=False, methods=['post'], url_path='login', permission_classes=[])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='profile')
    def profile(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class CustomAuthToken(ObtainAuthToken): #this is for token log in view , return user + token
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'role': user.role  # assuming you have a `role` field
        })

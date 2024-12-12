from rest_framework import generics
from apps.users.serializers import RegisterSerializer
from apps.users.models import User

from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer


class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'slug'



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def logout_view(request):
        logout(request)                                            # Колдонуучуну системадан чыгарып салуу
        return redirect('home')                                                    # Негизги бетке жөнөтүү
                                                
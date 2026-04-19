import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Verificacion

@api_view(['POST'])
def registrar_usuario(request):
    print("Datos recibidos:", request.data)
    data = request.data
    try:
        # 1. Crear el usuario en Django
        nuevo_user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        
        # 2. Generar código aleatorio
        codigo_random = str(random.randint(100000, 999999))
        
        # 3. Guardar código en la DB
        Verificacion.objects.create(user=nuevo_user, codigo=codigo_random)
        
        # 4. ENVIAR CORREO (Al correo que puso el usuario en el front)
        asunto = 'Bienvenido a Riot Games - Verifica tu cuenta'
        mensaje = f'Hola {nuevo_user.username}, tu código de verificación es: {codigo_random}'
        
        send_mail(asunto, mensaje, 'tu-correo@gmail.com', [nuevo_user.email])
        
        return Response({'status': 'ok', 'message': 'Usuario creado. Código enviado.'})
    
    except Exception as e:
        print("Error en el registro:", str(e))
        return Response({'status': 'error', 'message': str(e)}, status=400)
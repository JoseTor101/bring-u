from functools import wraps
from django.shortcuts import redirect
from accounts.models import UserProfile  # Import the User Profile model

#PARA QUE EL USUARIO SOLOP PUEDA VER LAS ENTREGAS DISPONIBLES SI ESTÁ ACTIVADA LA OPCIÓN

def is_service_prov_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(username=user)

            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return redirect('accounts/login')  # Redirect to the login page if the user is not authenticated
            
            # Check if the user has is_service_prov set to True
            if not user_profile.is_service_prov:
                return redirect('/profile')
            
            return view_func(request, *args, **kwargs)
        except:
            return redirect('/')
    
    return _wrapped_view

from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return redirect('inicio')
            
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Iniciar sesión'
        return context
    
def logout_request(request):
    logout(request)
    # messages.success(request, 'Se cerro la sesión de manera correcta...')
    return redirect('inicio')
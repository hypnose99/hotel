from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from userauths.models import User, Profile

from userauths.forms import UserRegisterForm
# Create your views here.


def RegisterView(request):
    # Vérifie si l'utilisateur est connecté et exécute une redirection
    if request.user.is_authenticated:
        messages.warning(request, f"Vous êtes déjà connecté ")
        return redirect("hotel:index")
    
    # Initialise l'intense "UserRegisterForm" de userauths.forms 
    # Vérifie et sauvegarde les données puis néttoie 
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        # Authentifie l'utilisateur et le connecte avec un message de succès
        user = authenticate(email=email, password=password)
        login(request, user)
        messages.success(request, f"Hey {full_name}, Votre compte a été créé avec succès")

        #Initialise l'intense et affecte les données de l'utilisateur au champs de la table profil
        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()
        return redirect("hotel:index")

    context = {
        "form": form
    }
    return render(request, "userauths/sign-up.html", context)


def loginView(request):
    # Vérifie si l'utilisateur est connecté et exécute une redirection
    if request.user.is_authenticated:
        messages.warning(request, "Vous êtes déjà connecté")
        return redirect("hotel:index")
    
    # Récupère les données qui sont rentré par l'utilisateur 
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            # Récupère l'intense dans user avec l'email rentrer par l'utilisateur et l'authentifie 
            user_query = User.objects.get(email= email)
            user_auth = authenticate(request, email=email, password=password)
             
             # Vérifie si l'information existe dans la base et connecte l'utilisateur
            if user_query is not None:
                login(request, user_auth)
                messages.success(request, "Vous êtes connecté ")
                next_url = request.GET.get("next", "hotel:index")
                return redirect(next_url)
            else:
                messages.error(request, "email ou mot de passe est incorrecte")
                return redirect("userauths:sign-in")
        except:
            messages.error(request, "L'utilisateur n'existe pas")
            return redirect("userauths:sign-in")
    
    return render(request, "userauths/sign-in.html")

def LogoutView(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté")
    return redirect("userauths:sign-in")
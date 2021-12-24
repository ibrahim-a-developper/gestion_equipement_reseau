
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from mathfilters.templatetags.mathfilters import sub

from accounts.decorators import allowed_users
from accounts.models import Profile
from installation.models import Direction, Installation
from .filter import EquipementFilter
from .models import Equipement, Category
from django.contrib.auth.decorators import login_required
from .forms import EquipementForm, CategorieForm, DirectionForm, EquipInstall, AtributForm, EquipementFormm


# Create your views here.
# def cal(n1,n2):
#     z=5|sub:7
#     return z
#index.html page principale
@login_required(login_url='accounts/login')
def home(request):
    list_quip=Equipement.objects.all()
    list_installation = Installation.objects.all()
    list_direction = Direction.objects.all()
    list_dir = Direction.objects.all()
    list_category = Category.objects.all()
    # detail_installation = get_object_or_404(Installation, pk=Installation.id)
    equipement_service= Installation.objects.filter(service='En service')
    # inst = Installation.objects.filter(equipement_installe=Equipement.categoryE)
    equipement_panne = Installation.objects.filter(service='En panne')
    profile = Profile.objects.all()
    user = User.objects.all()



    paginator = Paginator(list_direction, 3)
    page_numbre = request.GET.get('page')
    page_obj = paginator.get_page(page_numbre)
    context={
       'title':'Accueil',
        # 'inst':inst,
        'list_quip': list_quip,
        'list_installation':list_installation,
        'list_direction':page_obj,
        'equipement_service':equipement_service,
        'equipement_panne':equipement_panne,
        'profile': profile,
        'user': user,
        'list_category':list_category,
        'list_dir':list_dir,

    }
    return render(request,'equipement/index.html',context)


@login_required(login_url='accounts/login')
def tableuser(request):
    profile = Profile.objects.all()
    user = User.objects.all()

    # n= Equipement.objects.all().count|sub-Installation.objects.all().count


    context={

        'profile': profile,
        'user': user

    }
    return render(request,'equipement/table_user.html',context)





# ajoute un equipement
@login_required(login_url='accounts/login')

def EquipementCreate(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"L'equipemet du numero  {myform.num_serie} est bien ajoute")
            return redirect(reverse('equip:add_equipement'))
        else:
            messages.error(request, "Un erreur se produire")
    else:
        form = EquipementForm()

    return render(request, 'equipement/add_equipement.html', {'form': form})



#afficher info d'equipement
@login_required(login_url='accounts/login')
def EquipementDetail(request, equipement_id):
    equipement_installe= get_object_or_404(Equipement, pk=equipement_id)
    inst= Installation.objects.filter(equipement_installe=equipement_id)
    # inst_id = Installation.objects.get(id=equipement_installe.installation_equipement.id)
    # insID= Equipement.objects.filter(id=equipement_installe.installation_equipement.id).exists()

    # equip_id = Installation.objects.get(id=equipement_installe.id)

    # inst_equip = Installation.equipement_installe
    # installation_equipement:releted_name between equipement and installation
    # check before save data from comment form
    if request.method == 'POST':
        installation_form = EquipInstall(data=request.POST)
        # Atribut_inst = AtributForm(data=request.POST)
        if installation_form.is_valid():
            deja_installe = installation_form.save(commit=False)
            deja_installe.author = request.user
            deja_installe.equipement_installe = equipement_installe
            # Atribut_inst.equipement_installe.etat_equipement='1'
            # Atribut_inst.save()

            deja_installe.save()
            messages.success(
                request, f"Felicitation l'equipemet est bien installer")
            return redirect('equip:detail_equipement', equipement_id)
        # else:
        #     return redirect('equip:detail_equipement', equipement_id)
    else:
        installation_form = EquipInstall()

    context = {
        'title': 'detail equipement',
        'equipement_installe': equipement_installe,
        # 'inst_equip': inst_equip,
        'inst':inst,
        'installation_form': installation_form,
        # 'Atribut_inst':Atribut_inst
        #  'inst_id':inst_id,
        # 'insID':insID,

    }

    return render(request, 'equipement/detail_equipement.html', context)



# modifier equipement
# @login_required(login_url='user_auth:login')
@login_required(login_url='accounts/login')

def EquipementUpdate(request, equipement_id):
    equipement=Equipement.objects.get(id=equipement_id)
    form=EquipementFormm(instance=equipement)

    if request.method == 'POST':
        form=EquipementFormm(request.POST, instance=equipement)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"L'equipemet du numero  {myform.num_serie} est bien modifier")
            return redirect('equip:detail_equipement',equipement_id)

    context = {
        'title': 'Modifier_equipement',
        'form': form
        }

    return render(request,'equipement/update_equipement.html', context)



# class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
#     model = Equipement
#     template_name = 'equipement/update_equipement.html'
#     form_class = EquipementForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         equip = self.get_object()
#         if self.request.user == equip.author:
#             return True
#         else:
#             return True





# # supprimer equipement
# class EquipementDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
#     model = Equipement
#     success_url = '/table'
#     # equip: table_equipement
#     def test_func(self):
#         equipo= self.get_object()
#         if self.request.user == equipo.author:
#             return True
#         else:
#             return True

# delet equipement
@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])

def EquipementDeleteView(request, equipement_id):
    equipement=Equipement.objects.get(id=equipement_id)
    if request.method == 'POST':
        equipement.delete()
        messages.success(
            request, f"Felicitation l'equipemet avec numero  {equipement.num_serie} est bien supprimer")
        return redirect('equip:table_equipement')

    context = {
        'title': 'Supprimer_equipement',
        'equipement': equipement
        }

    return render(request,'equipement/equipement_confirm_delete.html', context)


@login_required(login_url='accounts/login')
def table_equipement(request):
    list_quip=Equipement.objects.all()
    # filters
    filter = EquipementFilter(request.GET, queryset=list_quip)
    list_quip = filter.qs
    context={
       'title':'Table_des_equipement',
        'list_quip':list_quip,
        'filter': filter,

    }
    return render(request,'equipement/table_equip.html',context)

#view cataegorie equipement
@login_required(login_url='accounts/login')
def category_table(request):
    list_cat=Category.objects.all()
    list_direction = Direction.objects.all()
    context={
       'title':'Categorie des equipements et les directions',
        'list_cat':list_cat,
        'list_direction': list_direction
    }
    return render(request,'equipement/category_table.html',context)


#add categorie equipement
@login_required(login_url='accounts/login')

def CategorietCreate(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            myform=form.save()
            messages.success(
                request, f"Felicitations la categorie  {myform.name}  est bien ajoute")
            return redirect(reverse('equip:add_categorie'))
    else:
        form = CategorieForm()

    context = {
        'title': "Categorie D'equipement",
        'form':form,

    }
    return render(request, 'equipement/add_categorie.html', context)

#edit categorie equipement
@login_required(login_url='accounts/login')

def CategoryUpdate(request, categorie_id):
    category=Category.objects.get(id=categorie_id)
    form=CategorieForm(instance=category)

    if request.method == 'POST':
        form=CategorieForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation categorie {category.name} est bien modifier")
            return redirect('equip:category_table')

    context = {
        'title': 'Modifier_categorie',
        'form': form
        }

    return render(request,'equipement/update_categorie.html', context)




#direction
@login_required(login_url='accounts/login')

def DirectionCreate(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            myform=form.save()
            messages.success(
                request, f"Felicitation nom de la direction  {myform.Nom} est bien ajoute")
            return redirect(reverse('equip:add_direction'))
    else:
        form = DirectionForm()

    context = {
        'title': "Adresse De La Direction",
        'form':form,

    }
    return render(request, 'equipement/add_direction.html', context)


#edit direction
@login_required(login_url='accounts/login')

def DirectionUpdate(request, direction_id):
    direction=Direction.objects.get(id=direction_id)
    form=DirectionForm(instance=direction)

    if request.method == 'POST':
        form=DirectionForm(request.POST, instance=direction)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Felicitation nom direction {direction.Nom} est bien modifier")
            return redirect('equip:category_table')

    context = {
        'title': 'Modifier_direction',
        'form': form
        }

    return render(request,'equipement/update_direction.html', context)




# ajoute un equipement
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DeleteView

from accounts.decorators import allowed_users
from equipement.models import Equipement, Category
from installation.forms import InstallationForm, InstallationFormm, ServiceForm
from installation.models import Installation




# table installation
@login_required(login_url='accounts/login')
def table_installation(request):
    list_installation=Installation.objects.all()
    # list_installation_direction = Installation.objects.filter()
    context={
       'title':'Table des installation',
        'list_installation':list_installation,
        # 'list_installation_direction':list_installation_direction,
    }
    return render(request,'installation/table_installation.html',context)



#add installation
@login_required(login_url='accounts/login')

def InstallationCreate(request):
    if request.method == 'POST':
        form = InstallationForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"Felicitations votre ajout  est bien ajoute")
            return redirect(reverse('install:add_install'))
    else:
        form = InstallationForm()

    context = {
        'title': 'Detail Installation',
        'form':form,

    }

    return render(request, 'installation/add_installation.html', context)


#edit installation
@login_required(login_url='accounts/login')

def InstallationUpdate(request, installation_id):
    installation=Installation.objects.get(id=installation_id)
    form=InstallationFormm(instance=installation)

    if request.method == 'POST':
        form=InstallationFormm(request.POST, instance=installation)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            messages.success(
                request, f"Felicitation l'info d'installation avec mac adresse du numero  {myform.mac} est bien modifier")
            return redirect('install:detail_installation',installation_id)

    context = {
        'title': 'Modifier_info_installation',
        'form': form,
        'installation':installation,
        }

    return render(request,'installation/update_installation.html', context)

#Etat service update
@login_required(login_url='accounts/login')
@allowed_users(allowed_roles=['admin'])
def ServiceUpdate(request, service_id):
    installation=Installation.objects.get(id=service_id)
    form=ServiceForm(instance=installation)

    if request.method == 'POST':
        form=ServiceForm(request.POST, instance=installation)
        if form.is_valid():

            form.save()

            messages.success(
                request, f"Felicitation l'etat du service equipemnet est bien mise a jour")
            return redirect('install:detail_installation',service_id)

    context = {
        'title': 'Etat_service',
        'form': form,
        'installation':installation,
        }

    return render(request,'installation/update_service.html', context)





# delet installation
@login_required(login_url='accounts/login')

def InstallationDeleteView(request, installation_id):
    installation=Installation.objects.get(id=installation_id)
    if request.method == 'POST':
        installation.delete()
        messages.success(
            request, f"Felicitation l'equipemet avec numero  {installation.equipement_installe.num_serie} est bien desinstaller")
        return redirect('equip:detail_equipement', installation.equipement_installe.id)

    context = {
        'title': 'Desintaller_equipement',
        'installation': installation
        }

    return render(request,'installation/installation_confirm_delete.html', context)


# detail installation
@login_required(login_url='accounts/login')
def InstallationDetail(request, installation_id):
    detail_installation = get_object_or_404(Installation, pk=installation_id)
    # equipement_installe = Equipement.objects.filter(equipement_id=inst)
    # nstallations = equipement_installe.installation_equipement

    context = {
        'title': 'detail installation',

        'detail_installation':detail_installation,
        # 'nstallations':nstallations,

        # 'equipement_installe':equipement_installe,

    }

    return render(request, 'installation/detail_installation.html', context)








# def InstallationDetail(request, equipement_id):
#     equipement_installe= get_object_or_404(Equipement, pk=equipement_id)
#     inst= Installation.objects.filter(equipement_installe=equipement_id)
#     nstallations = equipement_installe.installation_equipement
#
#
#     context = {
#         'title': 'detail installation',
#
#         'inst':inst,
#         'nstallations':nstallations,
#
#         'equipement_installe':equipement_installe,
#
#     }
#
#     return render(request, 'equipement/detail_installation.html', context)




# # detail_equipement/<int:equipement_id>/
# #supprimer installation
# class InstallationDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
#     model = Installation
#     success_url = '/table_installation'
#     def test_func(self):
#         inst= self.get_object()
#         if self.request.user == inst.author:
#             return True
#         else:
#             return True
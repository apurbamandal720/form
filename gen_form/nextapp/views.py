from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from nextapp.functions.fonctions import handle_uploaded_file
from nextapp.forms import *
# Create your views here.
def regestion(request):
    return render(request,'admin_reg.html')
def rege(request):
	usr_otp = random.randint(100000, 999999)
	cat = usr_otp
	if request.method=='POST':
		c=re_meForm(request.POST, request.FILES)
		cc = re_me()
		cc.b_name = request.POST['b_name']
		cc.l_band= request.POST['l_band']
		cc.contact = request.POST['contact']
		cc.num_mem = request.POST['num_mem']
		cc.num_band_mem = request.POST['num_band_mem']
		cc.establi_date = request.POST['establi_date']
		cc.link_social = request.POST['link_social']
		cc.group_ph = request.POST['group_ph']
		cc.des = request.POST['des']
		cc.ca = request.POST['ca']
		cc.ca1=request.POST['ca1']
		if cc.ca == cc.ca1:
			cc.save()
			return HttpResponse("<br><br><br><center><h1 color:red>Reristration successful</h1></center>")
		else:
			return HttpResponse('<br><br><br><center><h1 color:red>You are typeing wrong captchar.</h1></center>')
	else:
		c=re_meForm()
		return render(request, 'admin_reg.html', {'us': usr_otp})
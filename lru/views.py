from django.http import Http404
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from forms import UtstyrForm, UtstyrsListeForm, ReservationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django import forms
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


from lru.models import Utstyr, Reservasjon

@login_required
def index(request):
	
	args = {}
	args['bruker'] = request.user
	args['reservasjonsliste'] = reversed(Reservasjon.objects.all())
	args.update(csrf(request))
	if request.method == 'POST':
		form = UtstyrsListeForm(request.POST)
		if form.is_valid():
			form.save()
			request.session["test"] = form.cleaned_data['utstyr']
			return redirect('/lru/reservation')
		else:
			args['form'] = form
			return render(request, 'lru/index.html', args)
	else:
		form = UtstyrsListeForm()
		
	args['form'] = form
	return render(request, 'lru/index.html', args)

	
def create(request):
	if request.POST:
		form = UtstyrForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/lru')
	else:
		form = UtstyrForm()
		
	args = {}
	args.update(csrf(request))
	args['form'] = form
	
	return render_to_response('lru/create.html', args)

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('lru/login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/lru/')
	else:
		return HttpResponseRedirect('/lru/invalid/')

def logout(request):
	auth.logout(request)
	return render_to_response('lru/logout.html')

def loggedin(request):
	return render_to_response('lru/loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
	
	return render_to_response('lru/invalid_login.html')

@login_required	
def reservation(request):
	args = {}
	args.update(csrf(request))	
	args['valgt_utstyr'] = request.session.get('test')
	args['lokasjon'] = args['valgt_utstyr'].lokasjon
	args['beskrivelse'] = args['valgt_utstyr'].beskrivelse
	args['siste_res'] = reversed(Reservasjon.objects.filter(utstyr__exact=args['valgt_utstyr']))
	
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/lru/')
		else:
			args['form'] = form
			return render(request, 'lru/reservation.html', args)	
	else:
		form = ReservationForm(initial={'reservert_av': request.user,'utstyr': args['valgt_utstyr']})
		args['form'] = form	
		return render(request, 'lru/reservation.html', args)
		
	
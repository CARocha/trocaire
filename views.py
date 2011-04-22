from django.http import HttpResponse
from trocaire.lugar.models import *
from trocaire.encuesta.models import *
from django.utils import simplejson

def get_depas(request):
    id = request.GET.get('id', '')
    depas = Departamento.objects.filter(pais__pk=int(id)).values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(depas)), mimetype='application/json')

def get_munis(request):
    id = request.GET.get('id', '')
    if id:
	    depas = Municipio.objects.filter(departamento__pk=int(id)).values('id', 'nombre')	
	
    ids = request.GET.get('ids', '')	
    if ids:
		dicc = {}
		resultado = []
		for id in ids.split(','):
			try:
				lista = []
				departamento = Departamento.objects.get(pk=int(id))
				[lista.append(municipio) for municipio in Municipio.objects.filter(departamento=departamento).order_by('nombre').values('id', 'nombre')]
				dicc[departamento.nombre] = lista
			except:
				pass
		resultado.append(dicc)
		return HttpResponse(simplejson.dumps(resultado), mimetype='application/json')	
	
    orgs = request.GET.get('orgs', '')
    if orgs:		
		munis = []
		lista = []
		contrapartes = Contraparte.objects.filter(pk__in=map(lambda x: int(x), orgs.split(','))).order_by('departamento__nombre')
		[munis.append(contraparte.municipio.pk) for contraparte in contrapartes]
		[lista.append(municipio) for municipio in Municipio.objects.filter(pk__in=set(munis)).order_by('nombre').values('id', 'nombre')]
		return HttpResponse(simplejson.dumps(lista), mimetype='application/json')	
	
    return HttpResponse(simplejson.dumps(list(depas)), mimetype='application/json')

def __get_data(request):
    id = request.GET.get('id', '')
    org = Contraparte.objects.get(pk=int(id))
    values = []
    values.append(org.departamento.id)
    values.append(org.municipio.id)

    return HttpResponse(simplejson.dumps(values), mimetype='application/json')
	
def get_group_depas(request):
	'''Metodo que devuelve los departamentos agrupados por pais en JSON format'''
	ids = request.GET.get('ids', '')
	dicc = {}
	resultado = []
	for id in ids.split(','):
		try:
			lista = []
			pais = Pais.objects.get(pk=int(id))
			for departamento in Departamento.objects.filter(pais=pais).order_by('nombre'):
				depa = {}
				depa['id'] = departamento.pk
				depa['nombre'] = departamento.nombre
				lista.append(depa)
			dicc[pais.nombre] = lista
		except:
			pass
	resultado.append(dicc)	
	return HttpResponse(simplejson.dumps(resultado), mimetype='application/json')

def get_orgs(request):
    ids = request.GET.get('ids', '')
    orgs = Contraparte.objects.filter(departamento__pk__in=map(lambda x: int(x), ids.split(','))).values('id', 'nombre_corto')

    return HttpResponse(simplejson.dumps(list(orgs)), mimetype='application/json')
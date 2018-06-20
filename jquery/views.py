from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


def index(request):
    template_name = 'index_jquery.html'
    data = {}

    return render(request, template_name, data)


def show(request):
    template_name = 'contacto.html'
    data = {}

    return render(request, template_name, data)


@csrf_protect
def json(request):
    data = {}

    data['id'] = 1
    data['body'] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus expedita iste, obcaecati reiciendis nostrum distinctio necessitatibus eum quisquam beatae doloribus aliquid laudantium similique in nisi incidunt id minus quod consequuntur!'  
    data['title'] = 'lorem asdfs'

    return JsonResponse(data)

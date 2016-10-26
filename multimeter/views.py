from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import UniversalJsonContainer
from .controllers import JSONResponse, GenerateRandomInRange
from .serializers import UniversalJsonContainerSerializer


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):

    data = UniversalJsonContainer.objects.create(session_id=0, content_type="data", 
    	data={"x":GenerateRandomInRange(0,9), "y":GenerateRandomInRange(0,9)})
    data.save()

    all_data = UniversalJsonContainer.objects.all()

    return render(request, 'multimeter.html', {'all_data': all_data})

@csrf_exempt
def universal_json_container_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        json_container = UniversalJsonContainer.objects.all()
        serializer = UniversalJsonContainerSerializer(json_container, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UniversalJsonContainerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def universal_json_container_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        json_container = UniversalJsonContainer.objects.get(pk=pk)
    except UniversalJsonContainer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UniversalJsonContainerSerializer(json_container)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UniversalJsonContainerSerializer(json_container, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        json_container.delete()
        return HttpResponse(status=204)

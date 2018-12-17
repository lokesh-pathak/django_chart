from django.shortcuts import render
from .models import SampleData
from django.views.generic import View
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def pagination(request, object_list):
    """
    :param request:
    :param object_list:
    :return: pagination for the list
    """
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 100)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects


class HomeView(View):
    def get(self, request):
        params={}
        params['data'] = pagination(request, SampleData.objects.all())
        return render(request, "index.html", params)

class DispalyGraph(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        test_data = SampleData.objects.select_related().all()
        sex = test_data.values('sex').annotate(count=Count('sex'))
        relationship = test_data.values('relationship').annotate(count=Count('relationship'))
        sex_labels = [x['sex'].capitalize() for x in sex]
        sex_data = [x['count'] for x in sex]
        relationship_labels = [x['relationship'].capitalize() for x in relationship]
        relationship_data = [x['count'] for x in relationship]
        data= {
            "sex_labels":sex_labels,
            "sex_data": sex_data,
            "relationship_labels":relationship_labels,
            "relationship_data":relationship_data
        }
        return Response(data)
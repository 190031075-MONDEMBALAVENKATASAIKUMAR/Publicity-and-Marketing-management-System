from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = [
            'Samsung',
            'Realme',
            'Apple',
            'HP'
        ]
        chartLabel = "my data"
        chartdata = [4, 10, 8, 3]
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)
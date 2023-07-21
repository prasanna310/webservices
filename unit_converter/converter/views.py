from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from pint import UnitRegistry

ureg = UnitRegistry()

class ConvertView(APIView):
    def get(self, request):
        value = float(request.query_params.get('value'))  # Convert the value to float
        from_unit = request.query_params.get('from')
        to_unit = request.query_params.get('to')
        value_in_from_unit = ureg.Quantity(value, from_unit)
        converted_value = value_in_from_unit.to(to_unit).magnitude
        return Response({'value': converted_value})


from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from pint import UnitRegistry

ureg = UnitRegistry()

mapping =  {"cfs": "cubic foot per second" ,
            "gpm": "gallon per minute" ,
            "gpd": "gallon per day" ,
            "ac-ft/yr":'acre foot per year' ,

            }

def replace_string(in_str, mapping):
    return ' '.join([mapping.get(i, i) for i in in_str.split()])

class ConvertView(APIView):
    def get(self, request):
        value = float(request.query_params.get('value'))  # Convert the value to float
        from_unit = request.query_params.get('from')
        to_unit = request.query_params.get('to')

        # replace custom units
        from_unit= replace_string(from_unit, mapping)
        to_unit= replace_string(to_unit, mapping)


        value_in_from_unit = ureg.Quantity(value, from_unit)
        converted_value = value_in_from_unit.to(to_unit).magnitude
        return Response({'value': converted_value})


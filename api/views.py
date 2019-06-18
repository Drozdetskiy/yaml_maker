from rest_framework import generics
from rest_framework.response import Response

from api.serializers import YamlSerializer
from yaml_maker.settings import PRINT_YAML


class YamlDetail(generics.GenericAPIView):
    def get(self, request):
        obj = YamlSerializer(**request.META)
        if PRINT_YAML:
            print(obj.data)
        return Response(obj.represent())

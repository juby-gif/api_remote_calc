from rest_framework import status, response, views
from foundation.models import Memory

class VersionAPIView(views.APIView):

    def get(self, request):
        """
        The ``GET`` call will return a simple message.
        """
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'version': '2.1.2',
            }
        )

class AddAPIView(views.APIView):
    def post(self, request):

        value = float(request.data['value'])
        try:
            memory = Memory.objects.get(id=1)

        except Exception as e:
            memory =  Memory.objects.create(id = 1, value = 0)

        memory.value = value + memory.value
        memory.save()
        print(memory.value)
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'detail': "Value was added",
            }
        )
class ResultAPIView(views.APIView):
    def get(self,request):

        try:
            memory = Memory.objects.get(id=1)

        except Exception as e:
            memory =  Memory.objects.create(id = 1, value = 0)
        result = memory.value
        print(result)
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'result': result,
            }
        )

class ClearAPIView(views.APIView):
    def post(self,request):
        try:
            memory = Memory.objects.get(id=1)

        except Exception as e:
            memory =  Memory.objects.create(id = 1, value = 0)
        memory.delete()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': "Memory has been cleared and the value is "+str(memory.value),
            }
        )

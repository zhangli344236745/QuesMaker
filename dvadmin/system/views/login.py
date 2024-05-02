from rest_framework.views import APIView
from dvadmin.utils.json_response import DetailResponse

class CaptchaView(APIView):
    authentication_classes =  []
    permission_classes = []

    def get(self,request):
        data = {"test":'ok'}
        return DetailResponse(data=data)

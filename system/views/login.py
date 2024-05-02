from rest_framework.views import APIView
from django.contrib.auth.models import User
from dvadmin.utils.json_response import DetailResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CaptchaView(APIView):
    authentication_classes =  []
    permission_classes = []

    def get(self,request):
        data = {"test":'ok'}
        return DetailResponse(data=data)
class LoginSerializer(TokenObtainPairSerializer):

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {"no_active_account": ("账号/密码错误")}

    def validate(self, attrs):
        data = super().validate(attrs)
        data["name"] = self.user.username
        data["userId"] = self.user.id
        request = self.context.get("request")
        request.user = self.user
        return {"code": 2000, "msg": "请求成功", "data": data}

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = []
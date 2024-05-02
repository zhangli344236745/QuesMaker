from django.urls import path
from rest_framework import routers
from system.views.api_white_list import ApiWhiteListViewSet

system_url = routers.SimpleRouter()
# system_url.register(r'menu', MenuViewSet)
# system_url.register(r'menu_button', MenuButtonViewSet)
# system_url.register(r'role', RoleViewSet)
# system_url.register(r'dept', DeptViewSet)
# system_url.register(r'user', UserViewSet)
# system_url.register(r'operation_log', OperationLogViewSet)
# system_url.register(r'dictionary', DictionaryViewSet)
# system_url.register(r'area', AreaViewSet)
# system_url.register(r'file', FileViewSet)
system_url.register(r'api_white_list', ApiWhiteListViewSet)
# system_url.register(r'system_config', SystemConfigViewSet)
# system_url.register(r'message_center',MessageCenterViewSet)

urlpatterns = [
    # path('user/export/', UserViewSet.as_view({'post': 'export_data', })),
    # path('user/import/', UserViewSet.as_view({'get': 'import_data', 'post': 'import_data'})),
    # path('system_config/save_content/', SystemConfigViewSet.as_view({'put': 'save_content'})),
    # path('system_config/get_association_table/', SystemConfigViewSet.as_view({'get': 'get_association_table'})),
    # path('system_config/get_table_data/<int:pk>/', SystemConfigViewSet.as_view({'get': 'get_table_data'})),
    # path('system_config/get_relation_info/', SystemConfigViewSet.as_view({'get': 'get_relation_info'})),
    # path('login_log/', LoginLogViewSet.as_view({'get': 'list'})),
    # path('login_log/<int:pk>/', LoginLogViewSet.as_view({'get': 'retrieve'})),
    # path('dept_lazy_tree/', DeptViewSet.as_view({'get': 'dept_lazy_tree'})),
]
urlpatterns += system_url.urls
from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api', views.UserViewSet.as_view({'get': 'list'}))
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
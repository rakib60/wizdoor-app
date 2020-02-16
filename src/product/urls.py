from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),

    # path("products/", 
    #     ProductCreateAPIView.as_view(), 
    #     name="create-product"),

    # path("questions/<slug:slug>/answer/", 
    #         qv.AnswerCreateAPIView.as_view(), 
    #         name="create-answer"),

    # path("answers/<int:pk>/", 
    #     qv.AnswerRUDAPIView.as_view(), 
    #     name="answer-details"),

    # path("answers/<int:pk>/like/", 
    #     qv.AnswerLikeApiView.as_view(), 
    #     name="answer-like"),
]

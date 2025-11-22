from rest_framework import routers
from .views import BooksViewSet

router = routers.DefaultRouter()
router.register("book", BooksViewSet)

urlpatterns = router.urls
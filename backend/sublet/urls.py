from django.urls import path
from rest_framework import routers

from sublet.views import Amenities, Favorites, Offers, Properties, UserFavorites, UserOffers


app_name = "sublet"

router = routers.DefaultRouter()
router.register(r"properties", Properties, basename="properties")

additional_urls = [
    path("amenities/", Amenities.as_view(), name="amenities"),
    path("favorites/", UserFavorites.as_view(), name="user-favorites"),
    path("offers/", UserOffers.as_view(), name="user-offers"),
    path(
        "properties/<sublet_id>/favorites/",
        Favorites.as_view({"post": "create", "delete": "destroy"}),
    ),
    path(
        "properties/<sublet_id>/offers/",
        Offers.as_view({"get": "list", "post": "create", "delete": "destroy"}),
    ),
]

urlpatterns = router.urls + additional_urls

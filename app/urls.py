from django.urls import path
from .views import subscribe,empCreateView,empListView,empDetailView,empDetailView,empUpdateView,empDeleteView, usercreate

urlpatterns = [
   path("create/", empCreateView.as_view(), name="create"),
   path("", empListView.as_view(), name="list"),
   path("signin",usercreate.as_view(), name="signin"),
   path("<pk>/detail/", empDetailView.as_view(), name="details"),
   path("<pk>/update/", empUpdateView.as_view(), name="update"),
   path("<pk>/delete/", empDeleteView.as_view(), name="delete"),
   path("mail/", subscribe, name="subscribe")
]

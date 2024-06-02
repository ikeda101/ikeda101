from django.urls import path
from .views import (
                    NippoListView ,
                    NippoDetailView, 
                    NippoCreateModelFormView, 
                    NippoUpdateModelFormView,
                    NippoDeleteView,
                    NippoAllView,
                  )

urlpatterns = [
  path("", NippoListView.as_view(), name="nippo-list"),
  path("detail/<slug:slug>/", NippoDetailView.as_view(), name="nippo-detail"),
  path("create/", NippoCreateModelFormView.as_view(), name="nippo-create"),
  path("update/<slug:slug>/", NippoUpdateModelFormView.as_view(), name="nippo-update"),
  path("delete/<slug:slug>/", NippoDeleteView.as_view(), name="nippo-delete"),
  # 2024-04-20 追加
  path("all/", NippoAllView.as_view(), name="nippo-all"),
]
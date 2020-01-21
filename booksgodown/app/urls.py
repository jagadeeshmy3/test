from django.conf.urls import url
from app import views
urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^bookslist/',views.display_view),
    url(r'^insert/',views.insert_view),
]
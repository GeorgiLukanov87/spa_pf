from django.urls import path

from spa_pf.web_portfolio.views import index

urlpatterns = (
    path('', index, name='index'),
)

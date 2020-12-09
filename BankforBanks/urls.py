from django.conf.urls import url
from django.urls import path
from BankforBanks import views

urlpatterns = [
    path(r'', views.index, name="index"),
    url(r'^signin/', views.sign_in, name="sign_in"),
    url(r'^stats/', views.bank_stats, name="bank_stats"),
    url(r'^logout/', views.log_out, name="log_out"),
    url(r'^main/', views.main_page, name="main"),
    url(r'^accounts/', views.accounts, name="accounts"),
    url(r'^analysis/', views.analysis, name="analysis"),
    url(r'^add-accounts/', views.add_account, name="add_account"),

]
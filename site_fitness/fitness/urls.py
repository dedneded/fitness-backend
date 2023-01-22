from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('', Home.as_view(), name='home'), #http://127.0.0.1:8000/
    path('halls/', Halls.as_view(), name='halls'),
    path('trainers/', Trainers.as_view(), name='trainers'),
    path('subscriptions/', Subscriptions.as_view(), name='subscriptions'),
    path('admin_visit_by_subscription/', AdminVisitBySubscription.as_view(), name='admin_visit_by_subscription'),
    path('admin_visits/', AdminVisits.as_view(), name='admin_visits'),
    path('admin_sport-services/', AdminSportServices.as_view(), name='admin_sport-services'),
    path('admin_services/', AdminServices.as_view(), name='admin_services'),
    path('admin_subscriptions/', AdminSubscriptions.as_view(), name='admin_subscriptions'),
    path('admin_employees/', AdminEmployees.as_view(), name='admin_employees'),
    path('admin_timetable/', AdminTimetable.as_view(), name='admin_employee_timetable'),
    path('admin_roles/', AdminRoles.as_view(), name='admin_roles'),
    path('admin_sales/', AdminSales.as_view(), name='admin_sales'),
    path('admin_reviews/', AdminReviews.as_view(), name='admin_reviews'),
    path('admin_manage_main/', AdminManageMain.as_view(), name='admin_manage_main'),
    path('admin_profile/', AdminProfile.as_view(), name='admin_profile'),
    path('admin_clients/', AdminClients.as_view(), name='admin_clients'),
    path('admin_client_create/', AdminClientCreate.as_view(), name='admin_client_create'),
    path('admin_client/<int:pk>/', AdminClientSee.as_view(), name='client_detail'),
    path('admin_client/<int:pk>/edit/', AdminClientUpdate.as_view(), name='client_edit'),
    path('admin_employees/', AdminEmployees.as_view(), name='admin_employees'),
    path('admin_employee/<int:pk>/', AdminEmployeeSee.as_view(), name='employee_detail'),
    path('admin_employee_create/', AdminEmployeeCreate.as_view(), name='employee_create'),
    path('admin_employee/<int:pk>/edit/', AdminEmployeeUpdate.as_view(), name='employee_edit'),
    path('admin_employee/<int:pk>/delete/', employee_delete, name='employee_delete'),
    path('admin_employee/<int:pk>/edit_roles/', add_role_view, name='add_role_view'),
    path('admin_employee/<int:pk>/delete_roles/', delete_role_view, name='delete_role_view'),
    path('admin_halls/', AdminHalls.as_view(), name='admin_halls'),
    path('admin_hall/<int:pk>/', AdminHallSee.as_view(), name='hall_detail'),
    path('admin_hall/<int:pk>/edit/', AdminHallUpdate.as_view(), name='hall_edit'),
    path('admin_hall/<int:pk>/delete/', hall_delete, name='hall_delete'),

]
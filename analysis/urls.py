from django.urls import path
from analysis.views import *


app_name = 'app'
urlpatterns = [
    path('', DashboardHome.as_view(), name='dashboard-home'),
    path('charts/', Charts.as_view(), name='charts'),
    path('tables/', Tables.as_view(), name='tables'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgotpassword'),
    path('pricingstrategy/', PricingStrategy.as_view(), name='pricingstrategy'),
    path('customersatisfaction/', CustomerSatisfaction.as_view(), name='customersatisfaction'),

    path('barchart/', BarChart.as_view(), name='barchart'),
    path('linechart/', LineChart.as_view(), name='linechart'),
    path('piechart/', PieChart.as_view(), name='piechart'),
    path('datatable/', DataTable.as_view(), name='datatable'),
    path('maps/', Maps.as_view(), name='maps'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),

    path('api/data/', DataTable_Json, name='api_data'),
 #   path('api/customersatisfaction/', CustomerSatisfaction_Json, name='api_data')


]


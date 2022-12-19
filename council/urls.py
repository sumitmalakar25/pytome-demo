from django.urls import path
from.views.base import Base
from.views import signup
from.views.signup import Signup
from.views.login import Login, logout
from .views.complain import Complaint
# from .views.solution import Solution
from.views.success import Success
from.views.success1 import Success1


urlpatterns=[
    path('', Base.as_view(), name='homepage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('success/', Success.as_view(), name='success'),
    path('success1/', Success1.as_view(), name='success1'),
    path('complain/',Complaint.as_view(), name='complain'),
    # path('solution/',Solution.as_view(), name='solution'),

]


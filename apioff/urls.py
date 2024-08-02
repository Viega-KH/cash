# urls.py
from django.urls import path
from .views import (
    positionschoollist, infoschoollist, officeschoollist,
    positionlevellist, infolevellist, officelevellist, infoschooldetail, infoleveldetail
)

urlpatterns = [
    # School URLs
    path('school/positions/', positionschoollist.as_view(), name='position_school_list_create'),
    path('school/infos/', infoschoollist.as_view(), name='info_school_list_create'),
    path('school/infos/<int:pk>', infoschooldetail.as_view(), name='info_school_detail'),
    path('school/offices/', officeschoollist.as_view(), name='office_school_list_create'),

    # Slevel URLs
    path('slevel/positions/', positionlevellist.as_view(), name='position_level_list_create'),
    path('slevel/infos/', infolevellist.as_view(), name='info_level_list_create'),
    path('slevel/infos/<int:pk>', infoleveldetail.as_view(), name='info_level_detail'),
    path('slevel/offices/', officelevellist.as_view(), name='office_level_list_create'),
]

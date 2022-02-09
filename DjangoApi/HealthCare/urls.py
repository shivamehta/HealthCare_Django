from django.conf.urls import url
from HealthCare import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[

    url(r'^user$',views.tbl_user_detailApi),
    url(r'^user/([0-9A-Fa-f-]+)$',views.tbl_user_detailApi),

    url(r'^height$',views.m_heightApi),
    url(r'^height/([0-9A-Fa-f-]+)$',views.m_heightApi),

    url(r'^location$',views.m_LocationApi),
    url(r'^location/([0-9A-Fa-f-]+)$',views.m_LocationApi),

    url(r'^entityType$',views.m_entity_typeApi),
    url(r'^entityType/([0-9A-Fa-f-]+)$',views.m_entity_typeApi),

    url(r'^entityDetail$',views.m_EntityDetailApi),
    url(r'^entityDetail/([0-9A-Fa-f-]+)$',views.m_EntityDetailApi),

    url(r'^speciality$',views.m_specialityApi),
    url(r'^speciality/([0-9A-Fa-f-]+)$',views.m_specialityApi),

    url(r'^entitySpeciality$',views.m_entity_specialityApi),
    url(r'^entitySpeciality/([0-9A-Fa-f-]+)$',views.m_entity_specialityApi)
]

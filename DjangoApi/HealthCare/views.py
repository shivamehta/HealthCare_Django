import uuid
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.models import User


from HealthCare.models import TblUserDetail,MHeight,MLocationDetail,MEntityType,MEntityDetail,MEntitySpeciality,MSpeciality
from HealthCare.serializers import TblUserDetailSerializer,MHeightSerializer,MLocationDetailSerializer,MEntityTypeSerializer,MEntityDetailSerializer,MSpecialitySerializer,MEntitySpecialitySerializer

from django.core.files.storage import default_storage



@csrf_exempt
def m_entity_typeApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_entity_type = MEntityType.objects.all()
        m_entity_type_serializer=MEntityTypeSerializer(m_entity_type,many=True)
        return JsonResponse(m_entity_type_serializer.data,safe=False)
    elif request.method=='POST':
        m_entity_type_data=JSONParser().parse(request)
        m_entity_type_serializer=MEntityTypeSerializer(data=m_entity_type_data)
        if m_entity_type_serializer.is_valid():
            #addedby.save()
            m_entity_type_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_entity_type_data=JSONParser().parse(request)
        m_entity_type=MEntityType.objects.get(entity_typeid=m_entity_type_data['entity_typeid'])
        m_entity_type_serializer=MEntityTypeSerializer(m_entity_type,data=m_entity_type_data)
        if m_entity_type_serializer.is_valid():
            m_entity_type_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_entity_type=MEntityType.objects.get(entity_typeid=id)
        m_entity_type.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def m_LocationApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_location = MLocationDetail.objects.all()
        m_location_serializer=MLocationDetailSerializer(m_location,many=True)
        return JsonResponse(m_location_serializer.data,safe=False)
    elif request.method=='POST':
        m_location_data=JSONParser().parse(request)
        m_location_serializer=MLocationDetailSerializer(data=m_location_data)
        if m_location_serializer.is_valid():
            #addedby.save()
            m_location_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_location_data=JSONParser().parse(request)
        m_location=MLocationDetail.objects.get(locationid=m_location_data['locationid'])
        m_location_serializer=MLocationDetailSerializer(m_location,data=m_location_data)
        if m_location_serializer.is_valid():
            m_location_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_location=MLocationDetail.objects.get(locationid=id)
        m_location.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def m_EntityDetailApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_entityDetail = MEntityDetail.objects.all()
        m_entityDetail_serializer=MEntityDetailSerializer(m_entityDetail,many=True)
        return JsonResponse(m_entityDetail_serializer.data,safe=False)
    elif request.method=='POST':
        m_entityDetail_data=JSONParser().parse(request)
        m_entityDetail_serializer=MEntityDetailSerializer(data=m_entityDetail_data)
        if m_entityDetail_serializer.is_valid():
            #addedby.save()
            m_entityDetail_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_entityDetail_data=JSONParser().parse(request)
        m_entityDetail=MEntityDetail.objects.get(entityid=m_entityDetail_data['entityid'])
        m_entityDetail_serializer=MEntityDetailSerializer(m_entityDetail,data=m_entityDetail_data)
        if m_entityDetail_serializer.is_valid():
            m_entityDetail_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_entityDetail=MEntityDetail.objects.get(entityid=id)
        m_entityDetail.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def tbl_user_detailApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        tbl_user_details = TblUserDetail.objects.all()
        tbl_user_detail_serializer=TblUserDetailSerializer(tbl_user_details,many=True)
        return JsonResponse(tbl_user_detail_serializer.data,safe=False)
    elif request.method=='POST':
        tbl_user_detail_data=JSONParser().parse(request)
        tbl_user_detail_serializer=TblUserDetailSerializer(data=tbl_user_detail_data)
        if tbl_user_detail_serializer.is_valid():
            #addedby.save()
            tbl_user_detail_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        tbl_user_detail_data=JSONParser().parse(request)
        tbl_user_detail=TblUserDetail.objects.get(pk_userid=tbl_user_detail_data['pk_userid'])
        tbl_user_detail_serializer=TblUserDetailSerializer(tbl_user_detail,data=tbl_user_detail_data)
        if tbl_user_detail_serializer.is_valid():
            tbl_user_detail_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        tbl_user_detail=TblUserDetail.objects.get(pk_userid=id)
        tbl_user_detail.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def m_heightApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_height = MHeight.objects.all()
        m_height_serializer=MHeightSerializer(m_height,many=True)
        return JsonResponse(m_height_serializer.data,safe=False)
    elif request.method=='POST':
        m_height_data=JSONParser().parse(request)
        m_height_serializer=MHeightSerializer(data=m_height_data)
        if m_height_serializer.is_valid():
            #addedby.save()
            m_height_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_height_data=JSONParser().parse(request)
        m_height=MHeight.objects.get(heightid=m_height_data['heightid'])
        m_height_serializer=MHeightSerializer(m_height,data=m_height_data)
        if m_height_serializer.is_valid():
            m_height_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_height=MHeight.objects.get(heightid=id)
        m_height.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def m_specialityApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_speciality = MSpeciality.objects.all()
        m_speciality_serializer=MSpecialitySerializer(m_speciality,many=True)
        return JsonResponse(m_speciality_serializer.data,safe=False)
    elif request.method=='POST':
        m_speciality_data=JSONParser().parse(request)
        m_speciality_serializer=MSpecialitySerializer(data=m_speciality_data)
        if m_speciality_serializer.is_valid():
            #addedby.save()
            m_speciality_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_speciality_data=JSONParser().parse(request)
        m_speciality=MSpeciality.objects.get(specialityid=m_speciality_data['specialityid'])
        m_speciality_serializer=MSpecialitySerializer(m_speciality,data=m_speciality_data)
        if m_speciality_serializer.is_valid():
            m_speciality_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_speciality=MSpeciality.objects.get(specialityid=id)
        m_speciality.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def m_entity_specialityApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_entity_speciality = MEntitySpeciality.objects.all()
        m_entity_speciality_serializer=MEntitySpecialitySerializer(m_entity_speciality,many=True)
        return JsonResponse(m_entity_speciality_serializer.data,safe=False)
    elif request.method=='POST':
        m_entity_speciality_data=JSONParser().parse(request)
        m_entity_speciality_serializer=MEntitySpecialitySerializer(data=m_entity_speciality_data)
        if m_entity_speciality_serializer.is_valid():
            #addedby.save()
            m_entity_speciality_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_entity_speciality_data=JSONParser().parse(request)
        m_entity_speciality=MEntitySpeciality.objects.get(entity_speciality_id=m_entity_speciality_data['entity_speciality_id'])
        m_entity_speciality_serializer=MEntitySpecialitySerializer(m_entity_speciality,data=m_entity_speciality_data)
        if m_entity_speciality_serializer.is_valid():
            m_entity_speciality_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_entity_speciality=MEntitySpeciality.objects.get(entity_speciality_id=id)
        m_entity_speciality.delete()
        return JsonResponse("Deleted Successfully",safe=False)
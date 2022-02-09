from rest_framework import serializers
from HealthCare.models import *


class TblUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblUserDetail
        #fields=()        
        fields=('userid','username','userfirstname','userlastname','user_contact','user_dob','gender','height','weight','bmi','blood_group','user_password','user_email','addedby','active')

class MHeightSerializer(serializers.ModelSerializer):
    class Meta:
        model=MHeight
        #fields=()        
        fields=('heightid','height_value','addedby','active')

class MLocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=MLocationDetail
        #fields=()        
        fields=('locationid','location_pincode','location_longitude','location_latitude','location_name','addedby','active')

class MEntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=MEntityType
        #fields=()        
        fields=('entity_typeid','entity_type','description','addedby','active')

class MEntityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=MEntityDetail
        #fields=()        
        fields=('entityid','entity_typeid','location','entityname','description','addedby','active')

class MSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=MSpeciality
        #fields=()        
        fields=('specialityid','speciality','description','addedby','active')

class MEntitySpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=MEntitySpeciality
        #fields=()        
        fields=('entity_speciality_id','entityid','specialityid','description','addedby','active')
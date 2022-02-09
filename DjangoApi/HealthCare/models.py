from django.db import models
from django.contrib.auth.models import User


class MBloodgroup(models.Model):
    bloodgroupid = models.CharField(db_column='bloodgroupID', primary_key=True, max_length=36)  # Field name made lowercase.
    shortcode = models.CharField(max_length=3)
    description = models.CharField(max_length=255, blank=True, null=True)        
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_bloodg')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_bloodg')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_bloodgroup'


class MBmi(models.Model):
    bmiid = models.CharField(db_column='bmiID', primary_key=True, max_length=36) 
 # Field name made lowercase.
    heightid = models.ForeignKey('MHeight', models.DO_NOTHING, db_column='heightID')  # Field name made lowercase.
    weightid = models.ForeignKey('MWeight', models.DO_NOTHING, db_column='weightID')  # Field name made lowercase.
    bmi = models.FloatField()
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_bmi')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_bmi')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_bmi'


class MGender(models.Model):
    genderid = models.CharField(db_column='genderID', primary_key=True, max_length=36)  # Field name made lowercase.
    shortcode = models.CharField(max_length=1)
    description = models.CharField(max_length=255, blank=True, null=True)        
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_gender')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_gender')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_gender'


class MHeight(models.Model):
    heightid = models.CharField(db_column='heightID', primary_key=True, max_length=36)  # Field name made lowercase.
    height_value = models.FloatField()
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_height')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_height')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_height'


class MWeight(models.Model):
    weightid = models.CharField(db_column='weightID', primary_key=True, max_length=36)  # Field name made lowercase.
    weight_value = models.FloatField()
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_weight')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_weight')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_weight'


class TblUserDetail(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=255)
    userfirstname = models.CharField(max_length=50)
    userlastname = models.CharField(max_length=50)
    user_contact = models.BigIntegerField(unique=True)
    user_dob = models.DateField()
    gender = models.ForeignKey(MGender, models.DO_NOTHING, db_column='gender',related_name='user_gender')   
    height = models.ForeignKey(MHeight, models.DO_NOTHING, db_column='height',related_name='user_height')   
    weight = models.ForeignKey(MWeight, models.DO_NOTHING, db_column='weight',related_name='user_weight')   
    bmi = models.ForeignKey(MBmi, models.DO_NOTHING, db_column='bmi',related_name='user_bmi')
    blood_group = models.ForeignKey(MBloodgroup, models.DO_NOTHING, db_column='blood_group',related_name='user_bloodgroup')
    user_password = models.BinaryField()  # This field type is a guess.
    user_email = models.CharField(unique=True, max_length=100)
    addedby = models.CharField(max_length=36)
    # addedon = models.DateTimeField()
    updatedby = models.CharField(max_length=36, blank=True, null=True)
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tbl_user_detail'

class MLocationDetail(models.Model):
    locationid = models.CharField(db_column='locationID', primary_key=True, max_length=36)  # Field name made lowercase.
    location_pincode = models.IntegerField()
    location_longitude = models.FloatField()
    location_latitude = models.FloatField()
    location_name = models.CharField(max_length=255)
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_loc')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_loc')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_location_detail'

class MEntityType(models.Model):
    entity_typeid = models.CharField(db_column='entity_typeID', primary_key=True, max_length=36)  # Field name made lowercase.
    entity_type = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_Etype')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_Etype')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_type'


class MEntityDetail(models.Model):
    entityid = models.CharField(db_column='entityID', primary_key=True, max_length=36)  # Field name made lowercase.
    entity_typeid = models.ForeignKey('MEntityType', models.DO_NOTHING, db_column='entity_typeID',related_name='Entity_Type')  # Field name made lowercase.
    location = models.ForeignKey('MLocationDetail', models.DO_NOTHING, db_column='location',related_name='Loc')
    entityname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_eDetail')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_eDetail')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_detail'

class MSpeciality(models.Model):
    specialityid = models.CharField(db_column='specialityID', primary_key=True, max_length=36)  # Field name made lowercase.
    speciality = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_speciality')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_speciality')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_speciality'

class MEntitySpeciality(models.Model):
    entity_speciality_id = models.CharField(db_column='entity_speciality_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    entityid = models.ForeignKey(MEntityDetail, models.DO_NOTHING, db_column='entityID',related_name='Eid')  # Field name made lowercase.
    specialityid = models.ForeignKey('MSpeciality', models.DO_NOTHING, db_column='specialityID',related_name='SpecID')  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby',related_name='add_especiality')
    # addedon = models.DateTimeField()
    updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True,related_name='update_especiality')
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    # version = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_speciality'

# class MDoctorDetail(models.Model):
#     dr_id = models.CharField(db_column='dr_ID', primary_key=True, max_length=36)  # Field name made lowercase.
#     entity_speciality = models.ForeignKey('MEntitySpeciality', models.DO_NOTHING, db_column='entity_speciality_ID')  # Field name made lowercase.
#     dr_name = models.CharField(max_length=50)
#     frequency = models.TimeField()
#     addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='addedby')
#     addedon = models.DateTimeField()
#     updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='updatedby', blank=True, null=True)
#     updatedon = models.DateTimeField(blank=True, null=True)
#     active = models.BooleanField()
#     version = models.TextField()  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'm_doctor_detail'

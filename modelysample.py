'''
class MAddresstype(models.Model):
    pk_addresstypeid = models.CharField(db_column='Pk_addressTypeID', primary_key=True, max_length=36)  # Field name 
    addresstype = models.CharField(db_column='addressType', max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_addressType'


class MBloodgroup(models.Model):
    pk_bloodgroupid = models.CharField(db_column='Pk_bloodgroupID', primary_key=True, max_length=36)  # Field name made lowercase.
    shortcode = models.CharField(max_length=3)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_bloodgroup'


class MBmi(models.Model):
    pk_bmiid = models.CharField(db_column='Pk_bmiID', primary_key=True, max_length=36)  # Field name made lowercase. 
    genderid = models.ForeignKey('MGender', models.DO_NOTHING, db_column='genderID', blank=True, null=True)  # Field 
    heightid = models.ForeignKey('MHeight', models.DO_NOTHING, db_column='heightID', blank=True, null=True)  # Field 
    weightid = models.ForeignKey('MWeight', models.DO_NOTHING, db_column='weightID', blank=True, null=True)  # Field 
    bmi = models.FloatField()
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_bmi'



class MDocumentType(models.Model):
    pk_documentid = models.CharField(db_column='Pk_documentID', primary_key=True, max_length=36)  # Field name made lowercase.
    document_type = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_document_type'


class MEntityDetail(models.Model):
    pk_entityid = models.CharField(db_column='Pk_entityID', primary_key=True, max_length=36)  # Field name made lowercase.
    fk_entity_typeid = models.ForeignKey('MEntityType', models.DO_NOTHING, db_column='Fk_entity_typeID', blank=True, null=True)  # Field name made lowercase.
    fk_location = models.ForeignKey('MLocationDetail', models.DO_NOTHING, db_column='Fk_location', blank=True, null=True)  # Field name made lowercase.
    entityname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_detail'


class MEntitySpeciality(models.Model):
    pk_entity_specialityid = models.CharField(db_column='Pk_entity_specialityID', primary_key=True, max_length=36)  # Field name made lowercase.
    fk_entity = models.ForeignKey(MEntityDetail, models.DO_NOTHING, db_column='Fk_entity_ID', blank=True, null=True) 
 # Field name made lowercase.
    fk_specialityid = models.ForeignKey('MSpeciality', models.DO_NOTHING, db_column='Fk_specialityID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_speciality'


class MEntityType(models.Model):
    pk_entity_typeid = models.CharField(db_column='Pk_entity_typeID', primary_key=True, max_length=36)  # Field name made lowercase.
    entity_type = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_type'


class MGender(models.Model):
    pk_genderid = models.CharField(db_column='Pk_genderID', primary_key=True, max_length=36)  # Field name made lowercase.
    shortcode = models.CharField(max_length=1)
    description = models.CharField(max_length=255)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_gender'


class MHeight(models.Model):
    pk_heightid = models.CharField(db_column='Pk_heightID', primary_key=True, max_length=36)  # Field name made lowercase.
    height_value = models.CharField(max_length=6)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_height'


class MLocationDetail(models.Model):
    pk_locationid = models.CharField(db_column='PK_locationID', primary_key=True, max_length=36)  # Field name made lowercase.
    location_pincode = models.IntegerField()
    location_longitude = models.FloatField()
    location_latitude = models.FloatField()
    location_name = models.CharField(max_length=255)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_location_detail'


class MMedicineType(models.Model):
    pk_medicine_typeid = models.CharField(db_column='Pk_medicine_typeID', primary_key=True, max_length=36)  # Field name made lowercase.
    medicine_type = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_medicine_type'


class MNotification(models.Model):
    pk_notificationid = models.CharField(db_column='Pk_notificationID', primary_key=True, max_length=36)  # Field name made lowercase.
    notification_type = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_notification'


class MPayment(models.Model):
    pk_paymentid = models.CharField(db_column='Pk_paymentID', primary_key=True, max_length=36)  # Field name made lowercase.
    payment_method = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_payment'


class MRoleType(models.Model):
    pk_roleid = models.CharField(db_column='Pk_roleID', primary_key=True, max_length=36)  # Field name made lowercase.
    role_type = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_role_type'


class MSpeciality(models.Model):
    pk_specialityid = models.CharField(db_column='Pk_specialityID', primary_key=True, max_length=36)  # Field name made lowercase.
    speciality = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_speciality'


class MStatus(models.Model):
    pk_statusid = models.CharField(db_column='Pk_statusID', primary_key=True, max_length=36)  # Field name made lowercase.
    status_type = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_status'


class MVitalParameter(models.Model):
    pk_vital_paramid = models.CharField(db_column='Pk_vital_paramID', primary_key=True, max_length=36)  # Field name made lowercase.
    shortcode = models.CharField(max_length=10)
    vital_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_vital_parameter'


class MWeight(models.Model):
    pk_weightid = models.CharField(db_column='Pk_weightID', primary_key=True, max_length=36)  # Field name made lowercase.
    weight_value = models.CharField(max_length=6)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_weight'


class TblUserDetail(models.Model):
    pk_userid = models.CharField(db_column='Pk_userID', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(max_length=255)
    user_contact = models.BigIntegerField()
    user_dob = models.DateField()
    fk_height = models.CharField(db_column='Fk_height', max_length=36)  # Field name made lowercase.
    fk_weight = models.CharField(db_column='Fk_weight', max_length=36)  # Field name made lowercase.
    fk_bmi = models.CharField(db_column='Fk_bmi', max_length=36)  # Field name made lowercase.
    fk_blood_group = models.CharField(db_column='Fk_blood_group', max_length=36)  # Field name made lowercase.       
    user_password = models.TextField()  # This field type is a guess.
    user_email = models.CharField(max_length=100)
    addedby = models.CharField(max_length=36, blank=True, null=True)
    addedon = models.DateTimeField()
    updatedby = models.CharField(max_length=36, blank=True, null=True)
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tbl_user_detail'
'''
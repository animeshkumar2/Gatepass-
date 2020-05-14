# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class ApproverReg(models.Model):
    app_id = models.AutoField(primary_key=True)
    # app = models.ForeignKey('Approval', models.DO_NOTHING)
    app_name = models.CharField(max_length=30)
    app_email = models.CharField(max_length=30)
    app_password = models.CharField(max_length=30)
    personal_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'approver_reg'

class Approval(models.Model):
    aid = models.AutoField(primary_key=True)
    source = models.ForeignKey('SourceLocation', models.DO_NOTHING)
    approver_name = models.CharField(max_length=50)
    pers_number = models.IntegerField()
    

    class Meta:
        managed = False
        db_table = 'approval'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gatepass(models.Model):
    oderid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    approval = models.CharField(max_length=50)
    material_id = models.CharField(max_length=50)
    quantity = models.IntegerField()
    courierservice = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gatepass'


class MMaterial(models.Model):
    m_material_id = models.AutoField(primary_key=True)
    m_material_name = models.CharField(max_length=50)
    m_quantity_available = models.CharField(max_length=50)
    m_unit_ofmeasure = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'm_material'


class Material(models.Model):
    mid = models.OneToOneField(MMaterial, models.DO_NOTHING, db_column='mid', primary_key=True)
    material = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unitmeasure = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'material'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    material = models.ForeignKey(Material, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order'


class SourceLocation(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'source_location'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    pno = models.IntegerField()
    email = models.CharField(max_length=40)
    password = models.IntegerField()
    phonenumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Vehicle(models.Model):
    vid = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=30)
    vehicle_no = models.CharField(max_length=30)
    v_trackno = models.CharField(max_length=30)
    s_loc = models.ForeignKey(SourceLocation, models.DO_NOTHING, db_column='s_loc')

    class Meta:
        managed = False
        db_table = 'vehicle'

        
class DestinationLocation(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'destination_location'

class Session(models.Model):
    hello = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'session'
from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin
from polling.forms import *


class PollsAdmin(admin.ModelAdmin):
    # fields = ('hospital_detail','hospital_user_name','api_token_key')
    # fields = "__all__"
    #  list_filter = ('id' )
    # list_display = 'id'
    # search_fields = ('id',)
    form = RegisterSubjectForm


# Hospital subject device registrations

# admin.site.register(HospitalSubjectDeviceRegistration, PollsAdmin)
admin.site.register(HopitalRegistration)
admin.site.register(InsurancePremiumModelling)
admin.site.register(InsuraceOfficeRegistration)
admin.site.register(HospitalSubjectRegistration)
# admin.site.register(HospitalSubjectDeviceRegistration)
admin.site.register(APIContactLogging)
admin.site.register(Insuranceplancategory)
admin.site.register(SensorDeviceType)
admin.site.register(DeviceRegistration)
admin.site.register(PublishSubscribeContact)
admin.site.register(HospitalInsuranceSubjectData)

admin.site.register(CadiacData)

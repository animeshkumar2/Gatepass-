from django.contrib import admin
from .models import SourceLocation
from .models import DestinationLocation
from .models import Approval
from .models import MMaterial
# Register your models here.


admin.site.register(SourceLocation)
admin.site.register(DestinationLocation)
admin.site.register(MMaterial)
admin.site.register(Approval)
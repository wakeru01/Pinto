from django.contrib import admin
from management.models import Zone, User, Member, SeatBooking, TopupLog
# Register your models here.

admin.site.register(Zone)
admin.site.register(User)
admin.site.register(Member)
admin.site.register(SeatBooking)
admin.site.register(TopupLog)

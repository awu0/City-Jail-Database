from django.contrib import admin
from .models import Criminal, Alias, Crime, ProbationOfficer, Sentence, Appeal, CrimeOfficer, Officer, CrimeCharge, \
    CrimeCode

admin.site.register(Criminal)
admin.site.register(Alias)
admin.site.register(Crime)
admin.site.register(ProbationOfficer)
admin.site.register(Sentence)
admin.site.register(CrimeCode)
admin.site.register(CrimeCharge)
admin.site.register(Officer)
admin.site.register(CrimeOfficer)
admin.site.register(Appeal)

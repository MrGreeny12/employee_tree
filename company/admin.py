from django.contrib import admin
from company.models import Company, Department, HighLevelDepartment, DepartmentRelations

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(HighLevelDepartment)
admin.site.register(DepartmentRelations)

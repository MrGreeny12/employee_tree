from django.shortcuts import render
from django.views import View
from company.services import get_correct_format_department_list


class OrganizationChartView(View):
    '''
    Передаёт данные для формирования организационной структуры
    '''
    def get(self, request):
        company, organization_data = get_correct_format_department_list()
        context = {
            'company': company,
            'data': organization_data
        }
        return render(request, 'base.html', context=context)

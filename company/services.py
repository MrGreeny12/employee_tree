from company.models import Company, DepartmentRelations
from employee.models import Employee


def get_correct_format_department_list():
    '''
    Возвращает список формата:
    list = [
        ['Название отдела, руководитель, сотрудники', 'Кому подчиняется', 'Описание']
        ['Название отдела, руководитель, сотрудники', 'Кому подчиняется', 'Описание']
        ['Название отдела, руководитель, сотрудники', 'Кому подчиняется', 'Описание']
        ['Название отдела, руководитель, сотрудники', 'Кому подчиняется', 'Описание']
        ['Название отдела, руководитель, сотрудники', 'Кому подчиняется', 'Описание']
    ], а также экземпляр объекта Компании
    '''
    company = Company.objects.first()
    # беру только первую компанию, потому что не было задачи как-то фильтровать
    correct_format_list = []
    relations = DepartmentRelations.objects.all()
    for relation in relations:
        department = relation.department
        staff = Employee.objects.filter(department=department)
        base_string = f'<b>{department.name}</b><br>'
        for employee in staff:
            if employee.post_type == 'MN':
                manager_name = f'{employee.last_name} {employee.first_name} {employee.patronymic}'
                manager_post = employee.post
                manager = f'{manager_name}<div style="color:red; font-style:italic">{manager_post}</div><br>'
                base_string = (base_string + manager)

            if employee.post_type == 'SB':
                subordinate_name = f'{employee.last_name} {employee.first_name} {employee.patronymic}'
                subordinate_post = employee.post
                subordinate = f'{subordinate_name}<div style="color:red; font-style:italic">{subordinate_post}</div>'
                base_string = (base_string + subordinate)
        first = {
            'v': f'{department.name}',
            'f': base_string
        }
        if relation.high_level_department:
            last = f'{relation.high_level_department}'
        else:
            last = ''
        about = 'Описание отсутствует'
        relation_pack = list()
        relation_pack.append(first)
        relation_pack.append(last)
        relation_pack.append(about)
        correct_format_list.append(relation_pack)

    return company, correct_format_list

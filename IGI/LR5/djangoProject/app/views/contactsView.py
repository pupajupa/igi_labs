from django.views import View
from django.shortcuts import render
from app.services.contactsService import ContactsService
from app.services.employeeService import EmployeeService


class ContactsView(View):
    @staticmethod
    def get(request):
        employees = EmployeeService.get_all()
        return render(request, 'contacts.html',
                      {'role': request.session['role'], 'employees': employees})

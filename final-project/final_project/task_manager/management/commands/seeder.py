from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from task_manager.models import Users


class Command(BaseCommand):
    help = "Roles seeder"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder roles - Started')
        self.__create_roles()
        print('Seeder roles - Finished')
        print('------------------------')
        print('Seeder employees - Started')
        self.__create_employees()
        print('Seeder employees - Finished')
        print('------------------------')
        print('Seeder admin - Started')
        self.__create_admin()
        print('Seeder admin - Finished')

    def __create_roles(self):
        print('Seeder roles - Creating roles')
        roles_data = [
            { 'name': 'Employee' },
            { 'name': 'Admin' },
            ]

        list_roles = []
        for role_data in roles_data:
            try:
                list_roles.append(Group.objects.create(
                        name = role_data['name']
                        ))
            except Exception as e:
                print(f'{role_data["name"]} already exists')
        print('\nList of roles created:')
        for role in list_roles:
            print(f'Role {role.name} created')
        print('\n')

    def __create_employees(self):
        print('Seeder roles - Creating users')
        employee_data = [
            { 'username': 'Antonio', 'email': 'antonio@test.com', 'password': 'contraseña' },
            { 'username': 'Maria', 'email': 'maria@test.com', 'password': 'contraseña' },
            { 'username': 'Carlos', 'email': 'carlos@test.com', 'password': 'contraseña' },
            { 'username': 'Luisa', 'email': 'luisa@test.com', 'password': 'contraseña' }
            ]
        employee_role = Group.objects.get(name = 'Employee')
        list_employee = []
        for employee in employee_data:
            try:
                list_employee.append(Users.objects.create(
                        username = employee['username'],
                        email= employee['email'],
                        password = employee['password']
                        ))
                list_employee[-1].set_password(employee['password'])
                list_employee[-1].save()
                list_employee[-1].groups.add(employee_role)
            except Exception as e:
                print(f'{employee["email"]} already exists')
        print('\nList of users created:')
        for employee in list_employee:
            print(f'Employee {employee.username} created')
        print('\n')

    def __create_admin(self):
        print('Seeder roles - Creating admin')
        admin_data = { 'username': 'Admin', 'email': 'admin@test.com', 'password': 'contraseña' }
        admin = Users.objects.create(
                username = admin_data['username'],
                email = admin_data['email'],
                password = admin_data['password'],
                is_superuser = True
                )
        admin.set_password(admin_data['password'])
        admin.save()
        admin.groups.add(Group.objects.get(name = 'Admin'))
        print('Admin created')


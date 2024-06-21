from django.core.management import BaseCommand


class SeederUsersCommand(BaseCommand):
    help = 'Fill the database with users'

    ROLES_DATA = [
        {'name': 'Client'},
        {'name': 'Chef'},
        {'name': 'Admin'}
        ]
    CHEF_DATA = [
        { 'username': 'gordon', 'email': 'gordon.ramsay@example.com', 'password': 'password123' },
        { 'username': 'jamie', 'email': 'jamie.oliver@example.com', 'password': 'jamie1234' },
        { 'username': 'nigella', 'email': 'nigella.lawson@example.com', 'password': 'nigella5678' },
        { 'username': 'thomas', 'email': 'thomas.keller@example.com', 'password': 'thomas9876' },
        { 'username': 'ina', 'email': 'ina.garten@example.com', 'password': 'ina6543' }
        ]

    CLIENT_DATA = [
        { 'username': 'juan', 'email': 'juan.perez@example.com', 'password': 'juanpass123' },
        { 'username': 'maria', 'email': 'maria.lopez@example.com', 'password': 'maria1234' },
        { 'username': 'carlos', 'email': 'carlos.garcia@example.com', 'password': 'carlos5678' },
        { 'username': 'ana', 'email': 'ana.martinez@example.com', 'password': 'ana9876' },
        { 'username': 'luis', 'email': 'luis.fernandez@example.com', 'password': 'luis6543' }
        ]

    ADMIN_DATA = [
        { 'username': 'admin', 'email': 'admin@mystical.com', 'password': 'mystical' }
        ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Seeder users - Started')
        self.__create_roles()
        self.__create_permissions()
        self.__create_users()
        print('Seeder users - Finished')

    def __create_roles(self):
        print('Seeder users - Creating roles')
        from django.contrib.auth.models import Group
        list_roles = []
        for role_data in self.ROLES_DATA:
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

    def __create_permissions(self):
        print('Seeder users - Defining permissions')
        from django.contrib.auth.models import Permission
        from authentication.models import Users
        from django.contrib.auth.models import Group
        permissions = Permission.objects.all()
        client_role = Group.objects.get(name = 'Client')
        chef_role = Group.objects.get(name = 'Chef')
        admin_role = Group.objects.get(name = 'Admin')
        for permission in permissions:
            admin_role.permissions.add(permission)
            if not permission.content_type.model in ['users', 'group', 'rating', 'permission']:
                chef_role.permissions.add(permission)
            if (not permission.content_type.model in ['users', 'group', 'permission'] and
                    (permission.codename.startswith('view') or permission.content_type.model in ['rating'])):
                client_role.permissions.add(permission)

    def __create_users(self):
        print('Seeder users - Creating users')
        from authentication.models import Users
        from django.contrib.auth.models import Group
        client_role = Group.objects.get(name = 'Client')
        chef_role = Group.objects.get(name = 'Chef')
        admin_role = Group.objects.get(name = 'Admin')

        list_users = []
        for user_data in self.CHEF_DATA:
            try:
                list_users.append(Users.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password']
                        ))
                list_users[-1].groups.add(chef_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in self.CLIENT_DATA:
            try:
                list_users.append(Users.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password']
                        ))
                list_users[-1].groups.add(client_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')

        for user_data in self.ADMIN_DATA:
            try:
                list_users.append(Users.objects.create_user(
                        username = user_data['username'],
                        email = user_data['email'],
                        password = user_data['password'],
                        is_superuser = True
                        ))
                list_users[-1].groups.add(admin_role)
            except Exception as e:
                print(f'{user_data["username"]} already exists')
        print('\nList of users created:')

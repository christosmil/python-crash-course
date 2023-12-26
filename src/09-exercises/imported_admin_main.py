import imported_admin

admin = imported_admin.Admin('bruce', 'wayne', 'bwayne@wayneenterprises.com',
                             'bAtm4n', 'admin')
print(f'{admin.username} has the following privileges:')
admin.user_privileges.show_privileges()
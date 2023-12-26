from multiple_modules_admin import Admin as ADM

admin = ADM('bruce', 'wayne', 'bwayne@wayneenterprises.com', 'bAtm4n', 'admin')
print(f"{admin.username} has the following privileges:")
admin.user_privileges.show_privileges()
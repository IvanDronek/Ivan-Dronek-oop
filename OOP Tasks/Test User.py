import Admin

admin = Admin.Admin("Іван", "Дронек", "18", "dronek.ivan@chnu.edu.ua", 9)
print(admin.priv.show_privileges())

from Admin import Admin, Privileges
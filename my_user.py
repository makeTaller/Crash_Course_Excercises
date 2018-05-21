from Users import Users,Admin,Privileges

#user = Users("kirk","toliver","engineering","chicago","454-343-3234")
#user.describe_user()
#user.greet_user()

adm = Admin("Garvey","Marquis","Engineering","Chicago","774-554-9892")
adm_privileges= ["can delete users", "can access logs", "can lock account"]
adm.privileges.privileges = adm_privileges
adm.privileges.show_privileges()
adm.describe_user()
#adm.privileges.show_privileges()

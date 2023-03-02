########################################################################
#
#  Creator: James Chen
#  Purpose: exercise 5-10
#
########################################################################

current_users = ["Admin", "Jennifer", "James", "Stan", "Grace", "Phil"]

new_users = ["Joe", "Judy", "Jennifer", "Jade", "James"]

lower_current_users = []

for user in current_users:
    lower_current_users.append(user)

for name in new_users:
    if name in lower_current_users:
        print("{} has already been used".format(name))
    else:
        print("{} is available".format(name))

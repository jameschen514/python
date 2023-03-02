usernames = ["admin", "Jinny", "James", "Stan", "Grace", "Phil"]

if "admin" in usernames:
    print("Hello admin, would you like to see a status report")
if "Jinny" in usernames:
    print("Hello Jinny, thank you for logging in again")
if "James" in usernames:
    print("Hello James, thank you for logging in again")
if "Stan" in usernames:
    print("Hello Stan, thank you for logging in again")
if "Grace" in usernames:
    print("Hello Grace, thank you for logging in again")
if "Phil" in usernames:
    print("Hello Phil, thank you for logging in again")

if usernames:
    print("The list is not empty")
else:
    print("The list is empty")
class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False


def auth_decorator(function):
    def wrapper(*args):
        if args[0].logged_in:
            function(args[0])
    return wrapper


@auth_decorator
def post(user):
    print(f"This is {user.name}'s post:\n")


new_user = User("John")
new_user.logged_in = True
post(new_user)

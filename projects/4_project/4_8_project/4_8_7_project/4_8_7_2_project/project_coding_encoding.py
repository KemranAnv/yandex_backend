# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapped():
        initial_dict = func()

        a_name = initial_dict['name']
        b_pass = initial_dict['password']

        # Converting name.
        if len(a_name) > 2:
            new_name = a_name[0] + '*' * (len(a_name) - 2) + a_name[-1]
        elif len(a_name) <= 2:
            new_name = a_name

        # Converting password.
        new_pass = '*' * len(b_pass)

        # return coded_dict
        return {
            'name': new_name,
            'password': new_pass
        }

    return wrapped


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())

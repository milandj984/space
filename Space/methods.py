def login_redirect(string):
    "Ukloni 'login url' i preusmeri na zeljenu adresu"
    new_string = string.replace('user_login/?next=/', '')
    new_string = new_string.replace('/user_login/', '')
    return new_string
from werkzeug.security import generate_password_hash

def setPassword(password):
    print(generate_password_hash(password))

setPassword('12345')


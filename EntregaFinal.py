
import string
from random import *

# Esta función genera una contraseña aleatoria de entre 4 y 16 caracteres
# que puede incluir minúsculas, mayúsculas, números y caracteres especiales.
def generatePassword():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(4, 16)))
    print (password)

generatePassword()






def validar_email(email):
    return "@" in email and "." in email

from util import validar_cpf, validar_email

email = input("Digite seu email: \n")
print("Email válido: ", validar_email(email))

cpf = input("Digite seu cpf: \n")
print("CPF válido: ", validar_cpf(cpf))
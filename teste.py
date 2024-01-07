from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente= Cliente('Felicity Jones','123.456.789-01','felicity@gmail.com','02/09/1987')
angelina: Cliente= Cliente('Angelina Jolie','234.567.890-02','angelina@gmail.com','08/07/1978')

print(felicity)
print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

print(contaf)
print(contaa)
from Conta import Conta
c = Conta()

print(c.getSaldo())
c.depositar(10.50)
print(c.getSaldo())
c.sacar(10)
print(c.getSaldo())
c.sacar(2)
print(c.getSaldo())
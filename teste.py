from conta import Conta

conta = Conta(123, "Kadu", 55.0, 1000.0)
conta2 = Conta(456, "Carlos", 150.0, 2000.0)

conta.extrato()

conta.transfere(50, conta2)

conta.extrato()
conta2.extrato()

conta2.saca(50)
conta2.extrato()

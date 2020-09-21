from conta import cria_conta, deposita, saca, extrato


conta = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta)

deposita(conta, 15.0)
extrato(conta)

saca(conta, 20.0)
extrato(conta)

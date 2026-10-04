def calcula_preco_final(preco_unitario, quantidade):
	### Seu código aqui.
	if quantidade >=1 and quantidade <=5:
		desconto = 0
	elif quantidade >=6 and quantidade <=10:
		desconto = 0.005
	elif quantidade >=11 and quantidade <=20:
		desconto = 0.010
	else:
		desconto = 0.020

	preco = preco_unitario*quantidade
	preco_final = preco -(preco*desconto)								
	return preco_final
print(calcula_preco_final(30,15))
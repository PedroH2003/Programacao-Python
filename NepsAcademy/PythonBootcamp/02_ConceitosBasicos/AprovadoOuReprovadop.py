# Lendo a entrada do exercício
A, B = map(float, input().split())


# Seu código vai aqui
media = (A + B) / 2


if media >= 7.0:
	print("Aprovado")
elif media >= 4.0:
	print("Recuperacao")
else:
	print("Reprovado")
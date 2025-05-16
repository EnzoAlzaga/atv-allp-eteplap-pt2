alunos = {"Ana": 8.5, "Pedro": 7.0, "Maria": 9.2}
alunos["Carlos"] = 6.5
alunos["Ana"] = 9.0
del alunos["Pedro"]

soma_notas = sum(alunos.values())
quantidade_alunos = len(alunos)

media = soma_notas / quantidade_alunos

print("A média é:", media)

if "Maria" in alunos:
    print("Maria está no dicionário.")
else:
    print("Maria não está no dicionário.")
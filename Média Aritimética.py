# Escreva um programa que solicite ao usuário três notas (entre 0 e 10) e calcule a média aritmética dessas notas. Em seguida, exiba a média calculada.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("A média aritmética é", media)
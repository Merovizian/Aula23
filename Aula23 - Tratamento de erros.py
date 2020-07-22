try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except (ValueError, TypeError):
    print("Error no tipo de dados de entrada")
except ZeroDivisionError:
    print("Voce tentou digitar zero no denominador")
except KeyboardInterrupt:
    print("O usuario preferiu não continuar o programa")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {r}")
finally:
    print("Obrigado! Volte sempre")
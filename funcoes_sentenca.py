def identificar_nucle_predicado(frase):
    # Dividir a frase em palavras
    palavras = frase.split()
    
    # Lista de verbos
    verbos = ["é", "são", "está", "estão", "correu", "correm", "corria", "corriam", "andou", "andam", "andava", "andavam", "come", "comem", "comia", "comiam", "foi", "foram", "fui", "fomos", "vai", "vão", "ia", "iam"]
    
    # Lista para armazenar os predicados encontrados
    predicados = []
    
    # Verificar se alguma palavra na frase é um verbo
    for palavra in palavras:
        if palavra.lower() in verbos:
            predicados.append(palavra)
    
    # Retornar a lista de predicados
    if predicados:
        return predicados
    else:
        return "Predicado não encontrado"

# Exemplo de uso
frase = "O cachorro correu até o parque, e o gato andou até a praça."
predicados = identificar_nucle_predicado(frase)
print("Os predicados da frase são:", predicados)

verbos = ["correu", "andou"]
frase = ["o", "cachorro", "correu", "até", "o", "parque"]
final = len(frase)

for palavra in frase:    

    if palavra in verbos:
        verbo_inicio = frase.index(palavra)

    if palavra == ",":
        final = frase.index(palavra)
        break

print(frase[verbo_inicio:final])

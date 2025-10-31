#   AND - Retorna TRUE se amabas as alterações forem verdadeiras
#   OR -  Retorna TRUE se uma das afirmações for verdadeira
#   NOT - Retorna se o resultado for verdadeiro


# TABELA VERDADE AND = "E"
"""
|  A  |  B  | A AND B |
| :-: | :-: | :-----: |
|  V  |  V  |  **V**  |
|  V  |  F  |    F    |
|  F  |  V  |    F    |
|  F  |  F  |    F    |


"""
# TABELA VERDADE OR = "OU"

"""
|  A  |  B  | A OR B |
| :-: | :-: | :----: |
|  V  |  V  |  **V** |
|  V  |  F  |  **V** |
|  F  |  V  |  **V** |
|  F  |  F  |    F   |

"""

# TABELA VERDADE NOT = "NÃO"

"""
|  A  | NOT A |
| :-: | :---: |
|  V  |   F   |
|  F  | **V** |


"""

# OPERADOR AND
numero_1 = 7
numero_2 = 8
# numero_1 e maior que 3 E numero_2 é menor que 8
# retorna True se ambos forem verdadeiras
print(numero_1 > 3 and numero_2 < 8 ) # false


# OPERADOR OR

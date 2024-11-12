# ESTUDAR SOBRE ESSAS FUNCOES
# nome = 'beto'    

# nome.replace
# nome.find
# nome.count
# nome.index
# nome.join
# nome.split
# nome.strip

# chamando a função utilizando o nome declarado // uma função só é utilizada quando for chamada

#funcao p somar dois numeros
def somar(num_a, num_b):                          #Utilize "def" para criar uma função                          
    """_summary_ Funcao para somar dois elementos e retornar o valor da soma

    Returns:
        _type_: somar(4, 5), result = 9 _description_
    """
    return num_a + num_b                           #criar variaveis sempre dentro de funções                    
    # var do tipo local
#funcao p subtrair dois numeros    
def sub(num_a, num_b):                                # PARA ESTILIZAR A FUNCAO UTILIZAR """generateDotString para adicionar informações as funcoes criadas
    """                                     
        funcao que ira subtrair dois valores          

    Args:
        num_a (int): _description_
        num_b (_type_): _description_

    Returns:
        int: retorna a subtracao de dois valores
    """
    return num_a - num_b

result_funcao = somar(30, 50)
print(result_funcao)

result_funcao = sub(50, 25)
print(result_funcao)


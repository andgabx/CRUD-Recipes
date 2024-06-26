# Imports
import os 
import random

########################################
################# CRUD  ################
########################################

# Adicionar
def adicionar_receita() -> None:
    """Função que adiciona uma receita no array."""
    print('Adicionando uma nova receita.')

    while True:
        nome = input('Digite o nome da receita: ')
        if nome or nome.strip() == '':
            break
        print("O nome da receita não pode ser vazio.")

    while True:
        pais = input('Digite o país de origem da receita: ')
        if pais or pais.strip() == '':
            break
        print("O país de origem não pode ser vazio.")

    if input('Esta receita é sua favorita? (sim/não): ') == 'sim':
        favorito=True
    else:
        favorito=False

    while True:
        tempo_de_preparo = input('Digite o tempo de preparo (ex. "20 min"): ').strip()
        if tempo_de_preparo or tempo_de_preparo.strip() == '':
            break
        print("O tempo de preparo não pode ser vazio.")

    ingredientes = []
    print("Digite os ingredientes (digite 'sair' para parar):")
    while True:
        ingrediente = input("Nome do ingrediente: ")
        if ingrediente.lower() == 'sair':
            if ingredientes:
                break
            else:
                print("A lista de ingredientes não pode estar vazia.")
                continue
        if ingrediente:
            ingredientes.append(ingrediente)
        else:
            print("O ingrediente não pode ser vazio.")

    modo_de_preparo = {}
    Passo = 1
    print("Digite o modo de preparo Passo a Passo (digite 'sair' para parar):")
    while True:
        descricao = input(f"Passo {Passo}: ")
        if descricao.lower() == 'sair':
            if modo_de_preparo:
                break
            else:
                print("O modo de preparo não pode estar vazio.")
                continue
        if descricao:
            modo_de_preparo[f'Passo {Passo}'] = descricao
            Passo += 1
        else:
            print("A descrição do passo não pode ser vazia.")

    nova_receita = {
        'nome': nome,
        'pais': pais,
        'favorito': favorito,
        'tempo_de_preparo': tempo_de_preparo,
        'ingredientes': ingredientes,
        'modo_de_preparo': modo_de_preparo
    }

    receitas.append(nova_receita)
    print("Receita adicionada com sucesso!")

# Modificar
def modificar_receita(valor) -> None:
    id_receita=int(valor)
    print(f"Modificando receita: {receitas[id_receita]['nome']}")

    while True:
        novo_nome = input('Digite um novo nome para a receita (deixe em branco para manter): ')
        if novo_nome or novo_nome.strip() == "":
            break
        print("O nome da receita não pode ser vazio.")

    while True:
        novo_pais = input('Digite o novo país de origem da receita (deixe em branco para manter): ')
        if novo_pais or novo_pais.strip() == "":
            break
        print("O país de origem não pode ser vazio.")

    while True:
        novo_tempo_de_preparo = input('Digite o novo tempo de preparo (deixe em branco para manter): ')
        if novo_tempo_de_preparo or novo_tempo_de_preparo.strip() == "":
            break
        print('O tempo de preparo não pode ser vazio.')

    ingredientes = []
    manter_ingredientes=False
    print('Digite os novos ingredientes (digite "sair" no primeiro para manter ou posteriormente para parar):')
    while True:
        ingrediente = input('Nome do ingrediente: ')
        if ingredientes == [] and ingrediente.lower() == 'sair':
            manter_ingredientes=True
            break
        if ingrediente.lower() == 'sair':
            if ingredientes:
                break
            else:
                print('A lista de ingredientes não pode estar vazia.')
                continue
        if ingrediente:
            ingredientes.append(ingrediente)
        else:
            print('O ingrediente não pode ser vazio.')

    modo_de_preparo = {}
    manter_preparo = False
    Passo = 1
    print('Digite o novo modo de preparo Passo a Passo (digite "sair" no primeiro para manter ou posteriormente para parar):')
    while True:
        descricao = input(f"Passo {Passo}: ")
        if modo_de_preparo == {} and descricao.lower() == 'sair':
            manter_preparo = True
            break
        if descricao.lower() == 'sair':
            if modo_de_preparo:
                break
            else:
                print('O modo de preparo não pode estar vazio.')
                continue
        if descricao:
            modo_de_preparo[f'Passo {Passo}'] = descricao
            Passo += 1
        else:
            print('A descrição do passo não pode ser vazia.')

    receitas[id_receita]['nome'] = novo_nome if novo_nome else receitas[id_receita]['nome']
    receitas[id_receita]['pais'] = novo_pais if novo_pais else receitas[id_receita]['pais']
    receitas[id_receita]['tempo_de_preparo'] = novo_tempo_de_preparo if novo_tempo_de_preparo else receitas[id_receita]['tempo_de_preparo']
    if manter_ingredientes == False:
        receitas[id_receita]['ingredientes'] = ingredientes if ingredientes else receitas[id_receita]['ingredientes']
    if manter_preparo == False:
        receitas[id_receita]['modo_de_preparo'] = modo_de_preparo if modo_de_preparo else receitas[id_receita]['modo_de_preparo']

    input(f'Receita "{receitas[id_receita]['nome']}" modificada com sucesso!\nEntre qualquer valor para continuar...')

########################################
########## SALVAR E CARREGAR  ##########
########################################

# Salvar
def salvar() -> None:
    """Salva as receitas em um arquivo chamado receitas.txt na raiz do aplicativo."""
    try:
        file = open('./receitas.txt', 'w+')
        file.write(str(receitas))
    except:
        input('Erro ao criar arquivo!\nPressione enter para continuar.')
    finally:
        try:
            file.close()
        except:
            pass

# Carregar
def carregar() -> list[dict]:
    try:
        file = open("./receitas.txt", "r")
        file_content = eval(file.read())
        return file_content
    except:
        return []
    finally:
        try:
            file.close()
        except:
            pass


########################################
######## FUNÇÕES PARA INTERFACE ########
########################################

# Filtragem por ingrediente
def filtro_ingrediente(filtros:list[str]) -> list[str]:
    """Filtra receitas por ingredientes."""
    resultado = []
    for i in receitas:
        flag = True
        for j in filtros:
            if j not in str(i['ingredientes']):
                flag = False
        if flag:
            resultado.append(i)
    return resultado

# Filtragem por país
def filtro_pais(filtro: str) -> list[str]:
    """Filtra receitas por país."""
    resultado = []
    for i in receitas:
        if i['pais'] == filtro:
            resultado.append(i)
    return resultado

# Filtro de favoritos
def filtro_favoritos() -> list[str]:
    """Filtra receitas por favoritos."""
    resultado = []
    for i in receitas:
        if i['favorito']:
            resultado.append(i)
    return resultado

# Text wrapping
def ui_text_wrap(texto, espacos) -> list[str]:
    """Função de text wrapping para não quebrar a UI."""
    split = texto.split(' ')
    linhas = []
    linha = []
    linha_len = 0
    
    for i in split:
        linha_len += len(i)+1
        if linha_len < espacos:
            linha.append(i+' ')
        else:
            linhas.append(''.join(linha).rstrip())
            linha_len=0
            linha=[]

    return linhas


########################################
########## TELAS DE NAVEGAÇÃO ##########
########################################

# Tela principal
def ui_inicio() -> None:
    """Imprime a tela principal."""

    error=''
    while True:
        os.system('cls')
        print(
            '┎──────────────────────────────────────────────────────────┐\n' +
            '┃ Bem-vindo ao seu repositório de receitas!                │\n' +
            '┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃ (1) Listar suas receitas                                 │\n' +
            '┃ (2) Favoritas                                            │\n' +
            '┃ (3) Filtrar por ingrediente                              │\n' + # Funcionalidade extra
            '┃ (4) Filtrar por país                                     │\n' +
            '┃ (5) Sortear uma receita                                  │\n' +
            '┃ (.) Sair                                                 │\n' +
            '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')
    
        if error!='':
            print(error)
        error=''

        user_input=input()

        match(user_input):
            case '1':
                ui_receitas()
            case '2':
                ui_favoritos()
            case '3':
                ui_ingredientes()
            case '4':
                ui_pais()
            case '5':
                if len(receitas)>1:
                    ui_mostrar_receita(0, [random.choice(receitas)])
                else:
                    error='Não há receitas registradas!'
            case '.':
                return
            case _:
                error=f'Valor inválido! ({user_input})'


# Tela do menu de receitas
def ui_receitas() -> None:
    """Imprime a tela do menu de receitas."""
    mensagem=''
    while True:
        os.system('cls')
        print(
            '┎──────────────────────────────────────────────────────────┐\n' +
            '┃ Suas Receitas                                            │\n' +
            '┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃ (1) Visualizar                │ (4) Remover              │\n' +
            '┃ (2) Adicionar                 │ (.) Retornar             │\n' +
            '┃ (3) Modificar                 │                          │\n' +
            '┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃ Nome                                                     │')
        
        if len(receitas) != 0:
            for i in receitas:
                index = receitas.index(i)
                print(f'┃ {index} {i['nome']}'.ljust(59)+'│')

        else:
            print(
                '┃                 Adicione alguma receita                  │\n' +
                '┃                 para visualizá-la aqui!                  │')
        
        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')
        
        if mensagem!='':
            print(mensagem)
        mensagem=''

        user_input=input()

        match(user_input):
            case '1':
                view=input("Digite o ID da receita que deseja visualizar\n")
                try:
                    ui_mostrar_receita(view, receitas)
                except:
                    mensagem=f'Valor inválido! ({view})'
            case '2':
                adicionar_receita()
                salvar()
            case '3':
                receita_id=input("Digite o ID da receita que deseja modificar!\n")
                try:
                    modificar_receita(receita_id)
                    salvar()
                except:
                    mensagem=f'Valor inválido! ({receita_id})'
            case '4':
                delete=input("Digite o ID da receita que deseja remover\n")
                try:
                    del receitas[int(delete)]
                    salvar()
                    mensagem="Receita removida com sucesso. Pressione enter para continuar."
                except:
                    mensagem=f'Valor inválido! ({delete})'
            case '.':
                return
            case _:
                mensagem=f'Valor inválido! ({user_input})'

# Mostra uma receita em um dado array
def ui_mostrar_receita(index:int, array:list) -> None:
    """Mostra a receita no [index] da [lista] fornecido."""
    erro=''
    save_flag=False
    while True:
        os.system('cls')
        current_recipe = array[int(index)]
        
        print('┎──────────────────────────────────────────────────────────┐')
        print(f'┃ Nome: {current_recipe['nome']}'.ljust(59)+'│')
        print(f'┃ País de origem: {current_recipe['pais']}'.ljust(59)+'│')
        print(f'┃ Tempo de preparo: {current_recipe['tempo_de_preparo']}'.ljust(59)+'│')
        print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥')
        print('┃ Você vai precisar de:                                    │')

        for i in current_recipe['ingredientes']:
            print(f'┃ • {i}'.ljust(59)+'│')

        print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥')

        for i, j in current_recipe['modo_de_preparo'].items():
            print(f'┃ {i}:'.ljust(59)+'│')
            if len(j)>36:
                for i in ui_text_wrap(j, 56):
                    print(f'┃  {i}'.ljust(59)+'│')
            else:
                print(f'┃  {j}'.ljust(59)+'│')        
        print('┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥')

        if current_recipe['favorito']:
            print('┃ (1) Desfavoritar            ┃ (.) Retornar               │')
        else:
            print('┃ (1) Favoritar               ┃ (.) Retornar               │')

        print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')

        if erro!='':
            print(erro)
        erro=''
        
        user_input = input()

        match(user_input):
            case '.':
                if save_flag:
                    salvar()
                return
            case '1':
                if current_recipe['favorito']:
                    current_recipe['favorito'] = False
                else:
                    current_recipe['favorito'] = True
                save_flag=True
            case _:
                erro=f'Valor inválido! ({user_input})'

def ui_favoritos() -> None:
    """Imprime uma tela contendo a lista de receitas favoritadas."""
    erro=''
    while True:
        favoritos = filtro_favoritos()
        os.system('cls')
        print(
            '┎──────────────────────────────────────────────────────────┐\n' +
            '┃ Suas receitas favoritas                                  │\n' +
            '┃ (ID) Visualizar            | (.) Retornar                │\n' +
            '┣━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃  ID  ┃ Nome                                              │')
        
        if len(filtro_favoritos()) != 0:
            for recipe in favoritos:
                index = favoritos.index(recipe)
                print('┃ '.ljust(5-len(str(index))) + f'{index}  ┃' +
                      f' {recipe['nome']}'.ljust(51)+'│')
        else:
            print(
                '┃      ┃           Favorite alguma receita                 │\n' +
                '┃      ┃           para visualizá-la aqui!                 │')
        
        print('┗━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')

        if erro!='':
            print(erro)
        erro=''

        # Retorna uma lista de chars com o range para comparação.
        referencia = list(map(lambda x: str(x), range(len(favoritos))))

        user_input = input()

        match user_input:
            case '.':
                return
            case _:
                if user_input in referencia:
                    ui_mostrar_receita(user_input, favoritos)
                else:
                    erro=f'Valor inválido! ({user_input})'

def ui_ingredientes() -> None:
    """Imprime uma tela para filtragem por ingredientes."""
    error=''
    filtros=[]
    while True:
        os.system('cls')
        print(
            '┎──────────────────────────────────────────────────────────┐\n' +
            '┃ Suas receitas favoritas                                  │\n' +
            '┃ (ID) Visualizar            | (-) Limpar filtros          │\n' +
            '┃ (+) Adicionar filtro       | (.) Retornar                │\n' +
            '┣━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃  ID  ┃ Nome                                              │')
        
        lista_filtrada = filtro_ingrediente(filtros)
        if len(lista_filtrada) != 0:
            for recipe in lista_filtrada:
                index = lista_filtrada.index(recipe)
                print('┃ '.ljust(5-len(str(index))) + f'{index}  ┃' +
                      f' {recipe['nome']}'.ljust(51)+'│')
        else:
            print(
                '┃      ┃       Nenhuma receita para esses filtros!         │\n' +
                '┃      ┃                 Tente novamente!                  │')
        
        print('┗━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')

        if error!='':
            print(error)
        error=''

        # Retorna uma lista de chars com o range para comparação.
        referencia = list(map(lambda x: str(x), range(len(lista_filtrada))))

        user_input=input()

        match user_input:
            case '.':
                return
            case '+':
                filtros.append(input("Que ingrediente você quer usar?\n"))
            case '-':
                filtros=[]
            case _:
                if user_input in referencia:
                    ui_mostrar_receita(user_input, lista_filtrada)
                else:
                    error=f'Valor inválido! ({user_input})'

def ui_pais() -> None:
    """Imprime uma tela contendo a lista receitas de um determinado país."""
    erro=''
    pais = input('Digite o nome do país do qual deseja ver as receitas: ')
    receita_pais = filtro_pais(pais)
    while True:
        
        os.system('cls')
        print(
            '┎──────────────────────────────────────────────────────────┐\n' +
            f'┃ Filtrando receitas por país: {pais}'.ljust(59) + '│\n' +
            '┃ (ID) Visualizar                                          │\n'
            '┃ (.) Retornar                                             │\n' +
            '┣━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥\n' +
            '┃  ID  ┃ Nome                                              │')
        
        if len(filtro_favoritos()) != 0:
            for recipe in receita_pais:
                index = receita_pais.index(recipe)
                print('┃ '.ljust(5-len(str(index))) + f'{index}  ┃' +
                      f' {recipe['nome']}'.ljust(51)+'│')
        else:
            print(
                '┃      ┃     Não há receitas marcadas com esse país!       │\n' +
                '┃      ┃     Verifique o que digitou e tente novamente!    │')
        
        print('┗━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙')

        if erro!='':
            print(erro)
        erro=''

        # Retorna uma lista de chars com o range para comparação.
        referencia = list(map(lambda x: str(x), range(len(receita_pais))))

        user_input = input()

        match user_input:
            case '.':
                return
            case _:
                if user_input in referencia:
                    ui_mostrar_receita(user_input, receita_pais)
                else:
                    erro=f'Valor inválido! ({user_input})'



# Função principal do programa
def main():
    global receitas # Apontando que receitas é global.
    receitas = carregar() # Criando/carregando o arquivo.
    ui_inicio() # Iniciando a UI.
    salvar() # Salva antes de encerrar.

# Carrega a função main()
if __name__=='__main__':
    main()

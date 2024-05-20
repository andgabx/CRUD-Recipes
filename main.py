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
        if nome:
            break
        print("O nome da receita não pode ser vazio.")

    while True:
        pais = input('Digite o país de origem da receita: ')
        if pais:
            break
        print("O país de origem não pode ser vazio.")

    if input('Esta receita é sua favorita? (sim/não): ') == 'sim':
        favorito=True
    else:
        favorito=False

    while True:
        tempo_de_preparo = input('Digite o tempo de preparo (ex. "20 min"): ')
        if tempo_de_preparo:
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
   
########################################
########## SALVAR E CARREGAR  ##########
########################################

# Salvar
def salvar() -> None:
    """Salva as receitas em um arquivo chamado receitas.txt na raiz do aplicativo."""
    try:
        file = open('receitas.txt', 'w+')
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
        file = open("receitas.txt", "r")
        print(__path__(file))
        input()
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
    
# Função principal do programa
def main():
    global receitas # Apontando que receitas é global.
    receitas = carregar() # Criando/carregando o arquivo.
    ui_inicio() # Iniciando a UI.
    salvar() # Salva antes de encerrar.

# Carrega a função main()
if __name__=='__main__':
    main()

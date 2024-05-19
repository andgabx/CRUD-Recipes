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

# Função principal do programa
def main():
    global receitas # Apontando que receitas é global.
    receitas = carregar() # Criando/carregando o arquivo.
    ui_inicio() # Iniciando a UI.
    salvar() # Salva antes de encerrar.

# Carrega a função main()
if __name__=='__main__':
    main()
# Função principal do programa
def main():
    global receitas # Apontando que receitas é global.
    receitas = carregar() # Criando/carregando o arquivo.
    ui_inicio() # Iniciando a UI.
    salvar() # Salva antes de encerrar.

# Carrega a função main()
if __name__=='__main__':
    main()
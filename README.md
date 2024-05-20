## Manual do Usuário: Sistema de Gerenciamento de Receitas

## Índice

1. [Descrição](#1-descrição)
2. [Funcionalidades](#4-funcionalidades)
    - [Adicionar Receitas](#41-adicionar-receitas)
    - [Modificar Receita](#42-modificar-receita)
    - [Carregar e Salvar Receitas](#44-carregar-e-salvar-receitas)
    - [Filtragem de Receitas](#45-filtragem-de-receitas)
3. [Progresso Atual](#5-progresso-atual)

## 1. Descrição 

Este sistema de gerenciamento de receitas permite aos usuários adicionar, modificar, carregar, salvar e filtrar receitas. Ele proporciona uma plataforma onde usuários podem compartilhar, armazenar e organizar suas criações culinárias, garantindo uma experiência prática e eficiente.

## 2. Funcionalidades

### 2.1. 🍰 Adicionar Receitas

A funcionalidade "Adicionar Receitas" permite aos usuários inserir novas receitas no sistema, expandindo a base de dados de receitas.

#### Funcionamento:

1. **Entrada de Dados:**
    - O usuário insere informações sobre a receita, incluindo:
        - Nome da receita
        - Lista de ingredientes
        - Instruções de preparo
        - Tempo de preparo
        - País da receita

2. **Processamento:**
    - O sistema valida os dados inseridos e armazena a receita no banco de dados.

3. **Saída de Dados:**
    - Uma mensagem de confirmação é exibida ao usuário e a nova receita torna-se acessível na lista de receitas.

#### Exemplo de Uso

```python
nova_receita = {
    "nome": "Bolo de Chocolate",
    "ingredientes": ["2 xícaras de farinha", "1 xícara de açúcar", "1/2 xícara de cacau em pó", "2 ovos", "1 xícara de leite"],
    "instrucoes": "Misture todos os ingredientes e asse em forno pré-aquecido a 180°C por 30 minutos.",
    "tempo_preparo": "15 minutos",    
    "pais": "nome do pais"
}
```

### 2.2. 🛠️ Modificar Receita

Permite aos usuários editar informações de uma receita existente, essencial para corrigir erros ou atualizar detalhes.

#### Funcionamento:

1. **Seleção da Receita:**
    - O usuário seleciona a receita a partir de uma lista existente.

2. **Entrada de Dados:**
    - O usuário edita os campos desejados.

3. **Processamento:**
    - O sistema valida e aplica as alterações.

4. **Saída de Dados:**
    - Uma mensagem de confirmação é exibida e a receita atualizada é refletida na lista.

#### Exemplo de Uso

```python
modificacao = {
    "nome": "Bolo de Chocolate com Cobertura",
    "ingredientes": ["2 xícaras de farinha", "1 xícara de açúcar", "1/2 xícara de cacau em pó", "2 ovos", "1 xícara de leite", "Cobertura de chocolate"],
    "instrucoes": "Misture todos os ingredientes e asse em forno pré-aquecido a 180°C por 30 minutos. Adicione a cobertura depois de assado.",
    "tempo_preparo": "15 minutos",
    "pais": "nome do pais"
}
```

### 2.3. 💾 Carregar e Salvar Receitas

Permite aos usuários armazenar e recuperar receitas de um banco de dados ou arquivo.

#### Funcionamento:

1. **Inicialização:**
    - O sistema carrega todas as receitas ao iniciar a aplicação.

2. **Processamento:**
    - As receitas são lidas e convertidas em objetos utilizáveis.

3. **Disponibilização:**
    - As receitas são exibidas na interface do usuário.

#### Salvar Receitas

1. **Acionamento do Salvamento:**
    - O sistema aciona o processo de salvamento ao adicionar ou modificar uma receita.

2. **Processamento:**
    - A receita é convertida e gravada no banco de dados ou arquivo.

3. **Confirmação:**
    - Uma mensagem confirma que a receita foi salva com sucesso.


### 2.4. 🔍 Filtragem de Receitas

Permite aos usuários buscar e visualizar receitas com base em critérios específicos.

#### Funcionamento:

1. **Entrada de Critérios de Filtragem:**
    - O usuário insere os critérios de filtragem desejados.

2. **Processamento:**
    - O sistema aplica os critérios de filtragem e realiza uma busca.

3. **Saída de Dados:**
    - As receitas que atendem aos critérios são exibidas ao usuário.

#### Exemplo de Uso

```python
def filtrar_receitas(receitas, categoria=None, tempo_preparo_max=None, ingrediente=None):
    receitas_filtradas = []
    
    for receita in receitas:
        if categoria and receita["categoria"] != categoria:
            continue
        if tempo_preparo_max and receita["tempo_preparo"] > tempo_preparo_max:
            continue
        if ingrediente and ingrediente not in receita["ingredientes"]:
            continue
        receitas_filtradas.append(receita)
    
    return receitas_filtradas
```

## 3. Progresso Atual

Lista de requisitos:

- [x] Adicionar receitas
- [x] Modificar receitas
- [x] Editar receitas
- [x] Carregar e salvar receitas
- [x] Filtragem de receitas
- [x] Validação e persistência de dados

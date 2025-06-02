# Projeto 1: Reconhecedor de Gramáticas

**Disciplina:** GRULFAT - Linguagens Formais e Autômatos  
**Curso:** Bacharelado em Engenharia de Computação  
**Instituição:** Instituto Federal de São Paulo - Campus Guarulhos

## Integrantes da Equipe

- Fernanda Barbosa da Silva - GU3045242  
- Gisele C.S.S. Medeiros - GU3046176  
- Natalia da Silva Tavares - GU3047008  
- Renan de Paula Paz Oliveira - GU3046478  

---

## Descrição do Projeto

Este programa tem como objetivo reconhecer e validar a especificação de uma gramática formal, conforme as regras definidas no documento `GRULFAT_Projeto 1.pdf`. Ele realiza verificações como:

- Estrutura correta das regras gramaticais
- Separação adequada entre lados esquerdo e direito
- Uso apropriado de símbolos terminais e não-terminais

---

## Instruções de Execução

### 1. Pré-requisitos

- Python 3.x instalado no sistema

### 2. Estrutura de Arquivos

Certifique-se de que os seguintes arquivos estejam no mesmo diretório:

- `reconhecedor.py` (programa principal)
- `gramatica.txt` (arquivo de entrada com a gramática)

> ⚠️ **Importante:** O nome do arquivo de entrada **deve ser obrigatoriamente** `gramatica.txt`.

### 3. Execução via Linha de Comando

Abra o terminal ou prompt de comando, navegue até o diretório onde estão os arquivos e execute:

```bash
python reconhecedor.py gramatica.txt


## Formato da Entrada (`gramatica.txt`)

O arquivo `gramatica.txt` deve seguir rigorosamente as seguintes regras:

- A gramática deve estar escrita **em uma única linha**.
- A linha deve terminar com o caractere especial `$`, que indica o fim da entrada.
- As produções devem seguir o formato estabelecido.

### Exemplo de entrada válida:

```txt
S>AB;A>a;B>b;$

S, A, B    → não-terminais  
a, b       → terminais  
>          → separa lado esquerdo e direito de uma produção  
;          → separa diferentes produções  
$          → indica o fim da definição gramatical



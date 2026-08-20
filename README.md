# 🐍 Fundamentos de Python

Este repositório apresenta conceitos fundamentais da linguagem **Python**, com exemplos práticos para quem está começando no desenvolvimento de sistemas.

Os principais conceitos abordados são:

* Variáveis
* `print()`
* f-strings
* `if`
* `elif`
* `else`

---

## 📚 Conteúdos

1. [Variáveis](#-variáveis)
2. [Print](#-print)
3. [F-Strings](#-f-strings)
4. [Estrutura if](#-if)
5. [Estrutura elif](#-elif)
6. [Estrutura else](#-else)
7. [Exemplo completo](#-exemplo-completo)

---

## 📦 Variáveis

Uma **variável** é um espaço utilizado para armazenar um valor que pode ser utilizado posteriormente pelo programa.

Em Python, não é necessário declarar previamente o tipo da variável.

### Exemplo

```python
nome = "Carlos"
idade = 25
altura = 1.75
```

Nesse exemplo:

* `nome` armazena uma string (`str`)
* `idade` armazena um número inteiro (`int`)
* `altura` armazena um número decimal (`float`)

Podemos verificar o tipo de uma variável utilizando `type()`:

```python
nome = "Carlos"

print(type(nome))
```

Saída:

```text
<class 'str'>
```

### 🧠 Regra importante

O operador `=` é utilizado para **atribuição**:

```python
idade = 25
```

Isso significa:

> A variável `idade` recebe o valor `25`.

---

## 🖨️ Print

A função `print()` é utilizada para **exibir informações no terminal**.

### Exemplo

```python
print("Olá, mundo!")
```

Saída:

```text
Olá, mundo!
```

Também podemos imprimir o conteúdo de uma variável:

```python
nome = "Carlos"

print(nome)
```

Saída:

```text
Carlos
```

Podemos imprimir vários valores:

```python
nome = "Carlos"
idade = 25

print(nome, idade)
```

Saída:

```text
Carlos 25
```

---

## 🧵 F-Strings

As **f-strings** facilitam a criação de textos que precisam apresentar valores armazenados em variáveis.

Para utilizar uma f-string, colocamos a letra `f` antes das aspas e usamos `{}` para inserir as variáveis.

### Exemplo

```python
nome = "Carlos"
idade = 25

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Saída:

```text
Meu nome é Carlos e tenho 25 anos.
```

### Por que utilizar f-strings?

Sem f-string:

```python
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")
```

Com f-string:

```python
print(f"Meu nome é {nome} e tenho {idade} anos.")
```

A segunda opção é mais simples e legível.

---

## 🔀 If

O `if` é utilizado para executar um determinado bloco de código **quando uma condição for verdadeira**.

### Exemplo

```python
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
```

Como `20 >= 18` é verdadeiro, o programa executará o `print()`.

### Estrutura básica

```python
if condição:
    # código executado caso a condição seja verdadeira
```

### ⚠️ Atenção à indentação

Python utiliza **indentação** para definir quais comandos pertencem a uma estrutura.

Correto:

```python
if idade >= 18:
    print("Maior de idade")
```

Incorreto:

```python
if idade >= 18:
print("Maior de idade")
```

---

## 🔄 Elif

O `elif` significa aproximadamente **"senão, se"**.

Ele permite verificar uma nova condição quando a condição anterior do `if` não foi satisfeita.

### Exemplo

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
elif idade >= 13:
    print("Adolescente")
```

Como `idade >= 18` é falso, Python verifica a condição do `elif`.

Saída:

```text
Adolescente
```

Podemos utilizar vários `elif`:

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
```

Saída:

```text
Bom
```

---

## 🔴 Else

O `else` é utilizado quando **nenhuma das condições anteriores foi verdadeira**.

### Exemplo

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Saída:

```text
Menor de idade
```

O `else` não possui uma condição própria.

Ele representa o **caso contrário**.

---

## 🔀 Combinando if, elif e else

Podemos utilizar as três estruturas juntas para criar uma tomada de decisão.

```python
nota = 6

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Aprovado")
else:
    print("Reprovado")
```

Nesse caso:

* `nota >= 9` → Excelente
* `nota >= 7` → Bom
* `nota >= 5` → Aprovado
* qualquer outro valor → Reprovado

---

## 🚀 Exemplo completo

Agora podemos combinar **variáveis, `print()`, f-string, `if`, `elif` e `else`** em um único programa:

```python
nome = "Ana"
idade = 20
nota = 8.5

print(f"Olá, {nome}!")
print(f"Você tem {idade} anos.")
print(f"Sua nota foi {nota}.")

if nota >= 9:
    print("Resultado: Excelente!")
elif nota >= 7:
    print("Resultado: Bom!")
elif nota >= 5:
    print("Resultado: Aprovado!")
else:
    print("Resultado: Reprovado!")
```

Saída:

```text
Olá, Ana!
Você tem 20 anos.
Sua nota foi 8.5.
Resultado: Bom!
```

---

## 🧠 Resumo

| Conceito   | Função                                                |
| ---------- | ----------------------------------------------------- |
| Variável   | Armazena informações                                  |
| `print()`  | Exibe informações no terminal                         |
| `f-string` | Facilita a inserção de variáveis em textos            |
| `if`       | Executa código quando uma condição é verdadeira       |
| `elif`     | Verifica outra condição                               |
| `else`     | Executa quando nenhuma condição anterior é verdadeira |

---

## 🎯 Próximos passos

Depois de dominar esses conceitos, os próximos assuntos recomendados são:

* Operadores matemáticos
* Operadores de comparação
* Operadores lógicos (`and`, `or`, `not`)
* Entrada de dados com `input()`
* Listas
* Tuplas
* Dicionários
* Laços `for` e `while`
* Funções
* Tratamento de exceções

> 💡 **Dica:** A melhor maneira de aprender programação é praticar. Modifique os exemplos, altere os valores das variáveis e observe como o comportamento do programa muda.

---

## 📌 Objetivo do projeto

Este material tem como objetivo servir como uma introdução prática aos fundamentos da programação em Python, proporcionando uma base para o desenvolvimento de aplicações e sistemas mais complexos.

**Bons estudos e boas linhas de código! 🐍💻**

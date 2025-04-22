Estruturas condicionais são blocos de código que permitem tomar decisões com base em condições específicas. Elas são fundamentais em qualquer linguagem de programação, pois possibilitam alterar o fluxo da execução dependendo de valores ou situações.

---

## principais tipos:

### **1. `if` (se)**
Executa um bloco de código **se** uma condição for verdadeira.

**Exemplo em Python:**
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
```

---

### **2. `if`...`else` (se...senão)**
Permite definir um caminho alternativo **caso a condição não seja verdadeira**.

```python
idade = 16
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

---

### **3. `elif` (senão se)**
Serve para testar **várias condições** em sequência. É uma abreviação de “else if”.

```python
nota = 75

if nota >= 90:
    print("Aprovado com excelência.")
elif nota >= 60:
    print("Aprovado.")
else:
    print("Reprovado.")
```

---

### **4. Condicional ternária**
É uma forma curta de escrever um `if...else`.

```python
idade = 20
status = "maior" if idade >= 18 else "menor"
print(f"Você é {status} de idade.")
```

---

Essas estruturas também existem em outras linguagens (como JavaScript, C, Java etc.) com variações na sintaxe, mas a lógica é a mesma.

---

## Exercícios:
**Execício 1.** Construa um programa que leia a categoria de um produto e determine o preço, conforme a tabela abaixo:

| Categoria | Preço |
|-----------|-------|
| 1         | 10,00 |
| 2         | 18,00 |
| 3         | 23,00 |
| 4         | 26,00 |
| 5         | 31,00 |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex1.py)

---

**Execício 2.** Construa um programa que leia dois números e pergunte ao usuário qual operação ele deseja executar: soma, subtração, multiplicação ou divisão. Após a operação o programa deve exibir o resultado do processamento.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex2.py)

---

**Execício 3.** Construa um programa bancário para aprovação de empréstimos. O programa deve receber o valor do empréstimo solicitado, o salário do cliente e a quantidade de meses para se pagar o empréstimo. O valor da prestação mensal não pode ultrapassar 30% do salário. O programa deve considerar o valor da prestação como sendo o valor solicitado dividido pela quantidade de meses.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex3.py)

---

**Execício 4.** Desenvolva um programa que leia a altura (em metros) e o peso (em quilogramas) e calcule o IMC - Índice de Massa Corporal do usuário e informe sua situação corporal conforme tabela abaixo. O cálculo do IMC é feito dividindo-se o peso pela altura ao quadrado. Sabe-se ainda que a tabela abaixo é válida apenas para pessoas acima dos 15 anos de idade, então o programa deverá invalidar os cálculos que fujam dessa regra.

| RESULTADO          | SITUAÇÃO                |
|--------------------|-------------------------|
| Abaixo de 17       | Muito abaixo do peso    |
| Entre 17 e 18,49   | Abaixo do peso          |
| Entre 18,5 e 24,99 | Peso normal             |
| Entre 25 e 29,99   | Acima do peso           |
| Entre 30 e 34,99   | Obesidade I             |
| Entre 35 e 39,99   | Obesidade II (severa)   |
| Acima de 40        | Obesidade III (mórbida) |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex4.py)

---

**Execício 5.** A CEF concederá um crédito especial com juros de 2% aos seus clientes de acordo com o saldo médio no último ano. Fazer um algoritmo em Python que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. Imprimir uma mensagem informando o saldo médio e o valor de crédito.

| Saldo Médio    | Percentual                  |
|----------------|-----------------------------|
| De 0 a 500     | Nenhum crédito              |
| De 501 a 1000  | 30% do valor do saldo médio |
| De 1001 a 3000 | 40% do valor do saldo médio |
| Acima de 3000  | 50% do valor do saldo médio |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex5.py)

---

**Execício 6.** Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação segundo a seguinte tabela:

- maior de idade;
- menor de idade;
- pessoa idosa (idade superior ou igual a 65 anos).

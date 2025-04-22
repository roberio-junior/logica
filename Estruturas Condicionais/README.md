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

**Execício 6.** Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação:

- maior de idade;
- menor de idade;
- pessoa idosa (idade superior ou igual a 65 anos).

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex6.py)

---

**Execício 7.** Crie um algoritmo em Python que leia a idade de uma pessoa e informe a sua classe eleitoral:

- Não eleitor (abaixo de 16 anos);
- Eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
- Eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex7.py)

---

**Execício 8.** A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um algoritmo em Python que receba a idade de um nadador e determine (imprima) a sua categoria segundo a tabela a seguir:

| Categoria  | Idade              |
|------------|--------------------|
| Infantil A | 5 – 7 anos         |
| Infantil B | 8 – 10 anos        |
| Juvenil A  | 11 – 13 anos       |
| Juvenil B  | 14 – 17 anos       |
| Sênior     | Maiores de 18 anos |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex8.py)

---

**Execício 9.** Depois da liberação do governo para as mensalidades dos planos de saúde, as pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um algoritmo em Python que entre com a idade de uma pessoa e imprima o valor que ela deverá pagar, segundo a seguinte tabela:

| Idade                   | Valor     |
|-------------------------|-----------|
| Até 10 anos             | R$ 30,00  |
| Acima de 10 até 29 anos | R$ 60,00  |
| Acima de 29 até 45 anos | R$ 120,00 |
| Acima de 45 até 59 anos | R$ 150,00 |
| Acima de 59 até 65 anos | R$ 250,00 |
| maior que 65 anos       | R$ 400,00 |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex9.py)

---

**Execício 10.** Escreva um algoritmo em Python que leia as notas das unidades de um aluno e determine a média das notas semestral. Através da média calculada o algoritmo deve imprimir a seguinte mensagem: “Aprovado”, “Reprovado” ou em “Quarta Prova” (a média é 7 para "Aprovação", menor que 3 para "Reprovação" e as demais em "Quarta Prova").

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex10.py)

---

**Execício 11.** Dado três valores, A, B e C, construa um algoritmo em Python para verificar se estes valores podem ser valores dos lados de um triângulo. 

> "Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo)* da diferença dos outros dois lados e menor que a soma dos outros dois lados."

| b - c | < a < b + c |

| a - c | < b < a + c |

| a - b | < c < a + b |

***Utilize a função abs() para encontrar um módulo de um número.***

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex11.py)

---

**Execício 12.** Dado três valores, A, B e C, construa um algoritmo em Python para verificar se estes valores podem ser valores dos lados de um triângulo, e se for, se é um triangulo escaleno, um triangulo equilátero ou um triangulo isósceles.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex12.py)

---

**Execício 13.** Criar um algoritmo em Python que receba o valor de x, e calcule e imprima o valor de f(x).

| f(x)          | Condição   |
|---------------|------------|
| 1             | x <= 1     |
| 2             | 1 < x <= 3 |
| x ao quadrado | 2 < x <= 3 |
| x ao cubo     | x  > 3     |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex13.py)

---

**Execício 14.** Construa um algoritmo em Python para determinar a situação (APROVADO / QUARTA PROVA / REPROVADO) de um aluno, dado a sua freqüência (porcentagem de 0 a 100%) e sua nota (nota de 0.0 a 10.0), sendo que:

| Condição                                            | Situação  |
|-----------------------------------------------------|-----------|
| Freqüência até 75%                                  | Reprovado |
| Freqüência entre 75% e 100% e Nota até 3.0          | Reprovado |
| Freqüência entre 75% e 100% e Nota de 3.0 até 7.0   | 4ª Prova  |
| Freqüência entre 75% e 100% e Nota entre 7.0 e 10.0 | Aprovado  |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex14.py)

---

**Execício 14.** Escreva um algoritmo em Python que leia as notas das unidades de um aluno e sua frequência (porcentagem de 0 a 100%). Através da média calculada e da frequência, o algoritmo deve determinar a situação (APROVADO / QUARTA PROVA / REPROVADO).

| Condição                                                                          | Situação  |
|-----------------------------------------------------------------------------------|-----------|
| Freqüência até 75%                                                                | Reprovado |
| Freqüência entre 75% e 100% e média até 3.0                                       | Reprovado |
| Freqüência entre 75% e 100% e média de 3.0 até 7.0 e notas inferiores a 3.0.      | Reprovado |
| Freqüência entre 75% e 100% e média de 3.0 até 7.0 e notas acima ou iguais a 3.0. | 4ª Prova  |
| Freqüência entre 75% e 100% e média entre 7.0 e 10.0                              | Aprovado  |

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/logica/blob/main/Estruturas%20Condicionais/ex15.py)

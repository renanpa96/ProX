# Operadores em JavaScript

### - Operadores são símbolos que sinalizam para o nosso interpretador de JavaScript a operação que desejamos realizar com nossos dados
    Exemplo: O sinal de + entre dois números sinaliza que desejamos somá-los

```javascript
const resultado = 237 + 512;
```


### - Existem alguns tipos de operadores (símbolos que indicam uma operação). O sinal *+* é um exemplo de um operador aritmético, e a lista de todos desse tipo segue abaixo:
| Operador 	| Descrição                      	|
|----------	|--------------------------------	|
| +        	| Adição                         	|
| -        	| Subtração                      	|
| *        	| Multiplicação                  	|
| /        	| Divisão                        	|
| **       	| Exponenciação (ou Potenciação) 	|
| %        	| Resto da divisão (Modulus)     	|
| ++       	| Incremento                     	|
| --       	| Decremento                     	|

```javascript
const resultado = 2**3; //aqui estamos fazendo 2³ e guardando o total na variável "resultado"

const restoDivisao = 29%7; //a variável restoDivisao está recebendo o número 1, que é o resto da divisão de 29 por 7
```

#### - *Apesar de operações aritméticas serem operações entre números, as vezes o JavaScript nos permite realizá-las com outros tipos de dados*

```javascript
const texto1 = 'Olá, bom dia! ';
const texto2 = 'Hoje é um ótimo dia para aprender a programar!';

const textoResultante = texto1 + texto2; //textoResultante está sendo inicializado com o texto 'Olá, bom dia! Hoje é um ótimo dia para aprender a programar!'
```



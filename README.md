# Dataclass vs TypedDict vs NamedTuple

Código-fonte ministrado na aula do Youtube: [https://www.youtube.com/watch?v=lQVaviQHfvg](https://www.youtube.com/watch?v=lQVaviQHfvg)

## TypedDict

Introduzido na versão 3.8.

O TypedDict é uma classe que representa um dicionário com um conjunto de chaves e valores tipados. Ele é uma alternativa ao uso de dicionários comuns, que não garantem que as chaves e valores tenham os tipos corretos (não faz validação de tipos).

O uso de dicionários aninhados com chaves de strings para representar objetos ou dados estruturados é comum em programas Python. Este padrão é especialmente relevante na manipulação de objetos JSON, ao ponto de Python incluir uma biblioteca para JSON. Este PEP propõe uma forma de melhorar a checagem de tipos para tal código.

Em termos gerais, usar tipos primitivos do Python como dicionários, strings e listas para representar objetos de dados puros tem suas vantagens. Eles são fáceis de serializar e desserializar, mesmo sem JSON, e suportam operações úteis como impressão formatada, iteração e comparações de igualdade sem esforço adicional.

O tipo Dict pode ser usado para representar objetos de dados puros, no entanto, tem uma desvantagem significativa: a falta de checagem de tipos. O tipo Dict não pode expressar a estrutura de um objeto de dados puro, e o Python não pode verificar se um objeto de dados puro é válido em tempo de execução. Isso pode levar a erros difíceis de depurar, especialmente em código grande e complexo. Além de definir um tipo `Dict[str, Any]` ou `Dict[str, Union[int, str]]`, não há uma maneira padrão de expressar a estrutura de um objeto de dados puro em Python.

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
```


### Acessar valores

Para acessar os valores de um TypedDict, você pode usar a notação de colchetes ou o método get.

```python
person = Person(name='Alice', age=30)

print(person['name'])  # Alice
print(person.get('age'))  # 30
```

### Restrições

### &rarr; Não suporta valores default.

```python

from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int = 30

person = Person(name='Alice')
person['age']  # TypeError: TypedDict 'Person' has no key 'age'
person.get('age')  # None
```


### &rarr; Não suporta métodos personalizados.

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

    def greet(self):
        return f'Hello, my name is {self["name"]}'

person = Person(name='Alice', age=30)
person.greet()  # AttributeError: 'Person' object has no attribute 'greet'
```

## NamedTuple

Introduzido na versão 3.6.

O NamedTuple é uma classe que representa uma tupla com um conjunto de campos nomeados. Ele é uma alternativa ao uso de tuplas comuns, que não garantem que os campos tenham os tipos corretos (não faz validação de tipos).

Este tipo é imutável e pode ser usado para criar objetos de dados puros. Ele é uma alternativa ao uso de classes comuns, que são mutáveis e podem ter métodos personalizados.

O uso de memória é mais eficiente do que o uso de classes comuns, pois o NamedTuple é uma tupla otimizada. Ele é uma alternativa ao uso de dicionários, que são menos eficientes em termos de uso de memória.

O tipo Tuple pode ser usado para representar objetos de dados puros, no entanto, tem uma desvantagem significativa:  a falta de checagem de tipos. O tipo Tuple não pode expressar a estrutura de um objeto de dados puro, e o Python não pode verificar se um objeto de dados puro é válido em tempo de execução. Isso pode levar a erros difíceis de depurar, especialmente em código grande e complexo. Além de definir um tipo Tuple com tipos primitivos do Python, não há uma maneira padrão de expressar a estrutura de um objeto de dados puro em Python.

```python

from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
```

### Acessar valores

Para acessar os valores de um NamedTuple, você pode usar a notação de ponto ou a notação de colchetes.

```python
person = Person(name='Alice', age=30)

print(person.name)  # Alice
print(person[0])  # Alice
print(person.age)  # 30
print(person[1])  # 30
```


### Restrições

### &rarr; Não suporta mudança de valores.

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

person = Person(name='Alice', age=30)
person.name = 'Bob'  # AttributeError: can't set attribute
```

Mas, com o método `_replace`, você pode criar uma nova instância com valores diferentes.

```python
person = person._replace(name='Bob')
print(person)  # Person(name='Bob', age=30)
```

### &rarr; Herança limitada.

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

class Employee(Person):
    salary: float

employee = Employee(name='Alice', age=30, salary=1000.0) # TypeError: __new__() got an unexpected keyword argument 'salary'
```


## Dataclass

Introduzido na versão 3.7.

O Dataclass é uma classe que representa um objeto de dados puro. Ele é uma alternativa ao uso de dicionários e NamedTuples. Ele melhora a tipagem dos dados da classe e é uma excelente alternativa ao uso de classes comuns.

Ele interfere nos métodos `__init__`, `__repr__`, `__eq__`, `__hash__` e `__str__` de uma classe, já criando esses métodos automaticamente.

Ele permite a adição de recursos como slots e imutabilidade, que são úteis para otimizar o uso de memória e garantir que os objetos sejam imutáveis.

Também é possível converter um objeto dataclass em tuplas e dicionários, o que é útil para serialização e desserialização de objetos.

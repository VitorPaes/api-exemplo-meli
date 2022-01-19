# api-exp-meli
## Api feita em Flask

API consistem em 3 endpoints
* /all
  * Consiste em trazer via metodo GET todos os resultados existentes no banco de dados da tabela items
* /find/{id}
  * Consiste em trazer via metodo GET as informações de um unico produto da tabela items
* /save
  * Adiciona uma nova linha a tabela de items pelo metodo POST. Abaixo exemplo de como se deve enviar o Json
  ~~~json
  {
    "title": "Exemplo",
    "price": 745.3,
    "initial_quantity": 555,
    "available_quantity": 8994,
    "sold_quantity": 1669,
    "condition": "Exemplo"
   }
  ~~~
## Modo de execução
### Requisitos
* python3
 * pip
* docker
#### Passo 1
* Iniciar o docker
* Acessar o dir {sua-rota-aqui}/api-exemplo-meli
* Executar o comando para criar o ambiente virtual
~~~shell
python3 -m venv $(pwd)
cd bin
.\Scripts\Activate.ps1
~~~
* Executar o comando para baixar a dependencias
~~~shell
pip install -r requirements.txt
~~~
#### Passo 2
* Com o docker EM EXECUÇÃO executar o comando (aguarde finalizar)
~~~shell
docker-compose up
~~~
* Execute o arquivo insert_data.py (exibira uma msg no terminal com a qtd de linha existente na tabela)
~~~shell
python insert_data.py
~~~
* Execute o arquivo app.py (entrara em execução o servidor no ip (http://127.0.0.1:5000/)
~~~shell
flask run
~~~


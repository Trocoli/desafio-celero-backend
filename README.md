DESAFIO CELERO
=================
_DESCRIÇÃODOPROJETO_

## [](#considera%C3%A7%C3%B5es-iniciais)Considerações Iniciais

Essas instruções serão necessárias para configuração e execução do projeto em sua maquina local para desenvolvimento e possíveis casos de testes. Antes de tudo, visualize o arquivo abaixo sobre como você realizará a configuração do projeto para execução oficial.

### [](#pr%C3%A9-requisitos)Pré-requisitos

_EXEMPLO DE REQUERIMENTOS BÁSICOS PARA UMA APLICAÇÃO, É INTERESSANTE QUE AO LADO DA TECNOLOGIA, INFORME A SUA VERSÃO._

```
- Python==3.9.7
- Django==4.0.3
- djangorestframework==3.13.1 
```

### [](#instalando)Instalando

É necessário ter instalado em sua máquina o Python 3.9.7 ou superior que é disponibilizado no site oficial do Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)). Antes de finalizar confira em suas Variações de Ambiente do Windows e verifique que o Python encontra-se configurado em sua "path". Posteriormente, tem-se necessário criar e configurar a sua própria máquina virtual de desenvolvimento para que as ferramentas de projeto não se instalem em suas respectivas máquinas permanentemente.

```
	Criar a virtual enviroment:
		--> python -m venv (nomeDaEnviroment)
	Ativar a enviroment criada:
		--> (nomeDaEnviroment)/Scripts/activate
	Instalar o requirements.txt:
	    --> pip install -r requirements.txt
	Atualizar as migrações do banco de dados:
	    --> python manage.py makemigrations
	Construir o banco de dados da aplicação:
	    --> python manage.py migrate
```

## [](#executando-os-testes)Executando os testes

Para executar os testes. Será necessário alguns passos a mais, seguem abaixo a sequência dos mesmos:

```
	Acessar a pasta do projetos:
		--> cd PASTADOPROJETO
	Executar o arquivo manage.py:
		--> python manage.py runserver
	Abrir o navegador e acessar o link de localhost:
		--> localhost:8000
```
	O teste dos endpoints é feito através de requests feitos preferencialmetne através do POSTMAN,
		Ao entrar no postman é necessário utilizar os endpoints com o método certo e enviar o request

## [](#utilizando-app)Endpoints

```
	Para popular o banco de dados é necessário fazer o download do arquivo [csv] '120 years of olympic history'(https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
	Criação manual e listagem de atletas:
		--> [POST] 'https://localhost:8000/athletes':
			permite a criação do atleta enviando através do body um JSON com:
				 Nome do atleta,
				 Sexo,
				 Altura,
				 Peso,
				 Time,
		--> [GET] 'https://localhost:8000/athletes':
			Exibe a lista de todos os atletas inseridos 
		
		--> [GET] 'https://localhost:8000/athletes':
			Exibe a lista de todos os atletas inseridos 

		--> [GET] 'https://localhost:8000/athletes':
			Exibe a lista de todos os atletas inseridos 

		--> [GET] 'https://localhost:8000/athletes':
			Exibe a lista de todos os atletas inseridos 




```

## [](#constru%C3%ADdo-com)Construído com

-   [Comic Sans](http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900) - Fonte utilizada no sistema.
-   [JQuery](http://code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css) - Dependencias do sistema
-   [Bootstrap](https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css) - Design do sistema
-   [Popper](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js) - Runs like AJAX (Pop-up's)

## [](#autor)Autor

-   **Ygor Trócoli** - _Desenvolvedor Back-End_ - [@vini192](https://github.com/Trocoli)

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
	Para popular o banco de dados é necessário fazer o download do arquivo 
    csv: '120 years of olympic history' 
    disponível em: https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    e inserindo um método de [POST] através do postman 
    --> [POST] ' https://localhost:8000/populate/':
            enviar o arquivo csv baixado com nome e tipo 'file' através do body -> Form Data

	Criação manual e listagem de atletas:
		--> [POST] 'https://localhost:8000/athletes':
			permite a criação do atleta enviando através do body um JSON com:
				 'name',
				 'sex',
				 'height',
				 'weight',
				 'team',
		--> [GET] 'https://localhost:8000/athletes/':
			Exibe a lista de todos os atletas inseridos 
		
		--> [GET] 'https://localhost:8000/athletes/':
			Exibe a lista de todos os atletas inseridos 

		--> [GET] 'https://localhost:8000/{id_do_atleta_/)':
			Exibe detalhes de atleta com o ID que foi passado no request

		--> [PATCH] 'https://localhost:8000/update/athletes/':
			Permite o update do atleta com o ID que foi passado no request

		--> [DELETE] 'https://localhost:8000/update/athletes/':
			Permite o update do atleta com o ID que foi passado no request
        
    Criação de objeto de olimíadas:
    		--> [POST] 'https://localhost:8000/olympics/':
			permite a criação da Olimpíada enviando através do body um JSON com:
				 'year':
				 'season': (Summer ou Winter),
				 'city',
            --> [GET] 'https://localhost:8000/olympics/':
                lista todos os jogos olimpicos cadastrados
            
            --> [GET, PATCH or DELETE]  'https://localhost:8000/olympics/{{olympic_id}}':
                    permite exibir detalhes, editar ou deletar uma olimpíada 

    Criação de objeto de evento olímpíco :
    		--> [POST] 'https://localhost:8000/events/':
			permite a criação do evento olímpico enviando através do body um JSON com:
				 'event_name':
				 'sport_name': 
				 'athletes': (lista com ID dos atletas),
                 'olympic_game': (ID de olimpiada relacionada a evento)

            --> [GET] 'https://localhost:8000/events/':
                lista todos os eventos cadastrados
            
    		--> [GET] 'https://localhost:8000/events/{id_do_evento/)':
			Exibe detalhes do evento com o ID que foi passado no request

		    --> [PATCH] 'https://localhost:8000/events/update/{{id}}':
			Permite o update do evento com o ID que foi passado no request

		    --> [DELETE] 'https://localhost:8000/events/update/{{id}}':
			Permite o update do evento com o ID que foi passado no request

    Inserção de medalhas:
    		--> [POST] 'https://localhost:8000/medals/':
			permite a criação da medalha enviando através do body um JSON com:
				 'event_name': (chave estrangeira com ID do evento relacionado),
				 'olympic_game': (chave estrangeira com ID da olimpíada relacionada),
				 'athlete': (chave estrangeira com ID do atleta ganhador da medalha),
                 'medal_type': (Gold, Silver ou Bronze)

            --> [GET] 'https://localhost:8000/olympics/':
                lista todas as medalhas cadastradas
            
            --> [GET, PATCH or DELETE]  'https://localhost:8000/medals/{{medal}}':
                    permite exibir detalhes, editar ou deletar uma medalha 
            





```

## [](#constru%C3%ADdo-com)Construído com

-   [Comic Sans](http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900) - Fonte utilizada no sistema.
-   [JQuery](http://code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css) - Dependencias do sistema
-   [Bootstrap](https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css) - Design do sistema
-   [Popper](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js) - Runs like AJAX (Pop-up's)

## [](#autor)Autor

-   **Ygor Trócoli** - _Desenvolvedor Back-End_ - [@vini192](https://github.com/Trocoli)

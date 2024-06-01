# Embrapa API

## Required technologies

* [Python] - Python in version >= 3.7.4
* [SQLite3] - Database
#
## Python packages manager
* [UV] - uv is and extremely fast Python package and resolver.
* [Pip] - Simple python packager manager
#

## Clone project

```sh
$ git clone https://github.com/luigus/embrapa-api.git
```

#
## Setup project
#### You can setup the project using uv with pip.

#### Using pip and virtualenv
```sh
$ cd embrapa-api/
$ python -m venv .venv -p python3.7
$ source .venv/bin/activate
$ uv pip install -r requirements.txt
```

#
## Database
#### Database already have all data from Embrapa inside the tables
If you want to check the table names, please, run this SQL query command below:

```sh
$ SELECT name FROM sqlite_master WHERE type='table';
```

#### Tables start with Imp (means Importacao), tables starts with Exp (means Expertacao), tables starts with Processa (means Processamento)
#
### List of tables inside database
| name 			   
| ------ 			 			
| Producao
| Comercio
| ProcessaViniferas
| ProcessaSemclass
| ProcessaMesa
| ProcessaAmericanas
| ImpVinhos
| ImpSuco
| ImpPassas
| ImpFrescas
| ImpEspumantes
| ExpVinho
| ExpUva
| ExpSuco
| ExpEspumantes


#
## Run FastAPI Web App
#### You need to have the environment enabled
```sh
$ cd embrapa-api/
$ python -m uvicorn main:app --reload
```

#### The following list of links will be available after the project starts
* http://localhost:8000/docs
* http://localhost:8000//producao/{year}
* http://localhost:8000//comercio/{year}
* http://localhost:8000//processa/{type}/{year}
* http://localhost:8000//importacao/{type}/{year}
* http://localhost:8000//exportacao/{type}/{year}

#{year} could be beetween 1970 and 2023


## API
| API 				   | METHOD 	| ENDPOINTS 				| Type   			 
| ------ 			   | ------ 	|------ 			   		|------
| Producao     		   | GET 		| producao/{year} 	        |
| Comercio             | GET 		| comercio/{year} 	        |
| Processamento        | Get 		| processa/{type}/{year}    | mesa, americanas, viniferas, semclasse
| Importacao           | Get 		| importacao/{type}/{year}  | suco, passas, vinho, frescas, espumantes
| Exportacao           | Get 		| exportacao/{type}/{year}  | suco, uva, espumantes


#### Exemples of endpoints
* http://localhost:8000/docs
* http://localhost:8000//producao/2020
* http://localhost:8000//comercio/2019
* http://localhost:8000//processa/mesa/2021
* http://localhost:8000//importacao/suvo/2018
* http://localhost:8000//exportacao/uva/2017




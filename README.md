For this ETL project, I wanted to extract data from a .data file and send it to a Postgres or SQlite database instance.
I decided to use **Postgres in a dockerized environment**.

And to interact with this database, I created a structure in the Django Rest Framework (DRF), where some routes are provided to perform the creations of the records in the DB.

Initially I analyzed how the data was coming from the Jupyter Notebook and after a first idea, I outlined which plans to use.
![alt text](https://github.com/Bereoff/etl_project/blob/main/images/df_jupyter.png "previous data analysis")

From the description file, I identified what type of data was expected by each field in the data source (Adult.data) and followed with verification treatments. For example, if the field "age" contained only numerical values, otherwise I would create some strategy with that record.
![alt text](https://github.com/Bereoff/etl_project/blob/main/images/df_regex_jupyter.png "check data consistency according to field")

And so on for all the other fields.

I performed batch ingestions of 1630 records every 10s, and had to think of a strategy to guarantee the state (the point where it stopped). 
![alt text](https://github.com/Bereoff/etl_project/blob/main/images/desev_jupyter.png "function for batch data")
And to solve this, besides the model that would receive the data sent from the data source (CensusEtl), to the DRF, I created another model to store a counter (Counter) and be able to identify the starting point for the new load, access the endpoints and send a post to the bank.
![alt text](https://github.com/Bereoff/etl_project/blob/main/images/testes_jupyter.png "payload sent in the post of the data in the bank")

To run the routine of ingesting the data into the bank, I created a script that is a command within the Django framework that performs the ingest according to the batch size and with the desired time and that needs to be triggered manually.

About the execution steps to run the project

* clone the repository

* python -m venv

* pip install -r requirements

* docker-compose up -d

* python manage.py migrate

And the project is ready to use.

After these steps you need to start the server with:
* python manage.py runserver 8001

And to perform the ingest of the data into the database:
* python manage.py ETL_Django

And for a quick delete on the two models (CensusEtl and Counter)
* python manage.py delete_models

The endpoints created are:
* http://localhost:8001/admin/ (Admin DRF)
* http://localhost:8001/api/v1/census-etl/ (CensusEtl)
* http://localhost:8001/api/v1/census-etl/counter (Counter)

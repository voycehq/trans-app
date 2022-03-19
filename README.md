# ROR Trans-app
ROR-Trans App is an online AI-driven web base application that seeks to facilitate the
process on how Rhapsody translation is being done in a much faster rate so as to reach
more people for Jesus. This application seeks to target all men regardless of the linguistic
constraints.

## Architecture
![Architecture](https://user-images.githubusercontent.com/42831769/158949952-6692ec32-7226-4637-8983-3fd094868789.png)

### Set up db migration

1. The first thing to do is to install the alembic database migration package.

```  
pip install alembic  
```  

2. Copy all details from **"alembic.example.ini"** to a new file called **"alembic.ini"**

```  
cp -b alembic.example.ini alembic.ini  
```  

3. Edit **"line 43"** from **"alembic.ini"** file with *key=sqlalchemy.url* with your sqlalchemy database url details for the project.
4. You are now good to go.

- Creating database migrations

strikethrough textBelow are the various processes to follow through to create a db migration after we update any database schema.

- Synchronize migrations **heads** pointer with your local database

```  
alembic stamp heads
```  

- Create a revision file

> Here we are going to create a revision migration file with our changes on our database schema structure.  
The command below creates a migration file with the message *"revision message"*

```  
alembic revision --autogenerate -m "revision message"  
```  

> The command below creates a migration file with an empty message.

```  
alembic revision --autogenerate  
```  

- Write changes to database

> Here we are going to perform the updates in our database.

```  
alembic upgrade head  
```  

- Listing out all alembic migration IDs

> The command below will provide us with all the history of all migrations performed with their unique revision id.

```  
alembic history  
```  

- Dropping all db tables

> The command below will reset our database state to the base alembic revision id.

```  
alembic downgrade base  
```  

- Downgrade to a specific alembic migration ID

> The command below will reset the database state to a given alembic revision state.

```  
alembic downgrade <migration-id>  
```  

- To more about alembic migration package.
To find out more about the alembic migration package and how it can be used, follow the link below.

* [Alembic Official Documentation](https://alembic.sqlalchemy.org/en/latest/)
- [Some Overviews](https://docs.google.com/document/d/1KPcFklHJ9prHKy0VxS3HvymkuyYu0BxqmbrIEQmx5RI/edit?usp=sharing)

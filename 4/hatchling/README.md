# Hatchling

The following is a toy micro-blog built to demonstrate an organized and scalable
"two tier" architecture for `Flask` applications.

## Organization

````
1. Controller
      |
2. DAO / Model
      |
3. Database
````

## Environment Variables 
Make sure your environment has the following environment variables setup.  To check if these variables are set, run 
`echo $VARIABLE_NAME`:

```bash
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=mysql://localhost/hatchling_db
export HATCH_DB_USER=CHANGE_ME
export HATCH_DB_PASS=CHANGE_ME
export HATCH_DB_NAME=hatchling_db
```

## Setup

1. Follow the directions to setup the dependencies for these [`demos`](https://github.com/Cornell-PoBE/demos#setup)
2. Install `MySQL`
3. Create a database in `MySQL`: `mysql> CREATE DATABASE hatchling_db;`
4. `cd` into the root of the app (`./hatchling`)
5. Run `./setup`

## Running
In the root (`./hatchling`):

```bash
python src/run.py
```

In a differnet terminal window, you can run the `client.py` script to setup an interface for interacting with the server:

```bash
python client.py
Type in a command, either:
CREATE content:<content> author:<author>
GET page:<page> page_size:<page_size>
```

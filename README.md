Dev Notebook
============

Version 1.0 of this app is live! [https://devbase.herokuapp.com](https://devbase.herokuapp.com)

# Stack
* Django 4.0.4
* PostgreSQL 9.x
* Gulp 3.9.1
* Vue.js 2.x
* Bulma

# Set up
* Clone this repository: `git clone https://github.com/choww/dev-notebook.git`
* Enter the directory: `cd dev-notebook`
* Run `npm install`
* Create a Postgres database called `dev_notebook`
* From the project's root directory: 
    * Run `source env/bin/activate`
    * Switch to the `app` directory
    * Create a secrets.py and assign the variables `db_user` and `db_pw` to your postgres username & password
    * Run migrations: `python manage.py makemigrations` and `python manage.py migrate`

# Run the website
* Make sure the virtual environment is activated: `source env/bin/activate`
* Switch to the `app` directory from the root directory of the project
* Run `python manage.py runserver`

# Deploy

## First time set up

Install python build pack
```sh
heroku create --buildpack https://github.com/heroku/heroku-buildpack-python.git
```

Add `runtime.txt` to the root of the project and specify the [Python version](https://devcenter.heroku.com/articles/python-runtimes)

Deploy: 
```
git push heroku main
```

# Contact
* carmenchow@protonmail.com

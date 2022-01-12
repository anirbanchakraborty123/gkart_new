# gkart-(A simple ecommerce web-application) using GITHUB ACTIONS- CI/CD PIPELINES- AWS 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app 
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages testenv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(testenv)$ pip install -r requirements.txt
```
Note the `(testenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(testenv)$ cd project
(testenv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

coming soon....

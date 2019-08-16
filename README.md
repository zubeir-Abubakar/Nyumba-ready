# Homex
This is an application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User stories

The user should be able to:

+ [x] Sign in with the application to start using.
+ [x] Set up a profile about me and a general location and my neighborhood name.
+ [x] Find a list of different businesses in my neighborhood.
+ [x] Find Contact Information for the health department and Police authorities near my neighborhood.
+ [x] Create Posts that will be visible to everyone in my neighborhood.
+ [x] Change My neighborhood when I decide to move out.
+ [x] Only view details of a single neighborhood.

## Prerequisites
+ [x] Python3.6

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/zubeyr-Abubakar/Nyumba-ready.git
    $ cd Hood
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```
## How to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```
## Demo

<!-- This is the live link to Hood [Click here](https://hood-murage-homex.herokuapp.com) -->

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

### Contact Information

To reach me, email me at: > muragemaina09@gmail.com

## License
This project is licensed under the MIT Open Source license, (c)

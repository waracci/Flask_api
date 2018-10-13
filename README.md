# Flask API
## Introduction

> Badges here

## Run in Postman

> Not linked yet

### Features

1. Users can create cart. (GET)
2. Users can post a cart. (POST)
3. Users can delete a cart they posted. (DELETE)
4. Users can edit a cart details. (PUT)


### Installing

*Step 1*

Create directory
```$ mkdir Flask_api```

```$ cd Flask_api```

create a .env file

``` touch .env```
``` using the .env_example as an example, add details to the .env file```

Create and activate virtual environment

```$ virtualenv env -p python3```


```$ source env/bin/activate```

Clone the repository [```here```](https://github.com/waracci/Flask_api) or 

``` git clone https://github.com/waracci/Flask_api ```

Install project dependencies 


```$ pip install -r requirements.txt```


*Step 2* 

#### Set up database and virtual environment & Database 

``` No database setup required```

*Step 3*

#### Storing environment variables 

```
environment variables are stored in .env file
```

*Step 4*

#### Running the application

```$ flask run```

*Step 5*

#### Testing

```$ python manage.py run_tests```

### API-Endpoints

#### Cart Endpoints : /api/v1/cart

Method | Endpoint | Functionality
--- | --- | ---
POST | /api/v1/cart | Create a cart
GET | /api/v1/cart | Get all carts
GET | /api/v1/cart/cart_id | Get a single cart
PUT | /api/v1/cart/cart_id | Edit details of a cart
DELETE | /api/v1/cart/cart_id | Delete a cart

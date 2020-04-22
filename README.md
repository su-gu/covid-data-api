# covid-data-api
This will scape the data from the government site and provide the consumable json data about the state-wise corona cases

This project uses Django and graphql for API.

To consume this API, send a GET request at:
https://statewisecovidindia.herokuapp.com/graphql/?query={stateWiseData}

[GraphQL](https://statewisecovidindia.herokuapp.com/graphql) playground is available



# To run this project locally: 
* Step 1 
Install pipenv 
`pip install pipenv` 
* Step 2 
In the root of this project, start the virtualenv
`pipenv shell`
* Step 3 
Install all the required packages
`pipenv install`

All the packages are installed. Time to run the Django server.

* Step 4
In the root directory(where `manage.py` recides) run,
`python manage.py runserver`

* Step 5
After the server is running, you can go-to 
`localhost/graphql` to open the graphql playground.

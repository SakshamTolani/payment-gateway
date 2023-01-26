# PAYMENT GATEWAY WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.9.6
- Django 4.1.5
- Django REST Framework 3.14.0

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `orders`, so we will use the following URLS - `/api/` and `/api/<order_id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/` | GET | READ | Get all orders
`api/:order_id/` | GET | READ | Get order by order-id
`api/createOrder/`| POST | CREATE | Create a new order
`api/:order_id/paymentStatus/` | GET | READ | Get Payment Details by order-id
`api/:order_id/paymentStatus/success/` | PUT | UPDATE | Update payment to success using order-id
`api/:order_id/paymentStatus/failure/` | PUT | UPDATE | Update payment to failure using order-id

### Commands
```
Get all orders
http http://127.0.0.1:8000/api/
Get order by order-id
http GET http://127.0.0.1:8000/api/{order_id}/
Create a new order
http POST http://127.0.0.1:8000/api/createOrder/ "order_id":"ORD265", "order_amount":2000, "customer_name":"Spiderman"
Get Payment Details by order-id
http GET http://127.0.0.1:8000/api/{order_id}/paymentStatus/ 
Update payment to success using order-id
http PUT http://127.0.0.1:8000/api/{order_id}/paymentStatus/success/
Update payment to failure using order-id
http PUT http://127.0.0.1:8000/api/{order_id}/paymentStatus/failure/ 
```

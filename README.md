# Libro: E-commerce REST API

A REST API for an online shop, built with Django REST Framework. It covers products, reviews, user accounts and orders, with JWT authentication.

## Features

- **Products:** list, view, create, update and delete products with name, brand, category (computer, food, home, kids), price, stock and rating
- **Filtering and pagination** on the product list with `django-filter`
- **Reviews:** signed-in users can rate and review a product, and the product's average rating is updated
- **Accounts:** sign up, get the current user, update your profile
- **Orders:** place an order with several items and a shipping address, list your orders, view or delete one
- **Order processing:** admins can change an order's status (processing, shipped, delivered)
- Payment status and method on each order (cash on delivery by default)
- JWT authentication with `djangorestframework-simplejwt`
- Custom JSON responses for 404 and 500 errors

## API

All endpoints are under `/api/`.

| Method | Endpoint | Auth | Description |
| --- | --- | --- | --- |
| POST | `/api/register/` | – | Create an account |
| POST | `/api/token/` | – | Get a JWT access and refresh token |
| GET | `/api/userinfo/` | JWT | Current user |
| PUT | `/api/userinfo/update/` | JWT | Update the current user |
| GET | `/api/products/` | – | List products (filters, pagination) |
| GET | `/api/products/<id>/` | – | One product with its reviews |
| POST | `/api/products/new/` | JWT | Create a product |
| PUT | `/api/products/update/<id>/` | JWT | Update a product |
| DELETE | `/api/products/delete/<id>/` | JWT | Delete a product |
| POST | `/api/products/<id>/review` | JWT | Add or update your review |
| DELETE | `/api/products/<id>/review/delete` | JWT | Delete your review |
| POST | `/api/orders/new/` | JWT | Place an order |
| GET | `/api/orders/` | JWT | List orders |
| GET | `/api/orders/<id>/` | JWT | One order |
| PUT | `/api/orders/<id>/process/` | Admin | Change the order status |
| DELETE | `/api/orders/<id>/delete/` | JWT | Delete an order |

Send the token as `Authorization: Bearer <access token>`.

## Built with

- Python 3, Django 5.1, Django REST Framework 3.15
- `djangorestframework-simplejwt`, `django-filter`
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/LIBRO_REST_DJANGO.git
cd LIBRO_REST_DJANGO
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
cd main
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API is then at http://127.0.0.1:8000/api/.

## Project structure

```
main/
  main/      Settings and root URLs
  product/   Products, reviews, filters
  account/   Sign up and user info
  order/     Orders and order items
  utils/     Custom error handlers
```

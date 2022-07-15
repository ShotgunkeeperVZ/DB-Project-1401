# DB-Project-1401

## Cart
  delivery_method for now is consist of "P" and "V" meaning post and vip <br>

# Order
  state is consist of "P", "C", "F" meaning pending, complete and failed <br>

## Available URLs
  localhost:8000/store/products <br>
  localhost:8000/store/products/id <br>
  localhost:8000/store/products/id/reviews <br>
  localhost:8000/store/products/id/reviews/id <br>

  localhost:8000/store/customers/ <br>
  localhost:8000/store/customers/me <br>
  localhost:8000/store/customers/id/ <br>

  localhost:8000/store/carts <br>
  localhost:8000/store/carts/id <br>
  localhost:8000/store/carts/id/cartitems <br>
  localhost:8000/store/carts/id/cartitems/id <br>
  
  localhost:8000/store/orders <br>
  localhost:8000/store/orders/id <br>
  localhost:8000/store/orders/id/orderitems <br>
  localhost:8000/store/orders/id/orderitems/id <br>
  
  localhost:8000/auth/user <br>
  localhost:8000/auth/user/me <br>
  
  localhost:8000/auth/jwt/create <br>
  localhost:8000/auth/jwt/refresh <br>

## Docker
start: docker-compose up -d --build <br>
check logs: docker-compose logs <br>
stop: docker-compose down -v <br>
database volume is saved in ./data <br>

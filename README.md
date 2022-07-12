# DB-Project-1401

## Available URLs
  localhost:8000/store/products <br>
  localhost:8000/store/products/id <br>
  localhost:8000/store/products/id/review <br>
  localhost:8000/store/products/id/review/id <br>

  localhost:8000/store/customers/ <br>
  localhost:8000/store/customers/me <br>
  localhost:8000/store/customers/id/ <br>
  
  localhost:8000/auth/user <br>
  localhost:8000/auth/user/me <br>
  
  localhost:8000/auth/jwt/create <br>
  localhost:8000/auth/jwt/refresh <br>

## Docker
start: docker-compose up -d --build <br>
check logs: docker-compose logs <br>
stop: docker-compose down -v <br>
database volume is saved in ./data <br>

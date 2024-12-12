# API Gateway

This API Gateway is a single entry point for various microservices. It forwards incoming requests to the appropriate backend service based on the requested route.

## Features

- **Single Endpoint Access**: Access multiple microservices (`users`, `subscriptions`, `vehicles`, `service`, `damages`, `invoice`) through a single gateway.
- **Flexible Routing**: The gateway handles different HTTP methods (GET, POST, PUT, DELETE) and forwards requests to the corresponding microservice endpoints.
- **Authorization Propagation**: Passes the `Authorization` header from the client request directly to the target service.
- **Easy to Extend**: Add new services by updating the `SERVICE_URLS` dictionary.

## Microservices

The gateway provides access to these services:

- **Users**: `/users` - User authentication and management  
- **Subscriptions**: `/subscriptions` - Manage subscriptions  
- **Vehicles**: `/vehicles` - Vehicle-related operations  
- **Service**: `/service` - Vehicle service management  
- **Damages**: `/damages` - Damage management for vehicles  
- **Invoice**: `/invoice` - Invoice management and payments

## Endpoints

- **`GET /`**  
  Lists available services and their endpoints.
  
- **`POST /login`**  
  Forwards the login request to the `users` service (`/login` endpoint).
  
- **`/<service>/<path:endpoint>`**  
  Routes requests to the specified `service` and `endpoint`.  
  For example, `GET /vehicles/list` will be forwarded to the `vehicles` service at `https://vehicle-service-.../list`.

- **`/<service>/`**  
  Access the root endpoint of a specific service (e.g., `GET /users/` will fetch the root of the `users` service).

## Usage

1. **Install Dependencies**  
   ```bash
   pip install Flask requests
   ```

2. **Run the Gateway**  
   ```bash
   python app.py
   ```
   The gateway will start on `http://localhost:5000`.

3. **Send Requests**  
   Use tools like `curl`, `Postman`, or `HTTPie` to send requests:
   ```bash
   # Get a list of all services
   curl http://localhost:5000/

   # Forward a GET request to the vehicles service
   curl http://localhost:5000/vehicles/list
   ```

   Include `Authorization` headers if required by the backend services:
   ```bash
   curl http://localhost:5000/vehicles/list \
   -H "Authorization: Bearer <your_token>"
   ```

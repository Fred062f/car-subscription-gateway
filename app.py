from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

# Microservice URLs
SERVICE_URLS = {
    "users": "https://users-service-fkgvgpfscqa3cjg8.northeurope-01.azurewebsites.net",
    "subscriptions": "https://subscription-service-bxffbmd0bydahpeu.northeurope-01.azurewebsites.net",
    "vehicles": "https://vehicle-service-fwdhc6gzavcgagd4.northeurope-01.azurewebsites.net",
    "service": "http://localhost:5004",
    "damages": "http://localhost:5005",
    "invoice": "https://invoice-service-b4a7cgbqgtejgpdw.northeurope-01.azurewebsites.net"
}

@app.route('/')
def index():
    """Route to display the available services."""
    services = {
        "services": [
            {"name": "Users", "endpoint": "/users", "description": "User authentication and management"},
            {"name": "Subscriptions", "endpoint": "/subscriptions", "description": "Manage subscriptions"},
            {"name": "Vehicles", "endpoint": "/vehicles", "description": "Vehicle-related operations"},
            {"name": "Service", "endpoint": "/service", "description": "Service management for vehicles"},
            {"name": "Damages", "endpoint": "/damages", "description": "Damage management and vehicles"},
            {"name": "Invoice", "endpoint": "/invoice", "description": "Invoice management and payments"}
        ]
    }
    return jsonify(services)

@app.route('/login', methods=['POST'])
def login():
    response = requests.post(f"{SERVICE_URLS['users']}/login", json=request.json)
    if response.status_code == 200:
        return Response(
            response=response.text,
            status=response.status_code,
            headers=dict(response.headers)
        )
    return response.text, response.status_code, response.headers.items()

@app.route('/<service>/<path:endpoint>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_request(service, endpoint):
    if service not in SERVICE_URLS:
        return jsonify({"error": "Service not found"}), 404

    headers = {
        "Authorization": request.headers.get("Authorization")
    }
    method = request.method
    url = f"{SERVICE_URLS[service]}/{endpoint}"
    
     # Check if the request has a valid JSON body
    if request.is_json:
        data = request.json
    else:
        data = None

    if method == "GET":
        response = requests.get(url, headers=headers, params=request.args)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, json=data)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers)

    return (response.text, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(debug=True, port=5000)

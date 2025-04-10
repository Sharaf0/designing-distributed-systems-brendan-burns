# HTTP to HTTPS Sidecar Example

This example demonstrates the **sidecar pattern** to add HTTPS support to a legacy HTTP application without modifying its source code. The setup includes:

1. **Legacy HTTP Application**: A containerized Node.js application serving HTTP requests on `localhost:8080`.
2. **Nginx Sidecar**: A containerized Nginx instance acting as a reverse proxy, terminating HTTPS traffic and forwarding it to the legacy application over HTTP.

## Problem Statement

Many legacy applications were built without HTTPS support, which is now a security standard. Modifying such applications to support HTTPS can be challenging due to outdated build systems or unavailable source code. The **sidecar pattern** provides a solution by introducing a proxy container to handle HTTPS traffic while leaving the legacy application unchanged.

## Solution Overview

- The **legacy application** serves HTTP traffic on `localhost:8080` and is not exposed externally.
- The **Nginx sidecar** terminates HTTPS traffic on port `443` and proxies requests to the legacy application over the local network.
- This ensures secure communication externally while keeping the internal setup simple.

## Directory Structure

```
http-to-https/
├── legacy-app/
│   ├── Dockerfile.legacy
│   └── server.js
├── nginx-sidecar/
│   ├── Dockerfile.nginx
│   └── nginx.conf
└── docker-compose.yml
```

## How to Run

1. **Build and Start the Services**:
   ```bash
   docker-compose up --build
   ```

2. **Access the Application**:
   - Open your browser and navigate to `https://localhost`.
   - You will see the response from the legacy application: `Hello, this is the legacy HTTP application!`

3. **Stop the Services**:
   ```bash
   docker-compose down
   ```

## Technical Details

### Legacy Application
- A simple Node.js application (`server.js`) serving HTTP requests.
- Runs on `localhost:8080` inside its container.
- Dockerfile: `Dockerfile.legacy`.

### Nginx Sidecar
- Acts as a reverse proxy.
- Terminates HTTPS traffic and forwards it to the legacy application.
- Uses a custom Nginx configuration (`nginx.conf`).
- Dockerfile: `Dockerfile.nginx`.

### Docker Compose
- Defines two services: `legacy-app` and `nginx-sidecar`.
- Both services share a private network (`sidecar-network`).
- Only the Nginx sidecar exposes port `443` to the host.

## Key Benefits

- **Security**: Adds HTTPS support without modifying the legacy application.
- **Simplicity**: Avoids the need to rebuild or refactor the legacy application.
- **Flexibility**: The sidecar pattern can be extended to add features like authentication, authorization, or certificate rotation.

## Notes

- Ensure you have valid SSL certificates (`server.crt` and `server.key`) in the `nginx-sidecar` directory.
- For testing purposes, you can generate self-signed certificates using OpenSSL:
  ```bash
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
  ```

## Conclusion

This example showcases how the sidecar pattern can modernize legacy applications by adding HTTPS support. It is a practical solution for teams facing challenges with outdated systems, enabling secure communication without significant redevelopment efforts.
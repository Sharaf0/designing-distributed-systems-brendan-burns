# Chapter 3: Sidecar Pattern

- Made up of two containers
- Coscheduled onto the same machine via atomic container group, such as a Kubernetes pod
- Both containers share filesystem, hostname, and network namespace
- The two containers are:
    1. The main application container
        - contains the core application logic
        - does not need to be aware of the sidecar container
    2. The sidecar container
        - augment and improve the main application container
        - can be used to add functionality, such as logging, monitoring, or security that might otherwise be difficult to implement in the main application container
- ![Sidecar Pattern](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098156343/files/assets/dds2_0301.png)

## Example: HTTP to HTTPS Sidecar

This example demonstrates the use of the sidecar pattern to add HTTPS support to a legacy HTTP application without modifying its source code. The setup includes:

1. **Legacy HTTP Application**: A containerized Node.js application serving HTTP requests on `localhost:8080`.
2. **Nginx Sidecar**: A containerized Nginx instance acting as a reverse proxy, terminating HTTPS traffic and forwarding it to the legacy application over HTTP.

For more details, refer to the [HTTP to HTTPS Sidecar Example](./code-examples/chapter-3/http-to-https/README.md).


# Chapter 2: Important Distributed Systems Concepts

## APIs and RPCs
- API (Application Programming Interface)
    - A set of rules and protocols for building and interacting with software applications
    - Defines the methods and data structures that developers can use to interact with a system
- RPC (Remote Procedure Call)
    - A protocol that allows a program to execute a procedure on a remote server as if it were local
    - Abstracts the details of network communication, allowing developers to focus on the logic of their applications
    - RPC is a specific type of API that is used for remote communication
- REST or RESTful (Representational State Transfer)
    - An architectural style for designing networked applications
    - Uses standard HTTP methods (GET, POST, PUT, DELETE) to interact with resources
    - Emphasizes stateless communication and the use of URIs to identify resources
    - Most commonly used with JSON data format, because of support, simplicity, and ease of use
- IDL (Interface Definition Language)
    - Describes the interface of a software component in a language-agnostic way
    - Used to generate client and server code in multiple programming languages
    - Allows for interoperability between different systems and languages
    - OpenAPI (formerly known as Swagger) is a popular IDL for RESTful APIs
- SLO (Service Level Objective) of an API:
    - A measurable goal for the latency, reliability, and throughput of an API
    - Helps to set expectations for performance and availability
    - Can be used to measure the success of an API and identify areas for improvement

## Synchronous vs. Asynchronous
- Synchronous communication
    - The client sends a request and waits (blocks) for a response from the server
    - Easier to implement and understand
    - Can lead to performance bottlenecks if the server is slow or unresponsive
- Asynchronous communication
    - The client sends a request and continues processing without waiting for a response
    - The server sends a response with an operation ID, and the client can check back later for the result
    - More suitable if length of the operation is measured in minutes or hours

## Latency (Performance)
- Latency is the time it takes for a request to travel from the client to the server and back
- It is generally measured in milliseconds (ms), faster systems in microseconds (μs), slower systems in seconds (s)
- Latency must be attributale (know where it comes from) and representative (know how it is measured)

## Reliability
- Fraction of successful requests relative to the total number of requests over a period of time
- Application dependable:
    - HTTP has rich error semantics, which means that it can return a variety of error codes (e.g., 404 Not Found, 500 Internal Server Error)
    - 20xs are generally considered acceptable (successful), but what about 20xs that contain errors?
    - 30xs are generally considered successful, they are just redirects, but what about too many redirects? it might be considered a failure
    - 40xs are generally considered client errors, which means that the client is at fault, but it is extremely uncertain, is 403 (unauthorized) a client error or the authorization server is down? is 404 (not found) a client error or the server is down or the server is misconfigured?
    - 50xs are generally considered a good target for reliability.
    - Misconfigured metrics can lead to wrong conclusions

## Percentiles
- The easiest way to measure is to just take the average
- Unfortunately, averages are often distorted, reasons for this:
    1. It is heavily skewed by outliers.
    2. It considers individual requests separately, while most user experiences are the combination of multiple requests which must succeed.
- The 90th or the 99th percentile of user experience is often used to measure latency:
    - 90th or 99th percentile of latency is the latency that 90% or 99% of requests are below
    - Example: The 99th precentile latency of single request is 100ms, which means that 99% of requests are below 100ms. Taken together, the 99th percentile latency of a single request rapidly approaches the 90th or even 50th percentile latency of different experiences.
- We must know which experience we are measuring, and which percentile we are measuring

## Idempotency
- Idempotency is the notion that whether an action is performed a single time or many times, the result is identical
- X = 5 <-- Whatever how many times, result will stay the same
- X = X + 1 <-- If you do it once, result is 6, if you do it twice, result is 7
- Similar to the IaaC, where the state of the system is defined by the code declaratively.
- Idempotency is important for distributed systems, because it allows for retries and error recovery without causing unintended side effects, i.e. we keep retrying until we get a success, and we do not care if we get the same result multiple times.

## Delivery Semantic
- Delivery semantics are the guarantees that a system provides about the delivery of messages or events
- At-least-once delivery
    - Guarantees that a message will be delivered at least once, but may be delivered multiple times
    - Example: A message queue that retries delivery if the consumer does not acknowledge receipt
- At-most-once delivery
    - Guarantees that a message will never be delivered more than once, but may be lost
    - Example: Charging a credit card, it assumes, in presence of failure, someone will try again
- Exactly-once delivery
    - Exceptionally difficult to achieve.
    - You are far better designing at-most-once or at-least-once delivery.

## Relational Integrity
- Refers to the accuracy and consistency of data stored within different systems and databases.
- Example: (user-id, balance) <-> (user-id, address), whether there are strong guarantees that for every user-id, the associated data remains consistent across different databases, ensuring integrity and reliability in data management.
- If the code can handle cases in which data in multiple stores may not be fully in sync, then the system does not rely on relational integrity.
- Synchronization of data across different systems has significant performance and reliability implications, for example the distributed transactions which require distributed locks, more complex and less parallel.
- It can be generally be seen as the distinction between SQL and NoSQL.
- SQL databases are designed to ensure relational integrity, while NoSQL databases (CosmosDB, Apache Cassandra) are designed to be more flexible and scalable; consistency is a problem of application code.
- Tradeoff between performance and code complexity.
- SQL: Low Complexity, low Performance, high Reliability, high Relational Integrity
- NoSQL: High Complexity, high Performance, low Reliability, low Relational Integrity

## Data Consistency
- In distributed systems, data is replicated to ensure availability, i.e. working even if one or more nodes fail
- Data consistency is the guarantee that all replicas of data are the same at any given time
- Choosing between strong consistency and eventual consistency is a long-term decision and will permeate the entire system.

### Strong Consistency
- Guarantees that the data is present everywhere before writing of the data is considered "complete".
- Example, in a replicated data among multiple data centers, if a user requests to write data, the system will ensure that the data is written to all replicas before returning a success response to the user.
- Decreases performance significantly but increases consistency and data reliability.


### Eventual Consistency
- Guarantees that the data will be same eventually, but not immediately.
- Example, in a replicated data among multiple data centers, if a user requests to write data, the system will return a success response to the user immediately, as soon as the data is written to only one replica, but it may take time for the data to be propagated asynchronously to all replicas.
- Increases performance significantly, it also ensures that the data is consistent eventually, but not immediately.
- Eventual consistency does not mean less reliable; it means that while the data may not be immediately consistent, it will become consistent over time as updates propagate through the system.

### CAP Theorem
- The CAP theorem states that in a distributed system, it is impossible to achieve all three of the following guarantees simultaneously:
    1. Consistency: All nodes see the same data at the same time.
    2. Availability: Every request receives a response, either success or failure.
    3. Partition Tolerance: The system continues to operate despite network partitions.

## Orchestration and Kubernetes
- Orchestration is the process of automating the deployment, scaling, operation, and management of containerized applications
- Kubernetes is the most common orchestration platform
- It takes desired state of the application, declaratively defined by the user, and makes it a reality

## Health Checks
- Orchestration platforms need to know the health of the application
- Knowing the health of the application will help the orchestration platform to make decisions about scaling, load balancing, and failover
### Liveness
- Liveness is a health check that determines whether the application is running and responsive
### Readiness
- Readiness is a health check that determines whether the application is ready to handle requests, initialzation of the state, reading cache, etc.

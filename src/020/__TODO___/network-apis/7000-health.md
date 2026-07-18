# Health check endpoints

It is good practice in network APIs to provide an endpoint that can be used to determine the health of the service.

In the case of HTTP APIs, this should be a simple `GET` request.

```http
GET /health
```

This endpoint may be called by other applications, such as load balancers, to act in case of service outage.

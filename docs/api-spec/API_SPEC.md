# API Specification

## Authentication
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| POST | /v1/auth/register | Register new user | 201, 400 |
| POST | /v1/auth/login | Login, receive JWT | 200, 401 |

## Services
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| POST | /v1/services/ | Register new microservice | 201, 400 |
| GET | /v1/services/ | List all services | 200 |
| GET | /v1/services/{id} | Get service + its endpoints | 200, 404 |
| PUT | /v1/services/{id} | Update service details | 200, 404 |
| DELETE | /v1/services/{id} | Delete service + endpoints | 204, 404 |

## Endpoints
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| POST | /v1/services/{id}/endpoints | Add endpoint to service | 201, 400 |
| GET | /v1/services/{id}/endpoints | List endpoints of service | 200 |
| GET | /v1/endpoints/{id} | Get endpoint + contract schema | 200, 404 |
| PUT | /v1/endpoints/{id} | Update endpoint contract | 200, 404 |

## Log Ingestion
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| POST | /v1/ingest/logs | Receive logs, build dependency graph | 202, 400 |

## Analysis
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| POST | /v1/analyze/change | Analyze breaking change impact | 200, 400 |

## Dependency Graph
| Method | URL | Purpose | Status Codes |
|--------|-----|---------|--------------|
| GET | /v1/graph/{service_id} | Get dependency graph for service | 200, 404 |
| GET | /v1/dependencies | List dependencies with filters | 200 |
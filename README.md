# Production Api Patterns
A production-grade REST API built with FastAPI and PostgreSQL, demonstrating patterns I care about: pagination, Redis caching, N+1 elimination, soft deletes, and OpenAPI documentation.

# ConnectHub User Service

## What I'm Building
A REST API for a social platform's user management system. The project is based on a real engineering scenario — a `/api/users` endpoint that degraded badly as the platform grew from 200K to 2.4M users. I'm rebuilding it properly.

## The Problem I'm Solving

The original implementation had five critical issues:

1. **N+1 queries** — fetched all users, then queried the database once per user for their posts. At 2.4M users this caused P95 latency of 22 seconds.
2. **No pagination** — loaded the entire user table into memory on every request, causing memory exhaustion and gateway timeouts.
3. **In-memory filtering** — filtered active users in Node.js after fetching all 2.4M rows from the database instead of filtering in SQL.
4. **Security** — `password_hash` was exposed in API responses. Deleted users (soft deletes) were still returned.
5. **No caching** — 71% of requests were for the same top 1,000 users, hitting the database every time.

## What I'm Building

A FastAPI + PostgreSQL service that fixes all of the above:

- `/api/users` — paginated, filtered at the database level, JOIN for posts, soft delete aware
- Redis caching for the top 1,000 users with a 5-minute TTL
- No sensitive fields ever fetched from the database
- Full OpenAPI documentation auto-generated from Pydantic models
- Integration tests with a real test database

## Tech Stack

- **FastAPI** — async Python web framework
- **PostgreSQL** — primary database via Docker
- **SQLAlchemy** — async ORM
- **Redis** — caching layer
- **Docker Compose** — local development environment
- **pytest** — integration and unit tests

## What I'll Learn

- Async database queries in Python
- Redis caching patterns in a real API context
- OpenAPI schema design with Pydantic
- Integration testing with a live database
- Production patterns: connection pooling, error handling, pagination


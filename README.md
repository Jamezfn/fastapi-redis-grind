# FastAPI-Redis Grind

A comprehensive collection of projects designed to master Redis and FastAPI integration through progressive, hands-on development.

## Overview

This repository contains 8 projects that systematically build your Redis skills and API development expertise. Each project introduces new Redis data structures and patterns, progressing from simple caching to advanced distributed systems.

## Prerequisites

- Python 3.9+
- Basic understanding of REST APIs
- Redis installed locally or access to a Redis instance
- Familiarity with key-value stores (helpful but not required)
- Understanding of async/await in Python (for Projects 6-8)

## Getting Started

Each project is self-contained in its own directory with dedicated setup instructions and API endpoints.
```bash
git clone https://github.com/Jamezfn/fastapi-redis-grind.git
cd fastapi-redis-grind
```

## Projects

### Project 1: Simple Cache API
**Core Concepts**: Strings, GET/SET, basic caching

A basic API that caches expensive computations and API responses.

**Key Learning**:
- Connecting to Redis with redis-py
- Basic string operations (GET, SET, DEL)
- Setting expiration with TTL
- Cache hit/miss patterns
- When to use caching

---

### Project 2: User Session Management
**Core Concepts**: Expiration, TTL, session tokens

A user authentication system with Redis-based session storage.

**Key Learning**:
- SETEX and EXPIRE commands
- Session token generation
- Automatic session expiration
- Session renewal patterns
- Deleting sessions on logout

---

### Project 3: Rate Limiter
**Core Concepts**: Counters, INCR, sliding window

An API rate limiting system to prevent abuse.

**Key Learning**:
- Atomic increment operations (INCR)
- Fixed window vs sliding window algorithms
- Using EXPIRE with counters
- Per-user and per-IP rate limiting
- Bucket-based rate limiting

---

### Project 4: Real-time Leaderboard
**Core Concepts**: Sorted Sets, ZADD, ZRANGE

A gaming leaderboard with real-time score updates and rankings.

**Key Learning**:
- Sorted Sets (ZADD, ZINCRBY, ZRANGE)
- Getting rank of a user (ZRANK, ZREVRANK)
- Range queries and pagination
- Leaderboard patterns (top N, around user)
- Score updates and tie-breaking

---

### Project 5: Shopping Cart System
**Core Concepts**: Hashes, complex data structures

An e-commerce shopping cart with item management.

**Key Learning**:
- Hash operations (HSET, HGET, HGETALL, HDEL)
- Storing structured data in hashes
- Incrementing hash fields (HINCRBY)
- Cart expiration strategies
- Converting between hashes and objects

---

### Project 6: Background Task Queue
**Core Concepts**: Lists, LPUSH/RPOP, async workers

A job queue system for processing background tasks with async workers.

**Key Learning**:
- Lists as queues (LPUSH, RPOP, BLPOP)
- Producer-consumer pattern
- Blocking operations for workers
- Task priority queues
- Using async redis-py for concurrent processing
- Dead letter queues for failed tasks

---

### Project 7: Real-time Chat with Pub/Sub
**Core Concepts**: Pub/Sub, channels, async messaging

A real-time chat application using Redis Pub/Sub with WebSockets.

**Key Learning**:
- Pub/Sub pattern (PUBLISH, SUBSCRIBE)
- Channel-based messaging
- Pattern subscriptions
- Async Pub/Sub with redis-py
- WebSocket integration with FastAPI
- Message broadcasting
- Online user tracking with Sets

---

### Project 8: Distributed Lock System
**Core Concepts**: Distributed locks, transactions, Lua scripts

A resource booking system with distributed locking to prevent race conditions.

**Key Learning**:
- SET with NX and EX options for locks
- Lock acquisition and release patterns
- Redlock algorithm basics
- WATCH and MULTI/EXEC for transactions
- Lua scripts for atomic operations
- Lock timeout and renewal
- Handling deadlocks

---

## Technical Stack

- **FastAPI**: Modern Python web framework (supports both sync and async)
- **Redis**: In-memory data structure store
- **redis-py**: Python Redis client (Projects 1-5: sync, Projects 6-8: async)
- **Pydantic**: Data validation and settings management

## Learning Path

Each project is designed to be completed sequentially, building on Redis concepts from previous projects.

**Progression**:
- **Projects 1-5**: Use sync redis-py to master core Redis data structures
- **Projects 6-8**: Transition to async redis-py for concurrent operations and real-time features

**Recommended approach**:
1. Complete each project fully before moving to the next
2. Implement all API endpoints for each project
3. Experiment with different Redis data structures for the same problem
4. Use Redis CLI to inspect data during development
5. Monitor commands with MONITOR for debugging
6. Test expiration and TTL behavior
7. Compare Redis solutions to database-backed approaches

## Key Concepts Covered

- **Data Structures**: Strings, Hashes, Lists, Sets, Sorted Sets
- **Caching Patterns**: Cache-aside, write-through, cache invalidation
- **Expiration**: TTL, EXPIRE, SETEX, automatic cleanup
- **Atomic Operations**: INCR, HINCRBY, ZINCRBY for race-free updates
- **Advanced Patterns**: Rate limiting, leaderboards, queues, locks
- **Pub/Sub**: Real-time messaging and event broadcasting
- **Transactions**: MULTI/EXEC, WATCH for optimistic locking
- **Lua Scripting**: Atomic multi-command operations
- **Performance**: Pipeline operations, connection pooling
- **Distributed Systems**: Distributed locks, coordination

## Contributing

Contributions are welcome! Please feel free to submit pull requests with improvements, additional projects, or documentation enhancements.

## License

MIT License - feel free to use these projects for learning and development.

## Resources

- [Redis Documentation](https://redis.io/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [redis-py Documentation](https://redis-py.readthedocs.io/)
- [Redis University](https://university.redis.com/) - Free courses
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Redis CLI](https://redis.io/docs/ui/cli/) - Command-line interface
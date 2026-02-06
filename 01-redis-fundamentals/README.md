# Redis Fundamentals - Phase 1

A comprehensive guide to mastering core Redis data structures and operations.

## Overview

This phase covers the essential building blocks of Redis, providing hands-on experience with the fundamental data structures and operations that power high-performance applications. By the end of this phase, I'll understand how to leverage Redis for caching, real-time analytics, message queues, and session management.

## Learning Objectives

- Understand Redis core data structures and their use cases
- Perform atomic operations and transactions
- Implement pub/sub messaging patterns
- Manage data lifecycle with expiration policies
- Apply best practices for Redis operations

## Topics Covered

### 1. Strings
**Simple key-value storage and atomic counters**

Strings are the most basic Redis data type, serving as the foundation for many operations.

**Key Concepts:**
- Basic SET/GET operations
- Atomic increment/decrement (INCR, DECR)
- Append operations
- Bit operations
- Numeric operations

**Use Cases:**
- Caching API responses
- Session tokens
- Page view counters
- Rate limiting counters
- Feature flags

**Example Commands:**
```bash
SET user:1000:name "Alice"
GET user:1000:name
INCR page:views
SETEX session:abc123 3600 "user_data"
```

---

### 2. Lists
**Queues and activity feeds**

Lists are ordered collections of strings, perfect for implementing queues and timelines.

**Key Concepts:**
- Push/pop operations (LPUSH, RPUSH, LPOP, RPOP)
- Blocking operations (BLPOP, BRPOP)
- Range queries (LRANGE)
- List trimming (LTRIM)
- List length (LLEN)

**Use Cases:**
- Task queues (background jobs)
- Activity feeds (social media timelines)
- Recent items lists
- Message queues
- Undo/redo functionality

**Example Commands:**
```bash
LPUSH queue:emails "email1@example.com"
RPOP queue:emails
LRANGE feed:user:100 0 9
LTRIM feed:user:100 0 99
```

---

### 3. Sets
**Unique collections and membership testing**

Sets store unordered collections of unique strings with fast membership testing.

**Key Concepts:**
- Add/remove members (SADD, SREM)
- Membership testing (SISMEMBER)
- Set operations (SINTER, SUNION, SDIFF)
- Random member selection (SRANDMEMBER)
- Cardinality (SCARD)

**Use Cases:**
- Unique visitor tracking
- Tags and categories
- Friend/follower relationships
- Blacklist/whitelist management
- Recommendation systems (collaborative filtering)

**Example Commands:**
```bash
SADD tags:post:500 "redis" "database" "nosql"
SISMEMBER tags:post:500 "redis"
SINTER friends:alice friends:bob
SUNION tags:post:1 tags:post:2
```

---

### 4. Sorted Sets
**Rankings and leaderboards**

Sorted Sets combine the uniqueness of sets with an associated score for ordering.

**Key Concepts:**
- Add members with scores (ZADD)
- Range queries by rank (ZRANGE, ZREVRANGE)
- Range queries by score (ZRANGEBYSCORE)
- Score updates (ZINCRBY)
- Rank retrieval (ZRANK, ZREVRANK)

**Use Cases:**
- Leaderboards and rankings
- Priority queues
- Time-series data with timestamps
- Rate limiting with sliding windows
- Auto-complete with prefix scoring

**Example Commands:**
```bash
ZADD leaderboard:game1 1000 "player1" 950 "player2"
ZREVRANGE leaderboard:game1 0 9 WITHSCORES
ZINCRBY leaderboard:game1 50 "player1"
ZRANK leaderboard:game1 "player2"
```

---

### 5. Hashes
**Object storage**

Hashes are maps between string fields and string values, ideal for representing objects.

**Key Concepts:**
- Set/get fields (HSET, HGET, HMSET, HMGET)
- Get all fields (HGETALL)
- Field existence (HEXISTS)
- Increment fields (HINCRBY)
- Field deletion (HDEL)

**Use Cases:**
- User profiles
- Product details
- Configuration settings
- Object caching
- Shopping carts

**Example Commands:**
```bash
HSET user:1000 name "Alice" email "alice@example.com" age 30
HGET user:1000 name
HGETALL user:1000
HINCRBY user:1000 age 1
```

---

### 6. Key Expiration and TTL
**Time-To-Live management**

Control data lifecycle by setting expiration times on keys.

**Key Concepts:**
- Set expiration (EXPIRE, EXPIREAT)
- Set key with expiration (SETEX, PSETEX)
- Check TTL (TTL, PTTL)
- Remove expiration (PERSIST)
- Refresh expiration on access

**Use Cases:**
- Session management
- Temporary caches
- Rate limiting windows
- OTP/verification codes
- Temporary locks

**Example Commands:**
```bash
SETEX session:abc123 3600 "session_data"
EXPIRE cache:user:100 300
TTL session:abc123
PERSIST cache:important:data
```

---

### 7. Pub/Sub
**Message broadcasting**

Publish/Subscribe enables real-time message distribution across multiple subscribers.

**Key Concepts:**
- Publish messages (PUBLISH)
- Subscribe to channels (SUBSCRIBE)
- Pattern matching (PSUBSCRIBE)
- Unsubscribe (UNSUBSCRIBE)
- Channel introspection (PUBSUB)

**Use Cases:**
- Real-time notifications
- Chat applications
- Event broadcasting
- Live updates and dashboards
- Microservice communication

**Example Commands:**
```bash
SUBSCRIBE notifications:user:100
PUBLISH notifications:user:100 "New message received"
PSUBSCRIBE events:*
PUBSUB CHANNELS
```

---

### 8. Transactions
**Atomic operations**

Execute multiple commands as a single atomic operation to ensure data consistency.

**Key Concepts:**
- Transaction blocks (MULTI, EXEC)
- Discard transactions (DISCARD)
- Optimistic locking (WATCH)
- Command queuing
- All-or-nothing execution

**Use Cases:**
- Atomic updates to multiple keys
- Financial transactions
- Inventory management
- Consistent state changes
- Race condition prevention

**Example Commands:**
```bash
MULTI
INCR balance:user:100
DECR balance:user:200
EXEC

WATCH inventory:item:500
MULTI
DECR inventory:item:500
SADD orders:pending order:12345
EXEC
```

---

## Getting Started

### Prerequisites
- Redis server installed (version 6.0 or higher recommended)
- Redis CLI or a Redis client library for your programming language

### Installation

**macOS:**
```bash
brew install redis
redis-server
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install redis-server
sudo systemctl start redis-server
```

**Docker:**
```bash
docker run -d -p 6379:6379 redis:latest
```

### Verification
```bash
redis-cli ping
# Expected output: PONG
```

## Practice Exercises

### Exercise 1: Build a Page View Counter
Implement atomic page view counting using strings.

### Exercise 2: Create a Task Queue
Use lists to build a simple job queue with producers and consumers.

### Exercise 3: Tag System
Implement a tagging system with set operations for finding related content.

### Exercise 4: Gaming Leaderboard
Build a real-time leaderboard using sorted sets.

### Exercise 5: User Profile Storage
Store and retrieve user profiles efficiently using hashes.

### Exercise 6: Session Management
Implement session storage with automatic expiration.

### Exercise 7: Real-time Notifications
Create a pub/sub notification system for multiple users.

### Exercise 8: Inventory System
Build a transactional inventory system that prevents overselling.

## Best Practices

1. **Key Naming Conventions**: Use descriptive, hierarchical names (e.g., `user:1000:profile`)
2. **Memory Management**: Set appropriate expiration times to prevent memory bloat
3. **Atomic Operations**: Use built-in atomic commands instead of read-modify-write patterns
4. **Pipeline Commands**: Batch multiple commands to reduce network round trips
5. **Choose the Right Data Structure**: Match data structures to your access patterns
6. **Monitor Memory Usage**: Track key sizes and total memory consumption
7. **Handle Connection Failures**: Implement retry logic and connection pooling

## Common Pitfalls

- Using Redis as a primary database without persistence configured
- Not setting expiration on temporary data
- Storing large values in individual keys
- Using transactions when Lua scripts would be more efficient
- Not handling pub/sub connection drops
- Blocking operations in single-threaded applications

## Resources

- [Official Redis Documentation](https://redis.io/documentation)
- [Redis Commands Reference](https://redis.io/commands)
- [Try Redis Interactive Tutorial](https://try.redis.io/)
- [Redis University](https://university.redis.com/)

## Next Steps

After mastering Phase 1, you'll be ready to explore:
- Advanced Redis patterns and use cases
- Lua scripting for complex operations
- Redis persistence and durability
- Replication and high availability
- Redis clustering and scaling
- Performance optimization and monitoring

## Contributing

Found an error or want to improve this guide? Contributions are welcome!

## License

This educational material is provided as-is for learning purposes.

---

**Happy Learning!**
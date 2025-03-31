# Momentum - Database Schema
## Overview
This document provides an explanation of the database structure for the **Project Management Web App**, including table definitions and SQL queries to create them.

## Database Schema
The database consists of the following tables:
- `users`: Stores user details and roles.
- `projects`: Stores project details and status.
- `tasks`: Stores tasks associated with projects.
- `comments`: Stores comments on tasks.
- `notifications`: Stores notifications for users.

## Table Definitions & SQL Queries

### 1. Users Table
Stores user details and roles.
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role ENUM('admin', 'manager', 'team_member') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Projects Table
Stores project details and status.
```sql
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('not_started', 'in_progress', 'completed') DEFAULT 'not_started',
    start_date DATE,
    end_date DATE,
    created_by INT REFERENCES users(id) ON DELETE SET NULL
);
```

### 3. Tasks Table
Each project contains multiple tasks.
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    assigned_to INT REFERENCES users(id) ON DELETE SET NULL,
    status ENUM('todo', 'in_progress', 'done') DEFAULT 'todo',
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Comments Table
Users can comment on tasks.
```sql
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    task_id INT REFERENCES tasks(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Notifications Table
To store user notifications.
```sql
CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Notes
- The `users` table contains role-based access control.
- The `projects` table references `users` as creators.
- The `tasks` table references `projects` and `users` for assignments.
- The `comments` table links users to tasks.
- The `notifications` table helps in tracking updates.

This schema ensures relational integrity and supports efficient data retrieval for the Project Management Web App.

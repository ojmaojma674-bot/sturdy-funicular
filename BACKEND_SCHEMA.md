# VHOTIEX AI Backend Schema

## 1. Purpose
This schema defines the backend data model for conversations, memory, agents, sessions, tools, and safety events.

## 2. Core Entities

### 2.1 users
- id: UUID
- email: string
- name: string
- created_at: timestamp
- updated_at: timestamp
- preference_profile: JSON
- consent_flags: JSON

### 2.2 sessions
- id: UUID
- user_id: UUID
- agent_id: UUID or nullable
- title: string
- status: enum (active, archived, suspended)
- created_at: timestamp
- updated_at: timestamp
- last_activity_at: timestamp

### 2.3 messages
- id: UUID
- session_id: UUID
- sender: enum (user, assistant, system)
- role: string
- content: text
- metadata: JSON
- created_at: timestamp

### 2.4 agents
- id: UUID
- name: string
- type: enum (coding, research, analysis, planning, review, security, recovery)
- status: enum (active, disabled, testing)
- description: text
- config: JSON

### 2.5 memory_items
- id: UUID
- user_id: UUID
- session_id: UUID or nullable
- topic: string
- summary: text
- relevance_score: float
- created_at: timestamp
- updated_at: timestamp

### 2.6 tools
- id: UUID
- name: string
- category: string
- description: text
- config: JSON
- enabled: boolean

### 2.7 tool_calls
- id: UUID
- session_id: UUID
- tool_id: UUID
- request_payload: JSON
- result_payload: JSON
- status: enum (queued, success, failed, blocked)
- executed_at: timestamp

### 2.8 security_events
- id: UUID
- user_id: UUID or nullable
- session_id: UUID or nullable
- event_type: string
- severity: enum (info, warning, critical)
- details: JSON
- created_at: timestamp

### 2.9 app_health
- id: UUID
- component: string
- state: enum (healthy, degraded, failed)
- details: JSON
- observed_at: timestamp

## 3. Relationships
- one user can have many sessions
- one session can have many messages
- one session can have many tool calls
- one user can have many memory items
- one session may relate to one active agent at a time
- one app health record may correspond to a runtime component

## 4. Security and Privacy Rules
- no secrets stored in plain text
- voice recordings should be stored only when consent is granted
- sensitive data must be encrypted at rest
- audit logs must be retained with access restrictions
- security events should be monitored and surfaced in recovery flows

## 5. API Data Contract Expectations
- chat responses should return message, session metadata, agent state, and safety notes
- memory requests should return compact summaries and relevant context
- tool execution should return status, payload, and error details when blocked or failed
- health endpoints should report operational status and degraded components

## 6. Storage Recommendations
- PostgreSQL for relational data
- Redis or in-memory cache for rapid context retrieval
- object storage for large attachments or voice artifacts if needed
- structured logging for service health and observability

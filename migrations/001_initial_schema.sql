-- Migration 001: Initial Schema

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    owner_user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS team_members (
    team_id INTEGER REFERENCES teams(id),
    user_id INTEGER REFERENCES users(id),
    role VARCHAR(50) DEFAULT 'member',
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (team_id, user_id)
);

CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams(id) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(team_id, name)
);

CREATE TABLE IF NOT EXISTS endpoints (
    id SERIAL PRIMARY KEY,
    service_id INTEGER REFERENCES services(id) ON DELETE CASCADE NOT NULL,
    path VARCHAR(500) NOT NULL,
    method VARCHAR(10) NOT NULL,
    contract_schema JSONB,
    version INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(service_id, path, method)
);

CREATE TABLE IF NOT EXISTS dependencies (
    id SERIAL PRIMARY KEY,
    caller_service_id INTEGER REFERENCES services(id) NOT NULL,
    callee_endpoint_id INTEGER REFERENCES endpoints(id) NOT NULL,
    call_frequency INTEGER DEFAULT 1,
    last_seen TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    first_seen TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(caller_service_id, callee_endpoint_id)
);

CREATE TABLE IF NOT EXISTS api_changes (
    id SERIAL PRIMARY KEY,
    endpoint_id INTEGER REFERENCES endpoints(id) NOT NULL,
    old_contract JSONB,
    new_contract JSONB,
    breaking_changes JSONB,
    impact_summary JSONB,
    analyzed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    analyzed_by INTEGER REFERENCES users(id)
);

CREATE INDEX IF NOT EXISTS idx_services_team        ON services(team_id);
CREATE INDEX IF NOT EXISTS idx_endpoints_service    ON endpoints(service_id);
CREATE INDEX IF NOT EXISTS idx_dependencies_caller  ON dependencies(caller_service_id);
CREATE INDEX IF NOT EXISTS idx_dependencies_callee  ON dependencies(callee_endpoint_id);
CREATE INDEX IF NOT EXISTS idx_api_changes_endpoint ON api_changes(endpoint_id);
CREATE INDEX IF NOT EXISTS idx_users_email          ON users(email);

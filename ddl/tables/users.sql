-- users table keeps initial data

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    name TEXT,
    age INTEGER,
    gender TEXT,
    phone INTEGER,
    country TEXT,
    --is_premium INTEGER
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Unique compound index
CREATE UNIQUE INDEX idx_user_id_username_unique ON users(user_id, username);

-- users_quality / users_characteristics
CREATE TABLE users_quality (
    user_id INTEGER PRIMARY KEY,
    current_weight REAL,
    height REAL,
    waist_measurement REAL,
    chest_measurement REAL,
    hip measurement REAL,
    body_type TEXT,
--    desired_weight REAL,
--    number_of_people INTEGER,
    measurement_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Index
CREATE INDEX idx_user_id ON users(user_id);

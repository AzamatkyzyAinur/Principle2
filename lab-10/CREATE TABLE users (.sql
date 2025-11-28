CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE user_score (
    user_id INT REFERENCES users(id),
    score INT DEFAULT 0,
    level INT DEFAULT 1
);
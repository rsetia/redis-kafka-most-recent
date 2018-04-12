CREATE DATABASE IF NOT EXISTS main; 
USE main; 

CREATE TABLE IF NOT EXISTS word_entries (
  id int NOT NULL PRIMARY KEY,
  user_id int NOT NULL,
  word text NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT current_timestamp, 
  updated_at TIMESTAMP NOT NULL DEFAULT now() ON UPDATE now()
);

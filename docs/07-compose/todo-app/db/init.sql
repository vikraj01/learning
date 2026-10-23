-- Runs once, the first time the database starts with an empty volume.
CREATE TABLE todos (
  id   SERIAL PRIMARY KEY,
  text TEXT NOT NULL,
  done BOOLEAN NOT NULL DEFAULT false
);

INSERT INTO todos (text) VALUES ('Learn Docker Compose'), ('Make chai');

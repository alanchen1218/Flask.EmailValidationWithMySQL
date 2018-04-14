SELECT * FROM emails;
INSERT INTO emails(email, created_at, updated_at) VALUES("alanchen5@gmail.com", now(), now());

UPDATE emails SET email = 'alanchen5@gmail.com' WHERE id =5
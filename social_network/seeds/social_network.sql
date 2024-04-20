DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;


CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
-- The foreign key name is always {other_table_singular}_id
    account_id int,
    constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

INSERT INTO accounts (email, username) VALUES ('iamcool@gmail.com', 'i_am_cool');
INSERT INTO accounts (email, username) VALUES ('tired@gmail.com', 'i_am_tired');
INSERT INTO accounts (email, username) VALUES ('icecream@gmail.com', 'i_am_icecream');

INSERT INTO posts (title, content, views, account_id) VALUES ('Today is Mon', 'it is sunny', '3', '1');
INSERT INTO posts (title, content, views, account_id) VALUES ('Today is Tue', 'it is rainy', '2', '1');
INSERT INTO posts (title, content, views, account_id) VALUES ('Today is Weds', 'it is bad', '0', '3');
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post text,
    content text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment_name text,
    comment_content text,
    post_id int,
    constraint fk_posts foreign key(post_id)
    references posts(id)
    on delete cascade
);
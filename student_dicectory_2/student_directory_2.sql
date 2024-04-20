DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

-- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS students_id_seq;
-- CREATE TABLE students (
--     id SERIAL PRIMARY KEY,
--     name text,
--     cohort_name text,
--     cohort_id int,
--     constraint fk_cohorts foreign key(cohort_id)
--     references cohorts(id)
--     on delete cascade
-- );

-- CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
-- CREATE TABLE cohorts (
--     id SERIAL PRIMARY KEY,
--     cohort_name text,
--     start_date text
-- );

CREATE SEQUENCE IF NOT EXISTS cohort_id_seq;
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    cohort_name text,
    starting_date date
);
CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name text,
    cohort_id int,
    constraint fk_cohorts foreign key(cohort_id) 
    references cohorts(id) on delete cascade
);
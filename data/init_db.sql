
CREATE TABLE boilerplate_student
(
    pk_uuid      UUID         NOT NULL DEFAULT gen_random_uuid(),

    created_at                 TIMESTAMP(6) WITHOUT TIME ZONE NOT NULL DEFAULT transaction_timestamp(),
    first_name      VARCHAR                     NULL,
    password      VARCHAR                     NULL,
    last_name      VARCHAR                     NULL,
    nationality_type VARCHAR                   NOT NULL,


    PRIMARY KEY (pk_uuid)
);
CREATE INDEX boilerplate_student_first_name
    ON boilerplate_student (first_name DESC);
CREATE INDEX boilerplate_student_last_name
    ON boilerplate_student (last_name DESC);

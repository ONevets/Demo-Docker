create table surveys (
    id SERIAL primary key,
    age varchar(5) NOT NULL,
    cats varchar(5) NOT NULL,
    features varchar(50) NOT NULL,
    conditionalquestion varchar(4) NOT NULL,
    conditionaldetails text,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
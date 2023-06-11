create table if not exists Users (
    id serial primary key,
    username varchar(120),
    password varchar(120)
);

create table if not exists Recipes (
    rid serial primary key,
    name varchar(120),
    category varchar(120),
    cuisine varchar(120),
    ingredients text,
    description text,
    method text,
    created_by int references Users(id) default 0,
    created_at timestamp default current_timestamp
);

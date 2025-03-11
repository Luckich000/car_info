create schema if not exists rakultcev_vagel;

create table if not exists rakultcev_vagel.car (
  car_id serial primary key,
  model varchar(100)not null,
  car_year int not null check(car_year>1885 and car_year<= extract(year from current_date)) ,
  color varchar(100)not null,
  car_number varchar(100)not null unique,
  car_type varchar(100) not null
);

create table if not exists rakultcev_vagel.accident(
  accident_id serial primary key,
  car_id int not null,
  accident_date date not null,
  description text not null,
  FOREIGN KEY (car_id) REFERENCES rakultcev_vagel.car(car_id) ON DELETE CASCADE
);
DROP DATABASE if exists restapiserver;
create database restapiserver;

use restapiserver;

create table users(
    id bigint auto_increment not null primary key ,
    email varchar(20) not null  ,
    name varchar(20) not null ,
    password varchar(64) not null ,
    authcode varchar(30) not null ,
    constraint email_unique unique key (email)
);


create table api_key(
    id bigint auto_increment not null primary key ,
    apikey varchar(64) not null ,
    created date not null ,
    moded date not null ,
    limittime int default 3,
    constraint apikey_unique unique key (apikey),
    FOREIGN KEY (id) REFERENCES users(id)
);

-- 작성중
create table address(
    id bigint auto_increment primary key ,
    country varchar(10) not null
    -- 국가 / 시 ,도 / 읍,면,리 / 상세 / 우편번호 /
    -- 영문주소 API 호출해서
);


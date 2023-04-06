drop database if exists serverlog;
create database serverlog;
use serverlog;

create table restapi_test(
    id bigint primary key auto_increment,
    loglevel varchar(10) not null ,
    adminId varchar(10) not null ,
    date date not null ,
    logstr varchar(1000) not null ,
    requesturl varchar(200) default null
)

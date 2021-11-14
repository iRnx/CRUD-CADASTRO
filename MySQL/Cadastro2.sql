create database if not exists cadastro2;
use cadastro2;

create table if not exists pessoas(
id int auto_increment not null primary key,
nome varchar(30) not null,
sobrenome varchar(45) not null,
sexo enum('M', 'F') not null,
data_nascimento date not null,
cpf varchar(11) not null unique,
email varchar(70) not null unique,
rua varchar(45) not null,
numero int  not null,
complemento varchar(20) default 'Sem Complemento',
cep int not null,
cidade varchar(50) not null,
estado char(2) not null
);



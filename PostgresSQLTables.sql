
CREATE TABLE info
(
  nombre character varying(100),
  hash character varying(100),
  creadora character varying(100),
  fecha character varying(100)
)



CREATE TABLE logs
(
  ip character varying(30),
  fecha character varying(30),
  hora character varying(30),
  numero1 character varying(30),
  numero2 character varying(30),
  sign character varying(30),
  solucion character varying(30)
)


CREATE TABLE public.personas
(
  nombre character varying(10)
)



CREATE TABLE sign
(
  significado character varying(30),
  simbolo character varying(30)
)

insert into sign (significado,simbolo) values ('suma','+');
insert into sign (significado,simbolo) values ('resta','-');
insert into sign (significado,simbolo) values ('dividir','/');
insert into sign (significado,simbolo) values ('multiplicar','*');


--Selects
select * from sign; --- Aquí se guardan los simbolos para que aprenda hacer lo q quiera
select * from estados; --- Dice lo que el mae sabe hacer, y lo que desaprende
select * from logs; --- Guarda lo que va ejecutando
select * from info --- Guarda la info del hash



create table Estados (simbolo varchar(10), definicion varchar(10))
drop table estados
drop table logs;


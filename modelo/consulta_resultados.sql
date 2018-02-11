use tuasiste_financiero;
#truncate table budget_test;
select *
from budget_test 
where description='Deudas';

create temporary table if not exists  top_user(user_id int);


select distinct user_id
from budget_test 
limit 20;

select distinct a.user_id as usuario, a.income as ingresos, a.description as categoria, a.category_total as total_gasto, a.class as porcentaje, a.percent as clasificacion
from budget_test as a
 #inner join (select distinct user_id
#from budget_test 
#limit 20) as b on a.user_id=b.user_id
where substring(a.user_id,1,4)=2015
order by a.user_id
limit 40;


#'201510385513111', '600000', 'Vivienda', '110000', 'BUENO', '0.183333333333333'

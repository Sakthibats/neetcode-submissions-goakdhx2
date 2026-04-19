-- Write your query below


select a.sale_date, a.sold_num-b.sold_num as diff from (select aa.sale_date, aa.fruit, aa.sold_num from sales aa 
where fruit = 'apples') a left join (select o.sale_date, o.fruit, o.sold_num from sales o
where fruit = 'oranges') b on a.sale_date = b.sale_date
order by sale_date
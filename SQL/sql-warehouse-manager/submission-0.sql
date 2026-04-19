-- Write your query below

select w.name as warehouse_name,sum(p.width * p.length * p.height*w.units) as volume from warehouse w
left join products p on p.product_id = w.product_id
group by warehouse_name
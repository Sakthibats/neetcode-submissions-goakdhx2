-- Write your query below
select fin.left_operand, fin.operator, fin.right_operand, 
    case 
        when fin.operator = '=' and fin.left=fin.right then 'true' 
        when fin.operator = '>' and fin.left>fin.right then 'true' 
        when fin.operator = '<' and fin.left<fin.right then 'true'
        else 'false'
    end as Value from
(select 
    e.left_operand, e.operator, e.right_operand, v1.value as left, v2.value as right
from expressions e
left join variables v1 on e.left_operand = v1.name
left join variables v2 on e.right_operand = v2.name) fin
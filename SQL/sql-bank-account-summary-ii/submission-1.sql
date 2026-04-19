-- Write your query below

select u.name, sum(t.amount) as balance from transactions t join users u on u.account = t.account
group by u.name
having sum(t.amount) >10000


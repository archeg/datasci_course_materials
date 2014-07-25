--r, c
select value from
(
select 2 as row_num, 3 as col_num, sum(val) as value from
(select a.value * b.value as val from A a, b b where a.row_num = 2 and b.col_num = 3 and a.col_num = b.row_num)
);

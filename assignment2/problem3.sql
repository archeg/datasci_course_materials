select col_num, value from
(
select a.docid as row_num, b.docid as col_num, sum(a.count*b.count) as value from 
(SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count)
a, 
(SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count)
b
where a.term = b.term 
group by a.docid, b.docid
)
where row_num = "q" order by value;

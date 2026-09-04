CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        select Max(salary) from(
            select salary , 
                DENSE_RANK() over (order by salary DESC) As rnk 
                from Employee
        )t 
        where rnk = N
  );
END
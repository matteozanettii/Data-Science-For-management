--18
select distinct e.name,e.surname
from employee e,participation par
where e.employeeid=par.participantid
and e.salary >= (select max(ee.salary)
                from employee ee, participation part
                where ee.employeeid = part.participantid
                and par.projectcode=part.projectcode
               )  
               
--19         
select avg(salary)
from employee
group by department
--20,21
select projectcode,sum(salary) as ProjectCost,
from employee e , project p
where e.employeeid=p.participantid
group by p.projectcode
order by projectcost desc
-- 22
SELECT DISTINCT pa.ProjectCode
FROM Participation pa, Project p
WHERE pa.ParticipantID = p.Manager
AND pa.ProjectCode <> p.ProjectCode;
--23 
select e.name,e.surname
from employee e,project pro, participation par
where e.employeeid=par.participantid
and par.projectcode=pro.projectcode
and pro.budget=(select max(budget)
                from project)
-- 24
SELECT pa.ProjectCode
FROM Participation pa
GROUP BY pa.ProjectCode
HAVING COUNT(*) <= ALL (
    SELECT COUNT(*)
    FROM Participation
    GROUP BY ProjectCode
);

--additional exercises
-- ============================================================
-- Exercise 4.7 -
-- ============================================================

-- 1 case 
SELECT Qualifications, AVG(Age) AS AverageAge
FROM PROFESSORS
GROUP BY Qualifications;

-- 2nd case
SELECT Qualifications, AVG(Age) AS AverageAge
FROM PROFESSORS
WHERE Age IS NOT NULL
  AND Age <> 0
GROUP BY Qualifications;


-- ============================================================
-- Exercise 4.16 - Students / Exams
-- ============================================================

-- 1.student wich did not pass the exams
SELECT s.*
FROM Students s
WHERE NOT EXISTS (
    SELECT 1
    FROM Exams e
    WHERE e.Student = s.RollNum
      AND e.Grade >= 18
);

-- alternative
-- SELECT s.*
-- FROM Students s
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM Exams e
--     WHERE e.Student = s.RollNum
-- );

-- 2. 
SELECT DISTINCT s.*
FROM Students s
JOIN Exams e
  ON e.Student = s.RollNum
WHERE e.Grade > ANY (
    SELECT e2.Grade
    FROM Exams e2
    JOIN Students s2
      ON e2.Student = s2.RollNum
    WHERE s2.Surname = 'Pythagoras'
      AND s2.Name = 'Archimedes'
);

-- 3. 
SELECT s.RollNum,
       s.Name,
       s.Surname,
       COUNT(e.CourseID) AS PassedExams,
       AVG(e.Grade) AS AverageGrade
FROM Students s
LEFT JOIN Exams e
  ON e.Student = s.RollNum
 AND e.Grade >= 18
GROUP BY s.RollNum, s.Name, s.Surname;


-- ============================================================
-- Exercise 4.19 - PRODUCTS / SALES
-- ============================================================

-- 1. 
SELECT p.Code
FROM PRODUCTS p
WHERE NOT EXISTS (
    SELECT 1
    FROM SALES s
    WHERE s.ProductID = p.Code
);

-- 2. 
SELECT s.Price
FROM SALES s
JOIN PRODUCTS p
  ON s.ProductID = p.Code
WHERE s.Date = DATE '2008-11-28';





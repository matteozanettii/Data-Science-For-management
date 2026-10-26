--1,2
select name, surname
from employee
where salary between 10 and 30
order by salary desc
--3,4
SELECT e.name, e.surname
FROM employee e, project p
WHERE e.employeeid = p.participantid 
  AND e.name = 'Matteo' 
  AND p.projectcode = 'Alpha';
  order by e.surname desc
--5,6
  select distinct e1.name,e1.surname
  from employee e1, employee e2
  where e1.name=e2.name
  and e1.department='Shipping'
  and e2.department='management'
  order by e1.surname asc;
  --7,8
  select distinct e.department
  from employee e, participation p
  where e.employeeid = p.participantid
  and p.projectcode = 'Alpha'
  order by e.department asc
  --9,10,12
  select d.director,d.location,d.name
  from employee e, department d
  where e.department = d.name
  where e.name='Marco'
  and e.surname='Bruni'
  -- 11
  select e.name,e.surname 
  from employee e, participation p
  where p.projectcode = "Apollo"
  and p.manager=e.employeeid
--13
select p.budget 
from employee e , project p, participation part
 where e.name="Marco"
 and e.surname="Bruni"
 and e.employeeid=part.participantid
 and part.projectcode=p.projectcode
--14,15
select e.name,e.surname
from employee e , department d, employee mng
where e.department=d.name
and d.director=mng.employeeid
and e.salary > mng.salary
order by e.salary asc

select Name, Surname
from employee
where department = 'Shipping'
  and name in (
      select name
      from employee
      where department = 'Management'
  );
  select name surname
  from employee
  where salary > (select e.salary
                  from employee e,department d 
                  where e.employeeid=d.director
                  and d.name=e.department 
)


















  














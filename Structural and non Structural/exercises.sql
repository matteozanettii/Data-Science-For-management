select name, surname
from employee
where salary >10 and salary <30 desc
--3
SELECT employee.name, surname
FROM employee, project, participation
WHERE employeeid = participantid 
  AND projectcode = project_id_or_code 
  AND employee.name = 'Matteo' 
  AND projectcode = 'Alpha';
  order by surname desc
  --5
  select distinct e1.name,e1.surname
  from employee e1, employee e2
  where e1.surname=e2.surname
  and e1.department="Shippings"
  and e2.department="management"
  order by e1.surname desc
  --7
  select p.departments
  from employee e, participation p
  where p.projectcode == "Alpha"
  and e.employeeid == p.participantid
  order by p.departments desc
  --9,10,12
  select d.director,d.location,d.name
  from employee e, department d
  where e.name="Marco"
  and e.surname="Bruni"
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
--15
select e.name,e.surname
from employee e , department d, employee mng
where d.name=e.department
and d.director=e.employeeid
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


















  














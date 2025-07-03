Select distinct
s.id as StudentID,
"program_ID",
'' as Grade,
cs.name,
cs."Unit",
sa.id as semesterID
from "CareerPath".student s
join "CareerPath"."Program" p on p.name=s."program_ID"
join "CareerPath"."career_Path" cp on cp."program_id" = p.id
join "CareerPath".courses cs on cs.career_path_id = cp.id
join "CareerPath".semesters sa on sa.id = cs.semesta_id
order by s.id asc
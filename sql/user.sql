desc user;

-- 회원가입
insert
	into user
    values (null, '둘리', 'dooly@gmail.com', password('1234'), 'male', now());



-- login
select *
from user
where eamil='dooly@mail.com'
and password=password('1234');


-- 회원정보 수정
select name, email, gender
  from user
 where no=2;

update user
   set name='...', gender='...'
  where no=2;

update user
   set name='...', password=password('....'), gender='...'
  where no=2;
  
  
  select *
	from user

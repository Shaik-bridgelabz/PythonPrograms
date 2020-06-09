import random

is_full_time=1;
is_part_time=2;
emp_rate_per_hr=20;
random_check=random.randint(1,2)

if(is_full_time == random_check):
	emp_hrs=8;
elif(is_part_time == random_check):
	emp_hrs=4;
else:
	emp_hrs=0;

salary=( emp_hrs * emp_rate_per_hr )
print (salary)


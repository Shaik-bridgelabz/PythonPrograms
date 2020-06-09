import random

isPresent=1
randomCheck=random.randint(0,1)

if(isPresent == randomCheck):
	empRatePerHr=200;
	empHrs=8;
	salary=( empHrs * empRatePerHr )
else:
	salary=0

print (salary)


chocolate_price=1
amount = 40
num_chocolate=amount//chocolate_price
wrapper=num_chocolate
wrappers_per_choc = 2
result=0
new_choco=0

while wrapper >= wrappers_per_choc:
    new_choco,wrapper=divmod(wrapper,wrappers_per_choc)
    num_chocolate+=new_choco
    wrapper += new_choco


print(num_chocolate)    
   

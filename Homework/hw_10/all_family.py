family = dict(grandpa_Alex = 76,  grandma_Nona= 74,

  dad_Greg = 48, mom_July= 45,  son_older_Bob = 18,

  son_middle_Alex = 15,  son_young_Mark = 10)
  
for k,v in family.items():
    print(k,v)

difference_old = max(family.values())- min(family.values())
print(f"This {difference_old} is the difference between the oldest and youngest family member")

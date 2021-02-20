def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'

def tickets_dict(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'

def tickets_orig(people):
    print(people)
    
    cost = 25
    change = []

    for person in people:
        
        if person == 25:
            change.append(person)
        elif person == 100 and change.count(50) == 0 and change.count(25) >=3:
            change.append(person)
            change.remove(cost)
            change.remove(cost)
            change.remove(cost)
        elif person == 50 and change.count(25) >=1:
            change.append(person)
            change.remove(cost)
        elif person == 100 and change.count(50) >=1 and change.count(25) >=1:
            change.append(person)
            change.remove(cost)
            change.remove(50)
        else:
            return "NO"
        print(change)
    return "YES"

"""def tickets(people):
    print(people)
    
    cost = 25
    change = 0
    i = 1
    
    for person in people:
        print("Iteration", i)
        print("Person", person)
        print("Change", change)
        print("Cost", cost)
        
        if change + cost >= person:
            print("* Change + Cost >= Person *")
            if person > cost:
                change += person - cost
            else:
                change += person
        
        if person - cost > change:
            return "NO"
        
    return "YES"
def tickets(people):
    print(people)
    cost = 25
    change = 0
    i = 1
    for person in people:
        print("Iteration", i)
        print("Person", person)
        print("Change", change)
        print("Cost", cost)
        
        if person > cost and change == 0:
            return "NO"
        if cost == person:
            print("1")
            change += person
        if person > cost and change > 0:
            print("2")
            if (person - cost) > change:
                print("3")
                return "NO"
            change -= cost
            print("Change2", change)
        
        i+=1
    return "YES"
"""
#cost = 25

#person = 25
#change = 25

#person = 25
#change = 50

#person = 50
#change = 
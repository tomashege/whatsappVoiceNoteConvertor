def diff(list1, list2): 
      return [x for x in (set(list1).union(set(list2))-set(list1).intersection(set(list2))) if x not in set(list1)]

print(diff(["apple",2,"bannana"],[2,"hey it works"])) 



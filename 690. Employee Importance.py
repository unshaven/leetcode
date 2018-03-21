'''
You are given a data structure of employee information, which includes the employee's unique id,
his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], 
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. 
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, 
you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11

Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. 
They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
'''
技巧都是利用hash table 将employee的id作为key值，value为一个employees对象
#两种方法 一种是递归，之前自己想的递归是传递一个sum参数，防止每次递归sum初始化为0，但是会把已经算过的值继续算一次
其实可以让sum=初始值，后面用sum+=
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        emp = {employee.id:employee for employee in employees}  #存储为hash
        return self.getSum(emp,id)
    def getSum(self,emp,id):
        sum1 = emp[id].importance     #递归地每次加的sum1其实是此id的value值
        for id1 in emp[id].subordinates:
            sum1 += self.getSum(emp,id1)
        return sum1
      
      
    
class Solution2:
    def getImportance(self, employees, id):
        emp = {employee.id:employee for employee in employees}  #存储为hash
        def dps(id):
            count_sum = sum(dps(id) for a in emp[id].subordinates)
            return count_sum + emp[id].importance
        return dps(id)
    
    
    
    
    
    
    

import clingo
import os,sys
from os.path import join as joinp



###################################INPUT PARAMETERS###############################################################

students = [
    "Giuseppe",  # 0
    "Maria",     # 1
    "Giovanni",  # 2
    "Anna",      # 3
    "Antonio",   # 4
    "Giulia",    # 5
    "Luca",      # 6
    "Lucia",     # 7
    "Marco",     # 8
    "Francesca", # 9
    "Alessandro",# 10
    "Sofia",     # 11
    "Matteo",    # 12
    "Martina",   # 13
    "Andrea",    # 14
    "Silvia",    # 15
    "Stefano",   # 16
    "Michele",   # 17
    "Alberto",   # 18
    "Elena",     # 19
    "Riccardo",  # 20
    "Valentina", # 21
    "Federico",  # 22
    "Chiara",    # 23
    "Daniele",   # 24
    "Beatrice",  # 25
    "Francesco", # 26
    "Alessia",   # 27
    "Roberto",   # 28
    "Laura",     # 29
    "Simone",    # 30
    "Sara",      # 31
    "Paolo",     # 32
    "Elisa",     # 33
    "Pietro",    # 34
    "Isabella",  # 35
    "Massimo",   # 36
    "Daniela"    # 37
]

### add a list of numbers corresponding to students that belong to the same group
### this can be used also to indicate lunch groups that happened in the past
past_groups = [
    [0, 1, 2, 3, 4],     # Group 1: 5 members
    [5, 6, 7, 8, 9],     # Group 2: 5 members
    [10, 11, 12, 13, 14],# Group 3: 5 members
    [15, 16, 17, 18, 19],# Group 4: 5 members
    [20, 21, 22, 23, 24, 25], # Group 5: 6 members
    [26, 27, 28, 29, 30, 31], # Group 6: 6 members
    [32, 33, 34, 35, 36, 37]  # Group 7: 6 members
]
weeks = 5
n_groups = 6
time_limit = 10 #timeout for the solver (in seconds)

cost = -1
solution = ""

###################################INPUT PARAMETERS END###############################################################



class Context:
    def id(self, x):
         return x
    def seq(self, x, y):
         return [x, y]

def on_model(m):
    global cost, solution #porcata indicibile, but works
    cost = m.cost[0]
    solution = str(m)

            
def create_input_file(filename="input.lp"):
    students_padded = pad_students(students,n_groups)
    past_groups_padded = pad_groups(past_groups,students,students_padded)
    students_per_group = len(students_padded)//n_groups
    input =  "groups({}).\n".format(n_groups)
    input += "students({}).\n".format(len(students_padded))
    input += "weeks({}).\n".format(weeks)
    input += "students_per_group({}).\n".format(students_per_group)
    input += facts_met_students(past_groups_padded,n_groups)
    with open(filename,'w') as f:
        f.write(input)
        f.close()

### if the number of students is not divisible by n_groups, add pad students 
def pad_students(students,n_groups):
    resdiv = len(students)//n_groups
    remainder = len(students)%n_groups
    print(resdiv-remainder)
    students_padded = students
    if remainder > 0:
        for i in range(resdiv-remainder):
            students_padded.append(len(students)+i)
        return students_padded

### add a group of the padded students, such that it is penalized to put more than one pad per group 
### (to avoid unbalanced groups)
def pad_groups(past_groups,students,students_padded):
    past_groups_padded = past_groups
    padded = students_padded[len(students):]
    if len(padded)>0:
        past_groups_padded.append(padded)
    return past_groups_padded

def facts_met_students(past_groups_padded,n_groups):
    result = ""
    curr_group = []
    for week_id,group in enumerate(past_groups_padded):
        group.sort()
        print(group)
        for i,student1 in enumerate(group):
            for j in range(i+1,len(group)):
                student2 = group[j]
                result += "meets({},{},{}).\n".format(student1,student2,week_id*-1)
    return result



create_input_file(filename="input.lp")




ctl = clingo.Control()
ctl.load('./input.lp')
ctl.load('./solver.lp')
ctl.ground([("base", [])], context=Context())

with ctl.solve(on_model=on_model, async_=True) as handle:
    handle.wait(time_limit)
    handle.cancel()
    print("++++++++++++++++++TIMEOUT+++++++++++++++++++++++")
    # print (handle.get())
print("Cost of Final solution is ",cost)
print(solution)

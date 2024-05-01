import clingo
import os,sys
from os.path import join as joinp

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

past_groups = [
    [0, 1, 2, 3, 4],     # Group 1: 5 members
    [5, 6, 7, 8, 9],     # Group 2: 5 members
    [10, 11, 12, 13, 14],# Group 3: 5 members
    [15, 16, 17, 18, 19],# Group 4: 5 members
    [20, 21, 22, 23, 24, 25], # Group 5: 6 members
    [26, 27, 28, 29, 30, 31], # Group 6: 6 members
    [32, 33, 34, 35, 36, 37]  # Group 7: 6 members
]
weeks = 1
n_groups = 6

class Context:
    def id(self, x):
         return x
    def seq(self, x, y):
         return [x, y]

def on_model(m):
    if str(m) == "":
        print("INSTANCE OK, NO VIOLATION DETECTED")
    else:
        print("VIOLATION DETECTED:")
        print(m)


def create_pair_list():
    pair_list = [[] for _ in range(len(students))]
    for group in groups:
        for id in group:
            break
            
def create_input_file(filename="input.lp"):
    students_padded = pad_students(students,n_groups)
    past_groups_padded = pad_groups(past_groups,students,students_padded)
    students_per_group = len(students_padded)//n_groups
    input =  "n_of_groups({}).\n".format(n_groups)
    input += "n_of_students({}).\n".format(len(students_padded))
    input += "weeks({}).\n".format(weeks)
    input += "students_per_group({}).\n".format(students_per_group)
    input += facts_met_students(past_groups_padded,n_groups)
    return input

### if the number of students is not divisible by n_groups, add pad students 
def pad_students(students,n_groups):
    remainder = len(students)/n_groups
    students_padded = students
    for i in range(remainder):
        students_padded.append(len(students)+i)

### add a group of the padded students, such that it is penalized to put more than one pad per group 
### (to avoid unbalanced groups)
def pad_groups(past_groups,students,students_padded):
    past_groups_padded = past_groups
    padded = students_padded[len(students)]
    if len(padded)>0:
        past_groups_padded.append(padded)
    return past_groups_padded

def facts_met_students(past_groups_padded,n_groups):
    result = ""
    curr_group = []
    for week_id,group in enumerate(past_groups_padded):
        curr_group = group.sort()
        for i,student1 in enumerate(curr_group):
            for j in range(i+1,len(curr_group)):
                student2 = curr_group[j]
                result += "meets({},{},{}).\n".format(student1,student2,week_id*-1)
    return result
````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def parsedSolution(file):
    outString = ""
    with open(joinp(file)) as f:
        for i, l in enumerate(f.readlines()):
            if i == 0:
                continue
            curr_line = l.strip("\n").replace(" ","")
            row = curr_line.split(",")
            op_id = f"op{row[1]}x{row[2]}x{row[3]}"
            mach_id = f"mach{row[4]}x{row[5]}"
            start = round(float(row[7])*60.0)
            end = round(float(row[8])*60.0)

            outString += f"start({op_id},{start}).\n"
            outString += f"end({op_id},{end}).\n"
            outString += f"onMachine({op_id},{mach_id}).\n"
    return outString

#DATA
# instance = "SMALL"
# solution = "instance.edb"
# instance_folder = f"../data/instances/{instance}"
# solution_file = f"../results/{solution}"
# checker_folder = f"./sol_checker/toCheck/{instance}"

# os.makedirs(checker_folder, exist_ok=True)
# toCheckFile = joinp(checker_folder,solution)

create_input_file(filename="input.lp")

# with open(toCheckFile,"w") as f:
#     f.write(parsedMachines(instance_folder))
#     f.write("\n\n")
#     f.write(parsedJobs(instance_folder))
#     f.write("\n\n")
#     f.write(parsedSolution(solution_file))

# for i in range(1,11):
#     instance_name = "instance{}.edb".format(i)

#     toCheckFile = joinp(checker_folder, instance_name)
#     print(toCheckFile)
#     ctl = clingo.Control()
#     ctl.load(toCheckFile)
#     ctl.load('./sol_checker/checker.asp')
#     ctl.ground([("base", [])], context=Context())
#     ctl.solve(on_model=on_model)


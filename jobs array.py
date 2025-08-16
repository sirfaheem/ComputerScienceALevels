Jobs = 0
NumberOfJobs=0

def Initialise():
    global Jobs
    Jobs = [[-1,-1] for x in range(100)]
    NumberOfJobs = 0

def AddJob(JobNo, Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs==99:
        print("Not Added")
    else:
        Jobs[NumberOfJobs][0] = JobNo
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs+=1
        print("Job Added")

def InsertionSort():
    global Jobs
    global NumberOfJobs
    for x in range(1,NumberOfJobs):
        thisJob = Jobs[x][0]
        thisPriority = Jobs[x][1]
        while x > 0 and Jobs[x-1][1]>thisPriority:
            Jobs[x][0] = Jobs[x-1][0]
            Jobs[x][1] = Jobs[x-1][1]
            x-=1
        Jobs[x][0] = thisJob
        Jobs[x][1] = thisPriority

def PrintArray():
    global Jobs
    global NumberOfJobs
    for x in range(NumberOfJobs):
        print(Jobs[x][0],' priority ',Jobs[x][1])
        
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
PrintArray()
InsertionSort()
#print(Jobs)
print(NumberOfJobs)
PrintArray()

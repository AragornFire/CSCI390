def avg(lst: list) -> int:
    return sum(lst) / len(lst)

def genslices(lst: list) -> list:
    finallst = []
    curr = lst[0]
    curn = 0
    for i in lst:
        if i == curr:
            curn += 1
        else:
            finallst.append(f"{curr}({curn})")
            curr = i
            curn = 1
    finallst.append(f"{curr}({curn})")
    return finallst

Processes = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 5},
    {"pid": "P2", "arrival_time": 1, "burst_time": 3},
    {"pid": "P3", "arrival_time": 2, "burst_time": 1}
]
time_quantum = 2

ttimes = {}
wtimes = {}

currtime = 0
currproc = None
currprocs = []
timeexpd = 0

finallst = []

while True:
    # Add new processes
    for p in Processes:
        if p["arrival_time"] == currtime:
            currprocs.append(p)
            ttimes[p["pid"]] = 0
            wtimes[p["pid"]] = 0
    # For waittime and turnaround
    for proc in currprocs:
        if proc["arrival_time"] < currtime:
            ttimes[proc["pid"]] += 1
            if proc != currproc:
                wtimes[proc["pid"]] += 1
    # Check if Finnish
    if not currprocs and all(p["burst_time"] == 0 for p in Processes):
        break
    # Get a process
    if currproc is None and currprocs:
        currproc = currprocs[0]
        timeexpd = 0
    # Process continues
    if currproc and currproc["burst_time"] > 0:
        finallst.append(currproc['pid'])
        #print(currproc['pid'], ttimes, [i['pid'] for i in currprocs])
        currproc["burst_time"] -= 1
        timeexpd += 1
    # Process death
    if currproc and currproc["burst_time"] == 0:
        currprocs.pop(0)
        currproc = None
        timeexpd = 0
    # Process time's up
    if currproc and timeexpd == time_quantum:
        if currproc["burst_time"] > 0:
            temp = currprocs.pop(0)
            currprocs.append(temp)
        else:
            currprocs.pop(0)  # Already finished
        currproc = None
        timeexpd = 0
    # Time flies when you throw it
    currtime += 1
    #print([i['pid'] for i in currprocs])

#print(finallst)
print("Execution Sequence:", ' -> '.join(genslices(finallst)))
#print("TTimes:", ttimes)
#print("WTimes:", wtimes)
print("Average Waiting Time:", avg(ttimes.values()))
print("Average Turnaround Time:", avg(wtimes.values()))

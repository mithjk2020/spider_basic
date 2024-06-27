def wait_time(proc, n, bt):
    wt = [0] * n
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]
    return wt

def turnaround_time(proc, n, bt, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat

def find_average_time(proc, n, bt):
    wt = wait_time(proc, n, bt)
    tat = turnaround_time(proc, n, bt, wt)
    total_wt = sum(wt)
    total_tat = sum(tat)

    print("Processes  Burst time  Waiting time  Turn around time")
    for i in range(n):
        print("   ", proc[i], "\t\t", bt[i], "\t    ", wt[i], "\t\t  ", tat[i])
    print("Average waiting time = ", total_wt / n)
    print("Average turn around time = ", total_tat / n)

if __name__ == "__main__":
    proc = [1, 2, 3, 4]
    n = len(proc)
    burst_time = [21, 3, 6, 2]
    find_average_time(proc, n, burst_time)

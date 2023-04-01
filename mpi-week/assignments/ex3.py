
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

value = 0
while value >= 0:
    if rank == 0:
        value = int(input("Enter an integer"))
        comm.send(value, dest=rank+1)
    else:
        value = comm.recv(source=rank-1)
        if rank < size - 1:
            if x < 0 : x-=rank
            comm.send(value, dest=rank+1)
    if x<0:
        break
    print("Process %d got %d" % (rank, value))

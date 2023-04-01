
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    value = int(input("Enter an integer : "))
else:
    None
    
value = comm.bcast(value, root=0)
    
print("rank", rank, ", value =", value)

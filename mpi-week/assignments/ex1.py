from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#First question
print("Hello World", rank, size)

#Second question
print("Hello World with the rank {} and the process {}".format(rank, size))

#Third question
if rank == 0:
    
    print("Hello with the rank {} and {} total process".format(rank,size))

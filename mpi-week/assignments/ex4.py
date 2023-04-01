from mpi4py import MPI

cols = 4
rows = 4

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

a = None

nprows = 2
npcols = 2
brows = rows // nprows
bcols = cols // npcols

if rank == 0:
    a = bytearray(range(rows*cols))

if size != nprows*npcols:
    if rank == 0:
        print(f"Error: number of PEs {p} != {nprows} x {npcols}")
    comm.Abort()

b = bytearray(brows * bcols)

blocktype2 = MPI.CHAR.Create_vector(brows, bcols, cols)
blocktype2.Commit()

blocktype = blocktype2.Create_resized(0, 1)
blocktype.Commit()

disps = [i * cols * brows + j * bcols for i in range(nprows) for j in range(npcols)]
counts = [1] * (nprows * npcols)

comm.Scatterv([a, counts, disps, blocktype], b)

for val in range(size):
    if val == rank:
        print(f"Rank = {rank}")
        if rank == 0:
            print("Matrix A:")
            for i in range(rows):
                for j in range(cols):
                    print(f"{a[i*cols+j]:3d}", end=" ")
                print("")
        print("Submatrix process:")
        for i in range(brows):
            for j in range(bcols):
                print(f"{b[i*bcols+j]:3d}", end=" ")
            print("")
        print("")

    comm.Barrier()

blocktype2.Free()
blocktype.Free()

MPI.Finalize()

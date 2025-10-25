import multiprocessing
import time

def n_square():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
def n_cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__=="__main__":
    
    ## create 2 processes
    p1=multiprocessing.Process(target=n_square)
    p2=multiprocessing.Process(target=n_cube)
    t=time.time()
    #Starting the processes
    p1.start()
    p2.start()
    
    ## Wait for the process to complete
    p1.join()
    p2.join()
    
    finished_time=time.time()-t
    print(finished_time)

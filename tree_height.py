# python3

import sys
import threading

def compute_height(n, parents):
    root = None
    position = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root=i 
        else:
            position[parents[i]].append(i)
            
    def max_height(b):
        heigth=1
        if not position[b]:
            return heigth
        else:
            for child in position[b]:    
                heigth=max(heigth,max_height(child))
            return heigth+1    
    return max_height(root)
    
def main():
    text=input("Enter I or F: ")
    if "I" in text:
        n= int(input())
        parents=list(map(int,input().split()))
    elif "F" in text:
        filename=input()    
        file='./test/'+filename
        if "a" not in filename:
            try:
                with open(file) as f:
                    n=int(f.readline())
                    parents=list(map(int,f.readline().split()))
            except Exception as e:
                print("Error:", str(e))
                return
        else:
            print("Error: invalid filename")   
            return  

    print(compute_height(n, parents))                 
 
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))

#merge sort
def mergeSort(nlist):
2	    print("Splitting ",nlist)
3	    if len(nlist)>1:
4	        mid = len(nlist)//2
5	        lefthalf = nlist[:mid]
6	        righthalf = nlist[mid:]
7	
8	        mergeSort(lefthalf)
9	        mergeSort(righthalf)
10	        i=j=k=0       
11	        while i < len(lefthalf) and j < len(righthalf):
12	            if lefthalf[i] < righthalf[j]:
13	                nlist[k]=lefthalf[i]
14	                i=i+1
15	            else:
16	                nlist[k]=righthalf[j]
17	                j=j+1
18	            k=k+1
19	
20	        while i < len(lefthalf):
21	            nlist[k]=lefthalf[i]
22	            i=i+1
23	            k=k+1
24	
25	        while j < len(righthalf):
26	            nlist[k]=righthalf[j]
27	            j=j+1
28	            k=k+1
29	    print("Merging ",nlist)
30	
31	nlist = [14,46,43,2]
32	mergeSort(nlist)
33	print(nlist)
#codded by chithra

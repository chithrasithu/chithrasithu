lis =list(map(int,input().split()))
search_input=int(input())
lis.sort()
low=0
high=len(lis)
def bin(lis,low,high):
  mid=low+high//2
  if search_input == lis[mid]:
    print(search_input,"element found")
  elif lis[mid] > search_input:
    bin(lis,low,mid-1)
  elif lis[mid] < search_input:
    bin(lis,mid+1,high)
bin(lis,low,high)

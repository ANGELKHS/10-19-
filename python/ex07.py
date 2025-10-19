a=list(map(int,input().split()))
b=min(a)
c=max(a)

filtered=[x for x in a if x !=b and x !=c]
total=sum(filtered)

print(total)
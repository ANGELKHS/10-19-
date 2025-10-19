prices=input().split(";")
prices=list(map(int,prices))
prices.sort(reverse=True)

for price in prices:
  print(str(price).rjust(9))
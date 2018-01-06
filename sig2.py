def sum(num):
    n=len(num)
    count = 0
    for i in range(n):
        #print i
        for j in range(i+1,n):
            for k in range (n):
                if num[i]+num[j]==num[k]:
                   count = count+1
    return count



with open('data1.txt') as f:
  testcase = [ int(x) for x in f.read().split(',')]
nos= sum(testcase)
if nos >0:
	print "Total possible combinations " +str(nos)
else :
      print "Not Exists"

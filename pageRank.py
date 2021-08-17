import numpy as np
import json

def matrixMul(a, n):
    if(n <= 1):
        return a
    else:
        return np.dot(matrixMul(a, n-1), a)

#read input file.
link=[]
with open("./summary.json","r") as f:
  link=json.load(f)

#initialize original transition matrix
original_transition=np.zeros((len(link),len(link)))
for i in range(len(link)):
  for o in link[i]:
    original_transition[i][o]=1
#normalize original transition matrix, avoid divide by 0.
totalLink=np.sum(original_transition,axis=0)
for i in range(len(link)):
    if(totalLink[i]==0):
        totalLink[i]=1
original_transition=original_transition/totalLink

print("Original transition matrix",original_transition)

initial_vector=np.ones(len(link))/len(link)
ordering_of_websites=np.zeros(len(link))
##########
#Todo: please implement pagerank algorithm and turn ordering_of_websites into a list representing the web pages. The order should be based on pagerank algorithm. The web page with a higher probability comes first.

M = 0.15 * np.ones([len(link),len(link)])/len(link) + 0.85 * original_transition
R = np.dot(matrixMul(M, 50), initial_vector)
ordering_of_websites = np.argsort(R)[::-1]

##########
print("R",R)
print("Your current answer",ordering_of_websites)

#turn your answer from a numpy array to list and output it as a json file.
ordering_of_websites=ordering_of_websites.tolist()
with open("answer.json","w") as f:
    json.dump(ordering_of_websites,f)

import pandas as pd
import statistics as st

data = pd.read_csv("StudentsPerformance.csv")
math = data["math score"]

mean = st.mean(math)
mode = st.mode(math)
sd = st.stdev(math)

fdfirst,fdlast = mean-sd, mean+sd
sdfirst,sdlast = mean-2*sd, mean+2*sd
tdfirst,tdlast = mean-3*sd, mean+3*sd

fdlist = [i for i in math if fdfirst<i<fdlast]
sdlist = [i for i in math if sdfirst<i<sdlast]
tdlist = [i for i in math if tdfirst<i<tdlast]

print("The mean for this dataset is", mean)
print("The mode for this dataset is", mode)
print("The standard deviation for this dataset is", sd)

print("{}% of data is in the first region".format(((len(fdlist)/len(math)*100.0))))
print("{}% of data is in the first region".format(((len(sdlist)/len(math)*100.0))))
print("{}% of data is in the first region".format(((len(tdlist)/len(math)*100.0))))

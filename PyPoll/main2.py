import csv

with open('election_data_1.csv') as csvfile:
    election_1=csv.reader(csvfile, delimiter=",")
    next(election_1)

    Voter_ID=[]
    County=[]
    Total_Candidates=[]
    Candidates=[]
    Candidate_Vote=[]
    Percent_Candidate_Vote=[]

    for row in election_1:
        Voter_ID.append(row[0])
        Total_Candidates.append(row[2])


    from collections import Counter
    New_List=Counter(Total_Candidates)
    for k,v in New_List.items():
        Candidates.append(k)
        Candidate_Vote.append(v)

for votes in Candidate_Vote:
    PercentVote=(votes/sum(Candidate_Vote))*100
    Percent_Candidate_Vote.append(PercentVote)

percent_winner= max(Percent_Candidate_Vote)
index_winner=Percent_Candidate_Vote.index(percent_winner)
Winning_Human_Candidate=Candidates[index_winner]

# print(Candidates)
# print(Candidate_Vote)
# print(sum(Candidate_Vote))
# print(Percent_Candidate_Vote)


print("Election Results")
print("----------------")
print("Total Votes: ", sum(Candidate_Vote))
print("----------------")
print(Candidates[0],":", Percent_Candidate_Vote[0], "%","(",Candidate_Vote[0],")")
print(Candidates[1],":", Percent_Candidate_Vote[1], "%","(",Candidate_Vote[1],")")
print(Candidates[2],":", Percent_Candidate_Vote[2], "%","(",Candidate_Vote[2],")")
print(Candidates[3],":", Percent_Candidate_Vote[3], "%","(",Candidate_Vote[3],")")
print("----------------")
print("Winner: " , Winning_Human_Candidate)











    
        
 
    
        






candidate1=input("enter Ist candidate name:")
candidate2=input("enter seceond candidate name:")
cand1_votes =0
cand2_votes =0
voter_id=[101,102,103,104,105,106]
no_of_voters=len(voter_id)
print("number of voters :-",no_of_voters)
voted=[]
while True:
    if voter_id==[]:
        print("voting over ")
        if cand1_votes>cand2_votes:
            print(f"{candidate1} won the election with{cand1_votes}")
        elif cand2_votes>cand1_votes:
            print(f"{candidate2} won the election with {cand2_votes}")    
        elif cand1_votes==cand2_votes:
            print("tied!!!")
        print("Voting is successful!!")
        break 
    else:
        voter=int(input("enter your id :-"))
        if voter in voted:
            print("you already voted")
        else:
            if voter in voter_id:
                print(f"1.{candidate1}\n2.{candidate2}")
                choice=int(input("enter your choice:"))
                if choice ==1:
                    cand1_votes+=1
                    print(f"you voted {candidate1} ")
                elif choice==2 :
                    cand2_votes+=1
                    print(f"you voted {candidate2} ")
                voter_id.remove(voter)
                voted.append(voter)  
            else:
                print("you are not allowed ")  


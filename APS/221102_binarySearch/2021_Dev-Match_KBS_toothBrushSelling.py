def solution(enroll, referral, seller, amount):
    temp = [0] * len(enroll)
    answer = [0] * len(enroll)
    members = dict()
    for i in range(len(enroll)):
        members[enroll[i]] = i
    
    for i in range(len(seller)):
        temp[members[seller[i]]] = amount[i]*100
        person = members[seller[i]]
        while referral[person] != "-" and temp[person] > 0:
            answer[person] += temp[person]- temp[person]//10
            temp[members[referral[person]]] += temp[person]//10
            temp[person] = 0
            person = members[referral[person]]
        answer[person] += temp[person]- temp[person]//10
        temp[person] = 0
        #print(answer, temp)
    return answer







enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
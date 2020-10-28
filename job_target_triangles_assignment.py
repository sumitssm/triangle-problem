max_number_list=[]
numbers=[]
index_1=0
index_2=0

with open('triangle.txt', 'r') as f:
    for line in f:
        line=line.split()
        numbers.append(line)
        
for number in numbers:
    temp_list=[]
    if len(number)<=1:
       n=map(int, number)
       max_number=max(n)
       max_number_list.append(max_number)
    else:
       index_1=current_index
       index_2=current_index+1
       temp_list.append(number[index_1])
       temp_list.append(number[index_2])
       n=map(int, temp_list)
       max_number=max(n)
       max_number_list.append(max_number)
    current_index=number.index(str(max_number))
    
final_number=sum(max_number_list)
print(final_number)   

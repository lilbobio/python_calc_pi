import csv


index = 0
ratio_total = 0
sequence_num = 0
all_flips = []

with open('flips.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    header = next(reader)
    for row in reader:
        all_flips.append(row['LANDED'])
       
for i in range(len(all_flips)):
    head_count = 0
    flip_count = 0
    
    for flip in all_flips[i:]:
        if flip == "h":
            head_count += 1

        flip_count += 1

        if head_count > 0.5*flip_count:
            this_ratio = head_count/flip_count
            ratio_total += this_ratio
            sequence_num += 1
            break
        
        
        

pi_val = (ratio_total/sequence_num)*4

print(f"pi = {pi_val}")
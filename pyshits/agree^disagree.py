
array = [];
cntr = 2;
agree_cntr = 0;
sagree_cntr = 0;
neutral_cntr = 0;
disagree_cntr = 0;
sdisagree_cntr = 0;

for x in range(25):
    text = "Enter the input {}: ";
    print(text.format(cntr));
    temp = input();
    array.append(temp);
    cntr += 1;

for i in array:
    if(i =="agree"):
        agree_cntr+=1;
    elif(i =="sagree"):
        sagree_cntr+=1;
    elif(i =="neutral"):
        neutral_cntr+=1;
    elif(i =="dsagree"):
         disagree_cntr+=1;
    elif(i =="sdsagree"):
        sdisagree_cntr+=1;
    else:
        print("**** you. Repeat.");

print("Strongly Agree: ", sagree_cntr);
print("Agree: ", agree_cntr);
print("Neutral: ", neutral_cntr);
print("Disagree: ", disagree_cntr);
print("Strongly Disagree: ", sdisagree_cntr);

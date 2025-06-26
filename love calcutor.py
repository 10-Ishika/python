name1=input("enter the name:")
name2=input("enter the name:")
combined=name1+name2
lower_letter=combined.lower()

t=lower_letter.count('t')
r=lower_letter.count('r')
u=lower_letter.count('u')
e=lower_letter.count('e')
true=t+r+u+e

l=lower_letter.count('l')
o=lower_letter.count('o')
v=lower_letter.count('v')
e=lower_letter.count('e')
love=l+o+v+e

love_score=true +love
if love_score<10 or love_score>90:
    print(f"your score is{love_score} and you both are luck")
elif love_score>=40 and love_score<=50:
    print(f"your score is{love_score} and you both are good")
else:
    print("nice")
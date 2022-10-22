# # dict_compre = [new_key: new_value for item in list]
# # dict_compre = [new_key: new_value for(key, value) in dict.items() if test]
# names=['ALex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

#Copy Paste your code below this line 👇
#Then click "Run" to execute the teslist ts
arr = list(map(str, sentence.split()))
result = {x: len(x) for x in arr}


print(result)
#Grading program
""" student_scores={
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for student in student_scores:
    score =student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades [student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
 """
#diction in list
""" travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
]
def add_new_country(country_visited,times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["times"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("Viet Nam",12,["Da Nang", "Hai Phong", "Nha trang"])
print(travel_log)

 """
bids = {}
continue_check = True
def highest_bid(bids):
    winner=""
    highest_price = 0
    for person in bids:
        if(bids[person]>highest_price):
            
            winner = person
            highest_price = bids[person]
    print(f"The winner is {winner} with the price {highest_price}$")
while (continue_check):
    name = input("What's your name?")
    price = int(input("What's your bid?"))
    bids[name] = price
    check = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if(check == "no"):
        continue_check=False
highest_bid(bids)


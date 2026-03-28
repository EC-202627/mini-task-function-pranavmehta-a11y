def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)

user_input = input()

last_space_index = user_input.rfind(" ")

title = user_input[:last_space_index]
days_str = user_input[last_space_index + 1:]
days = int(days_str)

result = calculate_fine(title, days)

print("Book:", title, "Days overdue:", days, "Fine: Rs.", result)

if result >= 150.0:
    print("You have accumulated the maximum fine of INR: 150.0")
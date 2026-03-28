def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)

user_input = input()
parts = user_input.split()

title = " ".join(parts[:-1])
days = int(parts[-1])

result = calculate_fine(title, days)

print("Book:", title, "Days overdue:", days, "Fine: Rs.", result, end="")

if result >= 150.0:
    print(" You have accumulated the maximum fine of INR: 150.0")

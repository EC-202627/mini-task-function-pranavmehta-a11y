def calculate_fine(book_title, days_overdue, daily_rate, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)


user_input = input()
parts = user_input.split()

title = " ".join(parts[:-2])
days = int(parts[-2])
rate = float(parts[-1])

result = calculate_fine(title, days, rate)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", result)
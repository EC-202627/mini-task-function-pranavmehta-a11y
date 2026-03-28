def calculate_fine(book_title, days_overdue, daily_rate, max_fine):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)

title = input()
days = int(input())
rate = float(input())
max_fine = float(input())

result = calculate_fine(title, days, rate, max_fine)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", result)
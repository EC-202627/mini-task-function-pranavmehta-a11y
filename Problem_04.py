def calculate_fine(book_title, days_overdue, daily_rate, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)


title = input()
days = int(input())
rate = float(input())

result = calculate_fine(title, days, rate)

print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", result)
def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)


title = input()
days = int(input())

result = calculate_fine(title, days)

print(f"Book: {title}, Days overdue: {days}, Fine: Rs. {result}")

if result >= 150.0:
    print("You have accumulated the maximum fine of INR: 150.0")
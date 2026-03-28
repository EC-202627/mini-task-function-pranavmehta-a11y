
def calculate_fine(book_title, days_overdue, daily_rate, max_fine):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
        
    return float(fine)


# Input (single line)
user_input = input()
parts = user_input.split()

title = " ".join(parts[:-3])
days = int(parts[-3])
rate = float(parts[-2])
max_fine = float(parts[-1])

# Calculate
result = calculate_fine(title, days, rate, max_fine)

# Output (MULTI-LINE)
print("Book:", title)
print("Days overdue:", days)
print("Fine: Rs.", result)
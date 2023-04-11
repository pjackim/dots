from datetime import datetime, timedelta
import calendar

def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.strptime(date_str, '%m/%d/%Y')
            return date_obj
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'mm/dd/yyyy'.")

def get_difference_input():
    while True:
        try:
            difference_str = input("Enter the difference as days, months, and years separated by spaces (e.g. 1 2 3): ")
            days, months, years = map(int, difference_str.split())
            return days, months, years
        except ValueError:
            print("Invalid difference format. Please enter the difference as days, months, and years separated by spaces (e.g. 1 2 3).")

def calculate_new_date(date_obj, days, months, years):
    new_date = date_obj + timedelta(days=days) + timedelta(days=months*30) + timedelta(days=years*365)
    return new_date.strftime('%m/%d/%Y')

def print_month_calendar_with_bold(year, month, day):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    
    print()
    print(f"{calendar.month_name[month]} {year}".center(20), f"{month}/{day}/{year}")
    print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", sep=f' {"│"} ')
    print("─"*3, "┼────"*6,sep="")

    for w in month_days:
        week_str = ""
        for d in w:
            if d == day:
                day_str = f"\033[7m\033[5m{d:2}\033[0m"  # Bold formatting
            elif d == 0:
                day_str = "  "
            else:
                day_str = f"{d:2}"
            week_str += day_str + f' {"│"} '
        print(week_str[:-3])
        # print(PrintUtil.line(32))
        print("─"*3, "┼────"*6,sep="")
        
if __name__ == '__main__':
    input_date = get_date_input("Enter the initial date (mm/dd/yyyy): ")
    days_diff, months_diff, years_diff = get_difference_input()

    new_date = calculate_new_date(input_date, days_diff, months_diff, years_diff)
    print_month_calendar_with_bold(int(new_date[6:]), int(new_date[0:2]), int(new_date[3:5]), )

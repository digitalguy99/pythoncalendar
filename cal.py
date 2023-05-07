import calendar
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('-y', '--year', type=int, required=False)
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument
# print('Hello,', args.name)

class CustomCalendar(calendar.TextCalendar):
    def formatday(self, day, weekday, width):
        if day == 0:
            return ' ' * width
        if day == datetime.now().day:
            return f'\033[7m{day:>{width}}\033[m'
        return f'{day:>{width}}'

def cal(month=None, year=None):
    if not month:
        month = datetime.now().month
    if not year:
        year = datetime.now().year
    cal = CustomCalendar()
    print(cal.formatmonth(year, month))

# cal()

# input_year = int(input("Input year: "))

def print_calendar(year: int):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    today = datetime.now()
    print(f"{'Year ' + str(year):^66}\n")
    for quarter in range(4):
        quarter_str = []
        for month in range(1 + quarter * 3, 4 + quarter * 3):
            month_str = cal.formatmonth(year, month).split('\n')
            for i in range(len(month_str)):
                if i == 0:
                    month_str[i] = f"{calendar.month_name[month]:^20}"
                elif i > 1:
                    days = month_str[i].split()
                    if len(days) > 0:
                        if i == 2 and len(days) < 7:
                            days = ['  '] * (7 - len(days)) + days
                        elif i == len(month_str) - 2 and len(days) < 7:
                            days += ['  '] * (7 - len(days))
                        for j in range(len(days)):
                            if days[j].strip():
                                if year == today.year and month == today.month and int(days[j]) == today.day:
                                    days[j] = f'\033[30;47m{days[j]:>2}\033[0m'
                        month_str[i] = ' '.join(['{:>2}'.format(day) for day in days])
            if not quarter_str:
                quarter_str.extend(month_str)
            else:
                for i in range(len(month_str)):
                    if i >= len(quarter_str):
                        stbp = quarter_str[-1].lstrip()
                        stbp_idx = quarter_str[-1].index(stbp)
                        s_no = (stbp_idx)/3
                        quarter_str[-1] = ' '*(40 if s_no == 2 else 20) + quarter_str[-1]
                        quarter_str.append('   ' + month_str[i])
                    else:
                        quarter_str[i] += '   ' + month_str[i]
        print('\n'.join(quarter_str))

if args.year:
    print_calendar(args.year)
else:
    cal()
# print_calendar(input_year)
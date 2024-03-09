import calendar
import argparse
import sys
import os
from datetime import datetime

# Setting calendar start day
calendar.setfirstweekday(calendar.SUNDAY)

# Allowing flags to be passed during execution
parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', action='append', type=int, required=False)
parser.add_argument('-m', '--month', action='append')
parser.add_argument('-v', '--version', action='store_true')
args = parser.parse_args()

# Setting variables
cal_month, cal_year = None, None
program_version = "4.0.2"

if args.month:
    if len(args.month) > 1:
        print(f"{os.path.basename(sys.argv[0])}: error: argument -m/--month: too many arguments: 1 expected but given {len(args.month)}")
        sys.exit()
    else:
        month_string = args.month[0]
        if month_string not in [str(month_number) for month_number in range(1,13)]:
            try:
                cal_month = list(calendar.month_name).index(month_string.capitalize())
            except:
                try:
                    cal_month = list(calendar.month_abbr).index(month_string.capitalize())
                except:
                    print(
                        "Enter appropriate month number or 3-letter/full name!",
                        f"{os.path.basename(sys.argv[0])}: error: argument -m/--month: invalid entry: '{month_string}'",
                        sep='\n'
                    )
                    sys.exit()
        else:
            cal_month = int(month_string)

if args.year:
    if len(args.year) > 1:
        print(f"{os.path.basename(sys.argv[0])}: error: argument -y/--year: too many arguments: 1 expected but given {len(args.year)}")
        sys.exit()
    else:
        cal_year = args.year[0]

# Creating custom calendar
class CustomCalendar(calendar.TextCalendar):
    def formatday(self, day, weekday, width):
        if day == 0:
            return ' ' * width
        if day == datetime.now().day:
            return f'\033[7m{day:>{width}}\033[m'
        return f'{day:>{width}}'

# Function to print month calendar
def cal(month=None, year=None):
    if not month:
        month = datetime.now().month
    if not year:
        year = datetime.now().year
    cal = CustomCalendar(calendar.SUNDAY)
    print(cal.formatmonth(year, month))

# Function to print full year calendar
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
                        elif (i == len(month_str)-2) and (len(days) < 7):
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
                        if i != (len(month_str)-1):
                            quarter_str[i] += '   ' + month_str[i]
                        else:
                            if len(month_str) >= len(quarter_str):
                                quarter_str[i] += '   ' + month_str[i]
                            else:
                                quarter_str[i] += 20*' ' + '   ' + month_str[i]
        print('\n'.join(quarter_str))

# Code to determine what to print out
if cal_month and cal_year:
    if cal_month == datetime.now().month and cal_year == datetime.now().year:
        cal()
    else:
        print(calendar.month(cal_year, cal_month))
elif cal_year:
    print_calendar(cal_year)
elif cal_month:
    if cal_month != datetime.now().month:
        print(calendar.month(datetime.now().year, cal_month))
    else:
        cal()
elif args.version:
    print(f"pythoncalendar v{program_version}", f"© {datetime.now().year} digitalguy99", sep='\n')
else:
    cal()
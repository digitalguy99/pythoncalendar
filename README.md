# pythoncalendar
Linux inspired cli calendar program brought to life on Windows with Python

*Requirement: any **Windows** version*

## Preview
![image](https://github.com/digitalguy99/pythoncalendar/assets/52367722/1899d730-c8ec-4ca5-ae79-f0a557a205c8)


## Installation
1. Open preferred console application.

2. Copy, paste and run the following:

   ```cmd
   cmd /v /c "IF EXIST %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe (set /p userinp=File already exists. Do you want to overwrite it? ^(y/n^) & IF /I !userinp! == y curl -kL -o %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe https://github.com/digitalguy99/pythoncalendar/releases/download/v4.0.2/cal.exe) ELSE curl -kL -o %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe https://github.com/digitalguy99/pythoncalendar/releases/download/v4.0.2/cal.exe"
   ```

3. Restart your console.

4. If you are facing any problem, check the [Troubleshooting](#troubleshooting) section.

## Uninstalling

Copy, paste and run the following:

```cmd
cmd /c "for /f "delims=" %i in ('where cal') do del "%i""
```

## Usage
```cmd
usage: cal [-h] [-y YEAR] [-m MONTH]

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
  -m MONTH, --month MONTH
```
or simply:
```cmd
cal -y <yyyy> -m <month full name or number>
```
### Examples
* Displaying calendar of current date
  ```cmd
  $ cal
  ```

* Displaying 1997 full year calendar
  ```cmd
  $ cal -y 1997
  ```

* Displaying March calendar of current year
  ```cmd
  $ cal -m March
  ```

* Displaying calendar of March 1997
  ```cmd
  $ cal -m March -y 1997
  ```

## Update
1. Run the [installation command](#installation).

2. Type `y` and press enter when prompted the following:
   > Do you want to overwrite it? (y/n)

3. Restart your console.

## Troubleshooting
If you are seeing some garbled characters on the calendar, try pasting and running the following:
```cmd
cmd /c "reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f"
```
Then restart your console application.

## License
© 2024 digitalguy99. This project is licensed under the terms of the MIT license.
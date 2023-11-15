# pythoncalendar
Linux inspired cli calendar program brought to life on Windows with Python

## Preview
*Requirement: any **Windows** version*

## Installation
1. Open preferred console application.

2. Copy and paste the following:

   ```cmd
   cmd /v /c "IF EXIST %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe (set /p userinp=File already exists. Do you want to overwrite it? ^(y/n^) & IF /I !userinp! == y curl -kL -o %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe https://github.com/digitalguy99/pythoncalendar/releases/download/v1.0.0/cal.exe) ELSE curl -kL -o %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\cal.exe https://github.com/digitalguy99/pythoncalendar/releases/download/v1.0.0/cal.exe"
   ```

3. Restart your console.

## Usage
```cmd
usage: cal [-h] [-y YEAR] [-m MONTH]

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR
  -m MONTH, --month MONTH
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
1. Run the installation command.

2. Type `y` and press enter when prompted the following:
   > Do you want to overwrite it? (y/n)

3. Restart your console.


## License
© 2023 digitalguy99. This project is licensed under the terms of the MIT license.

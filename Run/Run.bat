@Echo off

echo "Welcome to GNU+Cards!"
echo "====================="

echo bc_Max is:
echo wc_Max is:

::for /f "userbackq" %b in (`type ..\main\bc ^| fidn "" /v /c`) do (
::	echo line count is %b
::)

::::findstr /R /N "^" ..\Main\bc | find /C ":"
Find /C ":" << ..\Main\bc

set /a rand=((%random%bc_Max/32768) + 1)
findstr /n . ..\Main\bc | findstr "^%rand%:"

set /a rand=%random:~2%
findstr /n . ..\Main\wc | findstr "^%rand%:"

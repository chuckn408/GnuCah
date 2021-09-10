echo "Welcome to GNU+Cards!"

@echo off
for /f "delims=" %%a in (../Main/bc) DO ( 
  ECHO Line is: %%a
)
@echo off
for /f "delims=" %%a in (../Main/wc) DO ( 
  ECHO Line is: %%a
)

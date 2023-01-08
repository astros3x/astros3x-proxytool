@echo off
color c
title IP Pinger ~2Loop#6969
type main\title.py
echo.
set /p ip=IP here:
echo.
echo [#] Status:
echo.
:top
PING -n 1 %ip% | FIND "TTL="
if errorlevel  1 (echo [+] %ip% is offline)
if not errorlevel 1 (echo [-] %ip% is online)
color c
ping -t 2 0 10 127.0.0.1 >nul
color 9
ping -t 2 0 10 127.0.0.1 >nul
color d
ping -t 2 0 10 127.0.0.1 >nul
goto top
pause
exit
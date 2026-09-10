@echo off
chcp 65001 >nul
title Android TV ADB Installer - Windows
cd /d "%~dp0"

where adb >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Chưa tìm thấy adb trong PATH. Đang kiểm tra platform-tools cục bộ...
    if not exist "adb.exe" (
        echo [*] Đang tự động tải Google Platform Tools...
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip' -OutFile 'pt.zip'; Expand-Archive 'pt.zip' -DestinationPath 'temp_pt' -Force; Copy-Item 'temp_pt\platform-tools\*' '.' -Force; Remove-Item 'pt.zip', 'temp_pt' -Recurse -Force"
    )
    set "PATH=%CD%;%PATH%"
)

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Máy tính chưa cài Python. Vui lòng cài Python 3 từ Microsoft Store hoặc https://python.org.
    pause
    exit /b 1
)

python installer.py
pause

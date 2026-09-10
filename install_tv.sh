#!/bin/bash
# Android TV ADB Installer - Unified Launcher
# Tu dong kiem tra moi truong va khoi chay cong cu moi nhat

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

# Cai dat dependencies tren Termux / Debian neu thieu
if ! command -v adb &> /dev/null || ! command -v python3 &> /dev/null; then
    echo "[*] Dang kiem tra va cai dat goi bo tro..."
    if command -v pkg &> /dev/null; then
        pkg update -y && pkg install -y android-tools python git
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y adb python3 git
    fi
fi

PY="python3"
if ! command -v python3 &> /dev/null; then
    PY="python"
fi

exec $PY "$DIR/installer.py" "$@"

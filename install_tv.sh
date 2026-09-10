#!/bin/bash
# ATV ADB Installer - Cài ứng dụng từ Điện thoại lên Android TV qua ADB WiFi
# ponytail: bash script dùng curl + adb cơ bản, nâng cấp GUI khi cần

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JSON_FILE="$DIR/apps.json"

# Kiểm tra adb
if ! command -v adb &> /dev/null; then
    echo "[!] Không tìm thấy adb. Đang cài đặt..."
    if command -v pkg &> /dev/null; then
        pkg install -y android-tools jq curl
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y adb jq curl
    else
        echo "[ERROR] Vui lòng cài đặt ADB trước!"
        exit 1
    fi
fi

# Tải apps.json nếu chưa có cục bộ
if [ ! -f "$JSON_FILE" ]; then
    echo "[*] Đang tải danh sách app..."
    curl -sL "https://raw.githubusercontent.com/nguyenlocthanh796/android-tv-adb-installer/main/apps.json" -o "$JSON_FILE" || {
        echo "[ERROR] Không tải được apps.json!"
        exit 1
    }
fi

echo "=============================================="
echo "    ATV ADB INSTALLER - PHONE TO TV           "
echo "=============================================="

# Nhập IP Tivi
read -p "Nhập địa chỉ IP của Android TV (vd 192.168.1.50): " TV_IP
if [ -z "$TV_IP" ]; then
    echo "[!] IP không hợp lệ!"
    exit 1
fi

echo "[*] Đang kết nối tới $TV_IP:5555..."
adb disconnect >/dev/null 2>&1 || true
adb connect "$TV_IP:5555"

echo "[*] Vui lòng nhìn màn hình TV và bấm 'Cho phép / Always allow' nếu có hộp thoại xuất hiện..."
sleep 2

adb devices

install_apk() {
    local name="$1"
    local url="$2"
    if [ -z "$url" ] || [ "$url" = "null" ]; then
        echo "[!] Không có link APK trực tiếp cho $name"
        return
    fi
    echo "----------------------------------------------"
    echo "[*] Đang tải: $name"
    TMP_APK="/tmp/atv_temp.apk"
    rm -f "$TMP_APK"
    curl -L -# "$url" -o "$TMP_APK"
    echo "[*] Đang cài đặt lên TV..."
    adb -s "$TV_IP:5555" install -r -d "$TMP_APK" || adb install -r -d "$TMP_APK"
    rm -f "$TMP_APK"
    echo "[✓] Cài đặt thành công: $name"
}

combo_install() {
    echo "[*] Bắt đầu cài gói ứng dụng phổ biến:"
    # SmartTube, Phim4K, TiviMate, Downloader, Xplorer
    python3 -c "
import json
with open('$JSON_FILE', encoding='utf-8') as f:
    apps = json.load(f)
target_names = ['smart tube', 'phim4k tv', 'tivimate_v5.1.6', 'downloader_aftv_v1.5.3', 'xplorer_file_manager']
for a in apps:
    for t in target_names:
        if t in a['name'].lower() and a.get('direct_url'):
            print(f\"{a['name']}|{a['direct_url']}\")
            break
" | while IFS='|' read -r aname aurl; do
        install_apk "$aname" "$aurl"
    done
}

while true; do
    echo ""
    echo "================ MENU ================"
    echo "1. Cài Combo xem phim + truyền hình + Youtube chặn QC"
    echo "2. Tìm kiếm ứng dụng theo tên để cài"
    echo "3. Xem danh sách theo Danh mục và chọn cài"
    echo "4. Nhập trực tiếp link APK để cài"
    echo "0. Thoát"
    read -p "Chọn chức năng [0-4]: " choice

    case "$choice" in
        1)
            combo_install
            ;;
        2)
            read -p "Nhập từ khóa tìm kiếm (vd: youtube, bóng đá, bóng đá): " kw
            python3 -c "
import json, sys
kw = '$kw'.lower()
with open('$JSON_FILE', encoding='utf-8') as f:
    apps = json.load(f)
results = [a for a in apps if kw in a['name'].lower() or kw in a['category'].lower()]
if not results:
    print('Không tìm thấy app phù hợp!')
    sys.exit(0)
for i, a in enumerate(results):
    print(f\"{i+1}. [{a['category']}] {a['name']} ({a.get('meta','')})\")
sel = input('Chọn số thứ tự app để cài (hoặc Enter bỏ qua): ')
if sel.isdigit() and 1 <= int(sel) <= len(results):
    app = results[int(sel)-1]
    print(f\"SELECTED|{app['name']}|{app['direct_url']}\")
" | while IFS='|' read -r prefix aname aurl; do
                if [ "$prefix" = "SELECTED" ]; then
                    install_apk "$aname" "$aurl"
                else
                    echo "$prefix"
                fi
            done
            ;;
        3)
            python3 -c "
import json
with open('$JSON_FILE', encoding='utf-8') as f:
    apps = json.load(f)
cats = sorted(list(set(a['category'] for a in apps)))
for i, c in enumerate(cats):
    print(f\"{i+1}. {c}\")
c_idx = input('Chọn danh mục [1-' + str(len(cats)) + ']: ')
if c_idx.isdigit() and 1 <= int(c_idx) <= len(cats):
    cat_name = cats[int(c_idx)-1]
    cat_apps = [a for a in apps if a['category'] == cat_name]
    for j, a in enumerate(cat_apps):
        print(f\"  {j+1}. {a['name']} ({a.get('meta','')})\")
    a_idx = input('Chọn số app để cài (hoặc A để cài toàn bộ danh mục): ')
    if a_idx.upper() == 'A':
        for a in cat_apps:
            if a.get('direct_url'):
                print(f\"INSTALL|{a['name']}|{a['direct_url']}\")
    elif a_idx.isdigit() and 1 <= int(a_idx) <= len(cat_apps):
        a = cat_apps[int(a_idx)-1]
        print(f\"INSTALL|{a['name']}|{a['direct_url']}\")
" | while IFS='|' read -r action aname aurl; do
                if [ "$action" = "INSTALL" ]; then
                    install_apk "$aname" "$aurl"
                else
                    echo "$action"
                fi
            done
            ;;
        4)
            read -p "Dán đường dẫn trực tiếp file APK: " custom_url
            if [ -n "$custom_url" ]; then
                install_apk "Custom App" "$custom_url"
            fi
            ;;
        0)
            echo "Tạm biệt!"
            exit 0
            ;;
        *)
            echo "Lựa chọn không hợp lệ."
            ;;
    esac
done

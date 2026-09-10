#!/usr/bin/env python3
"""
ATV ADB Installer - Pure Python (Stdlib only)
Cài đặt trực tiếp ứng dụng từ Điện thoại / Máy tính sang Android TV qua ADB WiFi.
ponytail: chạy CLI thuần stdlib, không phụ thuộc pip. Nâng cấp Rich/Curses nếu cần UI màu mè.
"""

import os
import sys
import json
import urllib.request
import subprocess
import tempfile
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "apps.json")

def load_apps():
    if not os.path.exists(DATA_FILE):
        print(f"[!] Không tìm thấy {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def run_adb(args):
    try:
        res = subprocess.run(["adb"] + args, capture_output=True, text=True, check=False)
        return res.returncode == 0, res.stdout.strip()
    except FileNotFoundError:
        print("[ERROR] Không tìm thấy lệnh 'adb'. Cài đặt: pkg install android-tools (Termux) hoặc tải Android Platform Tools.")
        sys.exit(1)

def connect_tv(ip):
    print(f"[*] Đang kết nối tới {ip}:5555 ...")
    run_adb(["disconnect"])
    ok, out = run_adb(["connect", f"{ip}:5555"])
    print(out)
    print("[*] Kiểm tra TV và chọn 'Always allow from this computer' nếu có pop-up.")
    _, devs = run_adb(["devices"])
    print(f"[*] Thiết bị đã kết nối:\n{devs}")

def download_and_install(ip, app_name, url):
    if not url:
        print(f"[!] {app_name} không có link tải trực tiếp.")
        return False
    
    print(f"\n[*] Đang tải {app_name}...")
    temp_dir = tempfile.mkdtemp()
    apk_path = os.path.join(temp_dir, "temp.apk")
    
    try:
        def reporthook(blocknum, blocksize, totalsize):
            if totalsize > 0:
                percent = min(100, int(blocknum * blocksize * 100 / totalsize))
                sys.stdout.write(f"\r    Tiến trình: {percent}%")
                sys.stdout.flush()

        urllib.request.urlretrieve(url, apk_path, reporthook)
        print("\n[*] Đang cài đặt vào Android TV...")
        target = f"{ip}:5555"
        ok, out = run_adb(["-s", target, "install", "-r", "-d", apk_path])
        if not ok:
            # thử không có cờ -s nếu chỉ có 1 device
            ok, out = run_adb(["install", "-r", "-d", apk_path])
        print(f"    Kết quả: {out}")
        return ok
    except Exception as e:
        print(f"[ERROR] Lỗi khi tải/cài {app_name}: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def main():
    apps = load_apps()
    print("=" * 50)
    print("     ATV ADB INSTALLER - TỪ ĐIỆN THOẠI LÊN TIVI")
    print("=" * 50)
    
    tv_ip = input("Nhập địa chỉ IP TV (vd 192.168.1.15): ").strip()
    if not tv_ip:
        print("IP không được để trống.")
        return
    
    connect_tv(tv_ip)

    while True:
        print("\n" + "=" * 20 + " MENU " + "=" * 20)
        print("1. Tìm kiếm ứng dụng theo tên")
        print("2. Xem theo danh mục")
        print("3. Cài gói combo phổ biến (YouTube chặn QC, Phim 4K, TiviMate)")
        print("4. Cài bằng URL APK trực tiếp")
        print("0. Thoát")
        choice = input("Lựa chọn [0-4]: ").strip()

        if choice == "0":
            print("Tạm biệt!")
            break
        elif choice == "1":
            kw = input("Nhập tên ứng dụng cần tìm: ").strip().lower()
            results = [a for a in apps if kw in a["name"].lower() or kw in a["category"].lower()]
            if not results:
                print("[!] Không tìm thấy ứng dụng nào.")
                continue
            for i, a in enumerate(results, 1):
                print(f"{i:2d}. [{a['category']}] {a['name']} - Code: {a.get('code','')} - {a.get('meta','')}")
            sel = input("\nChọn số thứ tự để cài (Enter để quay lại): ").strip()
            if sel.isdigit() and 1 <= int(sel) <= len(results):
                app = results[int(sel)-1]
                download_and_install(tv_ip, app["name"], app["direct_url"])
        elif choice == "2":
            cats = sorted(list(set(a["category"] for a in apps)))
            for i, c in enumerate(cats, 1):
                count = sum(1 for a in apps if a["category"] == c)
                print(f"{i:2d}. {c} ({count} apps)")
            c_sel = input(f"Chọn danh mục [1-{len(cats)}]: ").strip()
            if c_sel.isdigit() and 1 <= int(c_sel) <= len(cats):
                cat_name = cats[int(c_sel)-1]
                cat_apps = [a for a in apps if a["category"] == cat_name]
                for j, a in enumerate(cat_apps, 1):
                    print(f"  {j:2d}. {a['name']} ({a.get('meta','')})")
                a_sel = input("Chọn số app (hoặc 'all' để cài tất cả): ").strip().lower()
                if a_sel == "all":
                    for a in cat_apps:
                        download_and_install(tv_ip, a["name"], a["direct_url"])
                elif a_sel.isdigit() and 1 <= int(a_sel) <= len(cat_apps):
                    app = cat_apps[int(a_sel)-1]
                    download_and_install(tv_ip, app["name"], app["direct_url"])
        elif choice == "3":
            quick_targets = ["smart tube", "phim4k tv", "tivimate_v5.1.6", "downloader_aftv_v1.5.3", "xplorer_file_manager"]
            to_install = [a for a in apps if any(t in a["name"].lower() for t in quick_targets) and a.get("direct_url")]
            print(f"[*] Sẽ cài đặt {len(to_install)} ứng dụng:")
            for a in to_install:
                print(f" - {a['name']}")
            confirm = input("Tiếp tục? (y/n): ").strip().lower()
            if confirm == "y":
                for a in to_install:
                    download_and_install(tv_ip, a["name"], a["direct_url"])
        elif choice == "4":
            u = input("Nhập trực tiếp URL APK: ").strip()
            if u:
                download_and_install(tv_ip, "Custom App", u)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Android TV ADB Installer - Professional CLI
Tu dong hoa ket noi va cai dat ung dung tu xa len Android TV qua Wireless ADB.
YAGNI: 100% Python Standard Library, khong yeu cau pip packages.
"""

import os
import sys
import json
import urllib.request
import subprocess
import tempfile
import shutil
import re

# Dam bao terminal Windows khong bi loi ma font Unicode (cp1252)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "apps.json")
CONFIG_FILE = os.path.join(BASE_DIR, ".last_tv_ip")

def load_apps():
    if not os.path.exists(DATA_FILE):
        print(f"[ERROR] Khong tim thay tap tin du lieu: {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def check_or_bootstrap_adb():
    """Kiem tra adb, neu o Windows ma thieu thi tu dong tai Google Platform Tools."""
    if shutil.which("adb"):
        return True
    
    local_adb = os.path.join(BASE_DIR, "adb.exe" if sys.platform == "win32" else "adb")
    if os.path.exists(local_adb):
        os.environ["PATH"] = BASE_DIR + os.pathsep + os.environ.get("PATH", "")
        return True

    if sys.platform == "win32":
        print("\n[INFO] He thong Windows chua co cong cu 'adb'.")
        print("[*] Dang tu dong tai bo Google Platform Tools chinh chu...")
        try:
            import zipfile
            zip_url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
            zip_path = os.path.join(BASE_DIR, "pt.zip")
            urllib.request.urlretrieve(zip_url, zip_path)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                for member in zip_ref.namelist():
                    if member.startswith("platform-tools/"):
                        filename = os.path.basename(member)
                        if filename:
                            source = zip_ref.open(member)
                            target = open(os.path.join(BASE_DIR, filename), "wb")
                            with source, target:
                                shutil.copyfileobj(source, target)
            if os.path.exists(zip_path):
                os.remove(zip_path)
            os.environ["PATH"] = BASE_DIR + os.pathsep + os.environ.get("PATH", "")
            print("[OK] Da tai va thiet lap Google Platform Tools thanh cong.\n")
            return True
        except Exception as e:
            print(f"[WARN] Khong the tu dong tai: {e}")
            return False
    return False

def run_adb(args):
    """Thuc thi lenh adb an toan qua subprocess."""
    if not shutil.which("adb"):
        check_or_bootstrap_adb()
    try:
        res = subprocess.run(["adb"] + args, capture_output=True, text=True, check=False)
        return res.returncode == 0, res.stdout.strip(), res.stderr.strip()
    except FileNotFoundError:
        print("\n[ERROR] Khong tim thay cong cu 'adb'.")
        print("  - Android (Termux): pkg install android-tools")
        print("  - Windows: Chay install_windows.bat de tu dong tai")
        print("  - macOS: brew install android-platform-tools")
        print("  - Linux: sudo apt install adb")
        sys.exit(1)

def get_connected_devices():
    """Lay danh sach cac thiet bi ADB dang ket noi."""
    ok, out, _ = run_adb(["devices"])
    if not ok:
        return []
    devices = []
    lines = out.splitlines()[1:]
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2 and parts[1] == "device":
            devices.append(parts[0])
    return devices

def save_last_ip(ip):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write(ip.strip())
    except Exception:
        pass

def get_last_ip():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return ""
    return ""

def connect_device():
    """Tu dong nhan dien thiet bi da ket noi hoac hoi dia chi IP."""
    active_devices = get_connected_devices()
    if len(active_devices) == 1:
        dev = active_devices[0]
        print(f"[INFO] Phat hien thiet bi da ket noi: {dev}")
        confirm = input(f"Su dung thiet bi nay? [Y/n]: ").strip().lower()
        if confirm in ["", "y", "yes"]:
            return dev

    last_ip = get_last_ip()
    prompt = f"Nhap dia chi IP cua TV"
    if last_ip:
        prompt += f" [Nhan Enter de dung {last_ip}]: "
    else:
        prompt += f" (vi du 192.168.1.15): "

    while True:
        user_input = input(prompt).strip()
        if not user_input and last_ip:
            target_ip = last_ip
        else:
            target_ip = user_input

        if not target_ip:
            print("[WARN] Dia chi IP khong duoc de trong.")
            continue

        if ":" not in target_ip:
            target_device = f"{target_ip}:5555"
        else:
            target_device = target_ip

        print(f"[*] Dang ket noi toi {target_device}...")
        run_adb(["disconnect", target_device])
        ok, out, err = run_adb(["connect", target_device])
        print(out or err)

        print("[*] Kiem tra man hinh TV: Tich 'Luon cho phep' neu co hop thoai uy quyen.")
        devices = get_connected_devices()
        if target_device in devices or any(target_ip in d for d in devices):
            print(f"[OK] Ket noi thanh cong toi {target_device}")
            save_last_ip(target_ip.split(":")[0])
            return target_device
        else:
            print(f"[WARN] Chua the ket noi toi {target_device}. Vui long kiem tra lai IP hoac xac nhan tren TV.")
            retry = input("Thu lai? [Y/n]: ").strip().lower()
            if retry not in ["", "y", "yes"]:
                return target_device

def download_and_install(device, app_name, url):
    """Tai APK voi thanh tien trinh truc quan va cai dat qua ADB."""
    if not url:
        print(f"[WARN] {app_name}: Khong co duong dan tai truc tiep.")
        return False

    print(f"\n[*] Dang xu ly: {app_name}")
    temp_dir = tempfile.mkdtemp()
    apk_path = os.path.join(temp_dir, "app.apk")

    try:
        def progress(count, block_size, total_size):
            if total_size > 0:
                percent = min(100, int(count * block_size * 100 / total_size))
                downloaded_mb = (count * block_size) / (1024 * 1024)
                total_mb = total_size / (1024 * 1024)
                bar_len = 30
                filled = int(bar_len * percent / 100)
                bar = "=" * filled + ">" + " " * (bar_len - filled - 1) if filled < bar_len else "=" * bar_len
                sys.stdout.write(f"\r    [{bar}] {percent}% ({downloaded_mb:.1f}/{total_mb:.1f} MB)")
                sys.stdout.flush()

        urllib.request.urlretrieve(url, apk_path, progress)
        print("\n    [INFO] Dang cai dat vao Android TV...")
        
        ok, out, err = run_adb(["-s", device, "install", "-r", "-d", apk_path])
        if ok or "Success" in out:
            print(f"    [OK] Cai dat hoan tat: {app_name}")
            return True
        else:
            # Thu cai khong co co -s phong truong hop chi co 1 thiet bi
            ok2, out2, err2 = run_adb(["install", "-r", "-d", apk_path])
            if ok2 or "Success" in out2:
                print(f"    [OK] Cai dat hoan tat: {app_name}")
                return True
            print(f"    [ERROR] Cai dat that bai: {out or err or out2 or err2}")
            return False
    except Exception as e:
        print(f"\n    [ERROR] Loi tai tap tin: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def parse_selections(user_input, max_count):
    """
    Phan tich cu phap chon da ung dung:
    Ho tro: '1', '1,3,5', '2-6', 'all'
    """
    inp = user_input.strip().lower()
    if inp == "all":
        return list(range(1, max_count + 1))
    
    selected_indices = set()
    parts = [p.strip() for p in inp.split(",") if p.strip()]
    for p in parts:
        if "-" in p:
            sub = p.split("-")
            if len(sub) == 2 and sub[0].isdigit() and sub[1].isdigit():
                start, end = int(sub[0]), int(sub[1])
                for idx in range(start, end + 1):
                    if 1 <= idx <= max_count:
                        selected_indices.add(idx)
        elif p.isdigit():
            idx = int(p)
            if 1 <= idx <= max_count:
                selected_indices.add(idx)
    return sorted(list(selected_indices))

def batch_install(device, app_list):
    total = len(app_list)
    success = 0
    for i, a in enumerate(app_list, 1):
        print(f"\n[{i}/{total}] {a['name']}")
        if download_and_install(device, a["name"], a["direct_url"]):
            success += 1
    print(f"\n==========================================")
    print(f"[KET QUA] Cai dat thanh cong: {success}/{total} ung dung")
    print(f"==========================================")

def main():
    apps = load_apps()
    print("=" * 55)
    print("       ANDROID TV ADB INSTALLER - CONSOLE CLI      ")
    print("=" * 55)

    device = connect_device()

    while True:
        print("\n------------------ MENU CHINH ------------------")
        print(f"Thiet bi hien tai: {device}")
        print("1. Tim kiem ung dung theo ten")
        print("2. Duyet ung dung theo danh muc")
        print("3. Cai goi co ban (YouTube chan QC, Phim 4K, TiviMate)")
        print("4. Cai dat bang duong dan APK truc tiep")
        print("5. Ket noi lai hoac doi dia chi IP TV")
        print("0. Thoat")
        choice = input("Lua chon [0-5]: ").strip()

        if choice == "0":
            print("[INFO] Da dong chuong trinh.")
            break
        elif choice == "1":
            kw = input("\nNhap tu khoa tim kiem (vi du: youtube, phim, tv): ").strip().lower()
            results = [a for a in apps if kw in a["name"].lower() or kw in a["category"].lower()]
            if not results:
                print("[WARN] Khong tim thay ung dung phu hop.")
                continue
            
            print(f"\nKet qua tim kiem ({len(results)} ung dung):")
            for i, a in enumerate(results, 1):
                print(f"  {i:2d}. [{a['category']}] {a['name']}")
            
            sel = input("\nChon so de cai (ho tro '1,3,5' hoac '1-4' hoac 'all', Enter de huy): ")
            indices = parse_selections(sel, len(results))
            if indices:
                chosen = [results[i - 1] for i in indices]
                batch_install(device, chosen)
        elif choice == "2":
            cats = sorted(list(set(a["category"] for a in apps)))
            print("\nDanh sach danh muc:")
            for i, c in enumerate(cats, 1):
                cnt = sum(1 for a in apps if a["category"] == c)
                print(f"  {i:2d}. {c} ({cnt} ung dung)")
            
            c_sel = input(f"\nChon danh muc [1-{len(cats)}]: ").strip()
            if c_sel.isdigit() and 1 <= int(c_sel) <= len(cats):
                selected_cat = cats[int(c_sel) - 1]
                cat_apps = [a for a in apps if a["category"] == selected_cat]
                print(f"\nDanh sach [{selected_cat}]:")
                for j, a in enumerate(cat_apps, 1):
                    print(f"  {j:2d}. {a['name']}")
                
                sel = input("\nChon so de cai (ho tro '1,3,5', '1-4', 'all', Enter de quay lai): ")
                indices = parse_selections(sel, len(cat_apps))
                if indices:
                    chosen = [cat_apps[i - 1] for i in indices]
                    batch_install(device, chosen)
        elif choice == "3":
            targets = ["smart tube", "phim4k tv", "tivimate", "downloader", "xplorer"]
            combo = [a for a in apps if any(t in a["name"].lower() for t in targets) and a.get("direct_url")]
            print(f"\nGoi co ban gom {len(combo)} ung dung:")
            for a in combo:
                print(f"  - {a['name']}")
            confirm = input("Xac nhan cai dat toan bo goi nay? [Y/n]: ").strip().lower()
            if confirm in ["", "y", "yes"]:
                batch_install(device, combo)
        elif choice == "4":
            custom_url = input("\nDan duong dan APK truc tiep: ").strip()
            if custom_url:
                download_and_install(device, "Custom App", custom_url)
        elif choice == "5":
            device = connect_device()

if __name__ == "__main__":
    main()

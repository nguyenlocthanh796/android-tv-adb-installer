#!/usr/bin/env python3
"""
Android TV ADB Installer - Professional 1-Click CLI
Tu dong quet mang LAN tim Android TV, chon so de ket noi va chon so de cai app.
YAGNI: 100% Python Standard Library.
"""

import os
import sys
import json
import socket
import urllib.request
import subprocess
import tempfile
import shutil
from concurrent.futures import ThreadPoolExecutor

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
    """Kiem tra hoac tu dong tai Google Platform Tools tren Windows neu thieu."""
    if shutil.which("adb"):
        return True
    
    local_adb = os.path.join(BASE_DIR, "adb.exe" if sys.platform == "win32" else "adb")
    if os.path.exists(local_adb):
        os.environ["PATH"] = BASE_DIR + os.pathsep + os.environ.get("PATH", "")
        return True

    if sys.platform == "win32":
        print("\n[*] Dang tu dong tai bo Google Platform Tools...")
        try:
            import zipfile
            zip_url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
            zip_path = os.path.join(BASE_DIR, "pt.zip")
            urllib.request.urlretrieve(zip_url, zip_path)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                for member in zip_ref.namelist():
                    if member.startswith("platform-tools/"):
                        fn = os.path.basename(member)
                        if fn:
                            src = zip_ref.open(member)
                            tgt = open(os.path.join(BASE_DIR, fn), "wb")
                            with src, tgt:
                                shutil.copyfileobj(src, tgt)
            if os.path.exists(zip_path):
                os.remove(zip_path)
            os.environ["PATH"] = BASE_DIR + os.pathsep + os.environ.get("PATH", "")
            print("[OK] Thiet lap ADB thanh cong.\n")
            return True
        except Exception as e:
            print(f"[WARN] Khong the tai ADB tu dong: {e}")
            return False
    return False

def run_adb(args):
    """Thuc thi lenh adb."""
    if not shutil.which("adb"):
        check_or_bootstrap_adb()
    try:
        res = subprocess.run(["adb"] + args, capture_output=True, text=True, check=False)
        return res.returncode == 0, res.stdout.strip(), res.stderr.strip()
    except FileNotFoundError:
        print("\n[ERROR] Khong tim thay 'adb'.")
        sys.exit(1)

def get_connected_devices():
    """Lay danh sach cac thiet bi ADB da ket noi san."""
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

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "192.168.1.1"

def scan_lan_for_tvs():
    """Quet nhanh mang LAN port 5555 trong 1-2 giay."""
    local_ip = get_local_ip()
    prefix = ".".join(local_ip.split(".")[:3]) + "."
    found = []

    def check_ip(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        res = sock.connect_ex((ip, 5555))
        sock.close()
        if res == 0:
            return ip
        return None

    ips = [f"{prefix}{i}" for i in range(1, 255)]
    with ThreadPoolExecutor(max_workers=60) as executor:
        for result in executor.map(check_ip, ips):
            if result:
                found.append(result)
    return found

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

def auto_connect_tv():
    """Tu dong do tim thiet bi hoac hien danh sach de chon so."""
    # 1. Kiem tra thiet bi da ket noi san (qua USB hoac WiFi)
    active = get_connected_devices()
    if active:
        print(f"[OK] Phat hien thiet bi ADB dang ket noi:")
        for idx, d in enumerate(active, 1):
            print(f"  [{idx}] {d}")
        if len(active) == 1:
            ans = input(f"Su dung thiet bi nay? [Enter de dong y / nhap 'n' de doi]: ").strip().lower()
            if ans in ["", "y", "yes"]:
                return active[0]

    # 2. Quet nhanh mang LAN tim TV bat port 5555
    print("\n[*] Dang tu dong do tim Android TV trong mang WiFi...")
    discovered = scan_lan_for_tvs()
    last_ip = get_last_ip()

    if last_ip and last_ip not in discovered:
        # Kiem tra nhanh last_ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        if sock.connect_ex((last_ip, 5555)) == 0:
            discovered.insert(0, last_ip)
        sock.close()

    target_ip = ""
    if discovered:
        print(f"[OK] Da tim thay {len(discovered)} thiet bi Android TV:")
        for idx, ip in enumerate(discovered, 1):
            tag = " (Lan truoc)" if ip == last_ip else ""
            print(f"  [{idx}] {ip}{tag}")
        print("  [0] Nhap dia chi IP khac thu cong")
        
        sel = input(f"\nChon so TV muon ket noi [Mac dinh: 1]: ").strip()
        if not sel or sel == "1":
            target_ip = discovered[0]
        elif sel.isdigit() and 1 <= int(sel) <= len(discovered):
            target_ip = discovered[int(sel) - 1]

    # 3. Neu khong do duoc hoac nguoi dung chon nhap thu cong
    if not target_ip:
        prompt = "Nhap dia chi IP cua TV"
        if last_ip:
            prompt += f" [Nhan Enter dung lai {last_ip}]: "
        else:
            prompt += " (vi du 192.168.1.15): "
        inp = input(prompt).strip()
        target_ip = inp if inp else last_ip

    if not target_ip:
        print("[ERROR] Khong co dia chi IP nao duoc chon.")
        sys.exit(1)

    target_device = f"{target_ip}:5555" if ":" not in target_ip else target_ip
    print(f"\n[*] Dang ket noi toi {target_device}...")
    run_adb(["disconnect", target_device])
    ok, out, err = run_adb(["connect", target_device])
    print(out or err)

    print("[*] Vui long nhin man hinh TV va tich 'Luon cho phep' neu co hop thoai uy quyen.")
    save_last_ip(target_ip.split(":")[0])
    return target_device

def download_and_install(device, app_name, url):
    """Tai APK voi thanh tien trinh truc quan va cai vao TV."""
    if not url:
        print(f"[WARN] {app_name}: Khong co link tai.")
        return False

    print(f"\n[*] Dang tai: {app_name}")
    temp_dir = tempfile.mkdtemp()
    apk_path = os.path.join(temp_dir, "app.apk")

    try:
        def progress(count, block_size, total_size):
            if total_size > 0:
                percent = min(100, int(count * block_size * 100 / total_size))
                downloaded_mb = (count * block_size) / (1024 * 1024)
                total_mb = total_size / (1024 * 1024)
                bar_len = 25
                filled = int(bar_len * percent / 100)
                bar = "=" * filled + ">" + " " * (bar_len - filled - 1) if filled < bar_len else "=" * bar_len
                sys.stdout.write(f"\r    [{bar}] {percent}% ({downloaded_mb:.1f}/{total_mb:.1f} MB)")
                sys.stdout.flush()

        urllib.request.urlretrieve(url, apk_path, progress)
        print("\n    [INFO] Dang cai vao Android TV...")
        ok, out, err = run_adb(["-s", device, "install", "-r", "-d", apk_path])
        if ok or "Success" in out:
            print(f"    [OK] Da cai dat thanh cong: {app_name}")
            return True
        else:
            ok2, out2, err2 = run_adb(["install", "-r", "-d", apk_path])
            if ok2 or "Success" in out2:
                print(f"    [OK] Da cai dat thanh cong: {app_name}")
                return True
            print(f"    [ERROR] That bai: {out or err or out2 or err2}")
            return False
    except Exception as e:
        print(f"\n    [ERROR] Loi tai file: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def parse_selections(user_input, max_count):
    inp = user_input.strip().lower()
    if inp == "all":
        return list(range(1, max_count + 1))
    selected = set()
    for p in [x.strip() for x in inp.split(",") if x.strip()]:
        if "-" in p:
            parts = p.split("-")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                for idx in range(int(parts[0]), int(parts[1]) + 1):
                    if 1 <= idx <= max_count:
                        selected.add(idx)
        elif p.isdigit():
            idx = int(p)
            if 1 <= idx <= max_count:
                selected.add(idx)
    return sorted(list(selected))

def batch_install(device, app_list):
    total = len(app_list)
    success = 0
    for i, a in enumerate(app_list, 1):
        print(f"\n[{i}/{total}] {a['name']}")
        if download_and_install(device, a["name"], a["direct_url"]):
            success += 1
    print(f"\n==========================================")
    print(f"[KET QUA] Da cai dat thanh cong: {success}/{total} ung dung")
    print(f"==========================================")

def get_recommended_apps(apps):
    """Loc top 10 app pho bien nhat de hien thi ngay tren man hinh chinh."""
    keys = ["smart tube", "phim4k tv", "tivimate", "sportstv", "get out", "downloader", "xplorer", "totube", "vtvgo", "hop phim"]
    top_apps = []
    seen = set()
    for k in keys:
        for a in apps:
            if k in a["name"].lower() and a["name"] not in seen and a.get("direct_url"):
                top_apps.append(a)
                seen.add(a["name"])
                break
    return top_apps

def main():
    apps = load_apps()
    print("=" * 60)
    print("        ANDROID TV ADB INSTALLER - 1-CLICK TO TV        ")
    print("=" * 60)

    # 1. Tu dong do TV va ket noi
    device = auto_connect_tv()
    top_apps = get_recommended_apps(apps)

    while True:
        print("\n" + "=" * 25 + " DANH SACH APP PHO BIEN " + "=" * 25)
        print(f"Thiet bi TV dang ket noi: {device}")
        for idx, a in enumerate(top_apps, 1):
            print(f"  [{idx:2d}] {a['name']} ({a['category']})")
        print("  -------------------------------------------------------------")
        print("  [C]  Cai toan bo goi pho bien tren (1 click)")
        print("  [T]  Tim kiem ung dung theo ten")
        print("  [M]  Duyet tat ca theo 9 danh muc (110+ app)")
        print("  [R]  Doi dia chi IP / Ket noi TV khac")
        print("  [0]  Thoat")
        print("  -------------------------------------------------------------")

        choice = input("Chon so app muon cai (vi du '1' hoac '1,3,5', '1-4', 'C'): ").strip()

        if choice == "0":
            print("[INFO] Da thoat chuong trinh.")
            break
        elif choice.upper() == "C":
            batch_install(device, top_apps)
        elif choice.upper() == "T":
            kw = input("\nNhap tu khoa tim kiem (vi du: bóng đá, youtube, phim): ").strip().lower()
            results = [a for a in apps if kw in a["name"].lower() or kw in a["category"].lower()]
            if not results:
                print("[WARN] Khong tim thay ung dung.")
                continue
            print(f"\nKet qua tim kiem ({len(results)} ung dung):")
            for i, a in enumerate(results, 1):
                print(f"  [{i:2d}] {a['name']} ({a['category']})")
            sel = input("\nChon so app de cai (vi du '1' hoac '1,3' hoac 'all', Enter de huy): ")
            idx_list = parse_selections(sel, len(results))
            if idx_list:
                batch_install(device, [results[i - 1] for i in idx_list])
        elif choice.upper() == "M":
            cats = sorted(list(set(a["category"] for a in apps)))
            print("\nDanh sach 9 danh muc:")
            for i, c in enumerate(cats, 1):
                cnt = sum(1 for a in apps if a["category"] == c)
                print(f"  [{i}] {c} ({cnt} ung dung)")
            c_sel = input(f"\nChon danh muc [1-{len(cats)}]: ").strip()
            if c_sel.isdigit() and 1 <= int(c_sel) <= len(cats):
                selected_cat = cats[int(c_sel) - 1]
                cat_apps = [a for a in apps if a["category"] == selected_cat]
                print(f"\nDanh sach [{selected_cat}]:")
                for j, a in enumerate(cat_apps, 1):
                    print(f"  [{j:2d}] {a['name']}")
                sel = input("\nChon so de cai (vi du '1', '1,3', 'all', Enter de huy): ")
                idx_list = parse_selections(sel, len(cat_apps))
                if idx_list:
                    batch_install(device, [cat_apps[i - 1] for i in idx_list])
        elif choice.upper() == "R":
            device = auto_connect_tv()
        else:
            # Chon truc tiep theo so tren danh sach top_apps
            indices = parse_selections(choice, len(top_apps))
            if indices:
                selected_apps = [top_apps[i - 1] for i in indices]
                batch_install(device, selected_apps)
            else:
                print("[WARN] Lua chon khong hop le.")

if __name__ == "__main__":
    main()

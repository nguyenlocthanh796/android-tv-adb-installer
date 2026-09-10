# Android TV ADB Installer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20iOS%20%7C%20Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Apps](https://img.shields.io/badge/Apps-110%2B%20ATV%20Applications-blue.svg)](#danh-sach-ung-dung)

Bo cong cu quan tri va cai dat tu dong ung dung cho Android TV / Google TV / TV Box qua ket noi ADB khong day (Wireless ADB). Ho tro cai dat tu dien thoai Android, iPhone, iPad va may tinh (Windows, macOS, Linux).

---

## Muc luc
1. [Yeu cau va chuan bi tren Android TV](#chuan-bi-tren-android-tv)
2. [Huong dan cai dat theo he dieu hanh](#huong-dan-cai-dat)
   - [Android (Termux / Bugjaeger)](#1-android)
   - [iOS (iPhone / iPad)](#2-ios-iphone--ipad)
   - [Windows](#3-windows)
   - [macOS](#4-macos)
   - [Linux](#5-linux)
3. [Danh sach ung dung & Ma Downloader](#danh-sach-ung-dung)
4. [Xu ly loi thuong gap](#xu-ly-loi-thuong-gap)
5. [Tuyen bo phap ly & Ban quyen (Disclaimer & DMCA)](#tuyen-bo-phap-ly--ban-quyen-disclaimer--dmca)
6. [Giay phep](#giay-phep)

---

## Chuan bi tren Android TV

Ap dung cho tat ca thiet bi chay Android TV / Google TV (Sony, TCL, Xiaomi, Casper, Sharp, Chromecast with Google TV, Onn Box, Mi Box):

1. Truy cap **Settings (Cai dat)** -> **Device Preferences (Tuy chon thiet bi)** hoac **System (He thong)** -> **About (Gioi thieu)**.
2. Tim muc **Android TV OS Build (Ban dung he dieu hanh Android)**.
3. Nhan phim **OK / Select** tren remote **7 lan lien tiep** den khi he thong thong bao da kich hoat che do nha phat trien.
4. Quay lai menu truoc do -> vao muc **Developer Options (Tuy chon cho nha phat trien)**.
5. Kich hoat cac muc sau:
   - **USB Debugging (Go loi USB)**.
   - **Wireless / Network Debugging (Go loi qua mang)** (neu thiet bi ho tro).
6. Vao muc **Network & Internet (Mang & Internet)** de xac dinh **dia chi IP cua TV** (vi du: `192.168.1.15`).

> [!NOTE]
> Thiet bi dieu khien va Android TV phai ket noi vao cung mot mang Wi-Fi / LAN.

---

## Huong dan cai dat

### 1. Android

#### Phuong phap 1: Su dung Termux (Dong lenh tu dong)
1. Cai dat ung dung Termux tu F-Droid hoac GitHub Releases.
2. Mo Termux va thuc thi lenh:
```bash
pkg update && pkg install git python android-tools -y && git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git && cd android-tv-adb-installer && python installer.py
```
3. Nhap dia chi IP cua TV.
4. Tren man hinh TV, xac nhan hop thoai yeu cau quyen: chon **Always allow from this computer**.
5. Chon ung dung can cai dat tu danh muc hien thi tren man hinh.

#### Phuong phap 2: Su dung giao dien Bugjaeger
1. Cai dat **Bugjaeger Mobile ADB** tu Google Play Store.
2. Ket noi toi IP cua TV qua cong `5555`.
3. Xac nhan uy quyen ADB tren TV.
4. Chuyen qua tab **Packages**, chon **Install APK** va su dung link truc tiep tu danh sach ben duoi.

---

### 2. iOS (iPhone / iPad)

He dieu hanh iOS gioi han thuc thi ADB binary truc tiep. Chon mot trong hai giai phap sau:

#### Phuong phap 1: Nhap ma tren app Downloader cua TV (Khuyen nghi)
1. Cai dat ung dung **Downloader by AFTVnews** tren Android TV.
2. Tren iPhone, tra cuu ma tai tai [Danh sach ung dung](#danh-sach-ung-dung) ben duoi (vi du: `4411335` cho Phim4K TV).
3. Nhap ma vao o URL tren TV de cai dat truc tiep.

#### Phuong phap 2: Su dung Web ADB qua trinh duyet
1. Mo Safari tren iPhone / iPad, truy cap [webadb.com](https://app.webadb.com/).
2. Ket noi toi dia chi IP TV qua cong `5555`.
3. Tai file APK tu danh sach va nap vao TV.

---

### 3. Windows

#### Phuong phap 1: Thuc thi script tu dong
1. Tai ma nguon tu nut **Code** -> **Download ZIP** tren GitHub, giai nen.
2. Nhap dup file `install_windows.bat` (cong cu se tu dong tai Google Platform Tools neu he thong chua co ADB).
3. Nhap IP cua TV va thao tac theo huong dan tren man hinh Console.

#### Phuong phap 2: Chay qua PowerShell / Command Prompt
```powershell
winget install Google.PlatformTools
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python installer.py
```

---

### 4. macOS

1. Mo Terminal va cai dat cong cu thong qua Homebrew:
```bash
brew install android-platform-tools python
```
2. Thuc thi bo cai dat:
```bash
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python3 installer.py
```

---

### 5. Linux (Ubuntu / Debian / Fedora / Arch)

1. Cai dat ADB:
   - Ubuntu / Debian: `sudo apt update && sudo apt install -y adb python3 git`
   - Fedora: `sudo dnf install -y android-tools python3 git`
   - Arch Linux: `sudo pacman -S android-tools python git`
2. Thuc thi chuong trinh:
```bash
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python3 installer.py
```

---

## Danh sach ung dung


### TRUYỀN HÌNH -  ĐÁ BANH

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **Get Out 2 end** | `393939` | mới nhất • 158 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.end.apk) |
| **Get Out 2.0** | `3074016` | v2.0 • 31 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.0.apk) |
| **SportsTV v5.2.3** | `8705526` | v5.2.3 • 123 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV_5.2.3.apk) |
| **SportsTV v4.5** | `393939` | v4.5 • 24 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV-v4.5-Android5.apk) |
| **SportzX v3.2** | `393939` | v3.2 • 48 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_3.2v.apk) |
| **SportzX v2.6** | `393939` | v2.6 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_2.6v.apk) |
| **Hóng TV** | `7027363` | v1.1.8 • 81 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hongtv.apk) |
| **Xem TV 5.8.8** | `393939` | 5.8.8 • 59 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/XemTV_v5.8.8.apk) |
| **CricHDaiTV_v5.12** | `393939` | v5.12 • 23 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CricHDaiTV-v5.12.apk) |
| **TV365_v7** | `393939` | v7.0 • 43 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TV365_v7.apk) |
| **vAppTV** | `9788306` | v1.0.0 • 33 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vAppTV.apk) |
| **VTVgoTV_v11.12.30** | `393939` | v11.12.30 • 19 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVgoTV_v11.12.30.apk) |
| **VTVprime_v1.7.0** | `393939` | v1.7.0 • 21 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVprime_v1.7.0.apk) |
| **Cricfy_V6.6** | `1213128` | v6.6 • 13 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Cricfy_V6.6.apk) |
| **GeeSports_V3.6** | `7266756` | v3.6 • 29 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/GeeSports_%28V3.6%29.apk) |

### PHIM 4K

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **Phim4K TV 2.6.8** | `4411335` | v2.6.8 • 119 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/phim4k_TV_2.6.8.apk) |
| **Phim4K Mobile** | `4833418` | v2.6.1 • 31 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android%20Full.apk) |
| **Phim4K Android** | `393939` | v2.6.1 • 26 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android.apk) |
| **Film4k.net ATV** | `393939` | v1.0.0 • 29 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-arm64-v8a-debug8.apk) |
| **Film4k.net ATV v7a** | `393939` | v1.0.0 • 20 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-armeabi-v7a-debug8.apk) |
| **Film4k ATV x86_64-debug8** | `393939` | v1.0.0 • 14 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-x86_64-debug8.apk) |

### XEM PHIM

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **Gu-Phim_v1.0_Windows** | `393939` | v1.0 • 27 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Windows.zip) |
| **Gu-Phim_v1.0_Mobile_Tablet_TV** | `393939` | v1.0 • 20 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Mobile-Tablet-TV.apk) |
| **Hiphim mobile** | `393939` | v1.0.0 • 8 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphim150android.apk) |
| **Hiphim Tivi** | `393939` | v1.0.0 • 22 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphimtv.apk) |
| **NVCPhim_v2.2.8** | `2653652` | v2.2.8 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) |
| **NVC_Movie** | `393939` | v1.0.0 • 2 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVC_Movie.apk) |
| **hieuga** | `1059695` | v1.0.0 • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hieuga.apk) |
| **vuagiaitri** | `7716517` | v1.0.0 • 5 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vuagiaitri.apk) |
| **cobephim-tv** | `6207062` | v1.0.0 • 31 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtv.apk) |
| **cobephim mobile** | `6207062` | v1.0.0 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtvphone_v1.5.apk) |
| **rapphim-0.2.1-mobile** | `393939` | v0.2.1 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-0-2-1-mobile.apk) |
| **rapphim-1.0.1-tv** | `6766306` | v1.0.1 • 9 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-1-0-1-tv.apk) |
| **saigonphim-tv** | `7048453` | v1.0.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/saigonphim.apk) |
| **Chợ_Phim** | `5774068` | v1.0.0 • 24 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/chophim.apk) |
| **CloudStream_4.7.0** | `393939` | v4.7.0 • 15 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CloudStream_%5B4.7.0%5D.apk) |
| **NETFLY_v3** | `2844821` | v3.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NETFLY_v3.apk) |
| **NVC_Movie_TV_v2.6.10** | `1659529` | v2.6.10 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) |
| **TiemGiaiTri_v1.0** | `393939` | v1.0.0 • 11 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiemGiaiTri.apk) |
| **VAX_Player_1.6.5** | `1387135` | v1.6.5 • 5 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VAX_Player_1.6.5_%286666%29.apk) |
| **VaxPlayer_1.7.6** | `393939` | v1.7.6 • 11 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.apk) |
| **VaxPlayer_1.7.6_iOS** | `393939` | v1.7.6 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.ipa) |
| **DaoPhim_TV_1.0.3** | `393939` | v1.0.3 • 31 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-1.0.3-tv.apk) |
| **DaoPhim_Mobile** | `393939` | v1.0.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-mobile.apk) |

### PHẦN MỀM IPTV

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **HSTIVI_2.6** | `393939` | v1.0.0 • 33 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HSTIVI_2.6.apk) |
| **IPTV_PRO** | `393939` | v1.0.0 • 46 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/IPTV_PRO.apk) |
| **M3u-IPTV-v3.0.11-Mod** | `393939` | v3.0.11 • 14 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/m3u-iptv-3.0.19.apk) |
| **OTT_Navigator_v1.7.4.1_Mod** | `1995826` | v1.7.4.1 • 15 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/OTT.apk) |
| **SparkleTV** | `8439261` | v1.0.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SparkleTV.apk) |
| **TiviMate_v5.1.6_MOD** | `393939` | v5.1.6 • 27 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_v5.1.6_MOD.apk) |
| **quantv** | `393939` | v1.0.0 • 17 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/quantv.apk) |
| **televizo_v1.9.6.50_premium** | `6508980` | v1.9.6.50 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/televizo_v1.9.6.50_premium.apk) |
| **tivimate_2.1.5_premium** | `393939` | v2.1.5 • 14 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tivimate_2.1.5_premium.apk) |
| **Backup_Host_5.1.6** | `4739677` | v5.1.6 • 7 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Backup_Host_5.1.6.tmb) |
| **TiviMate_5.3.0** | `393939` | v5.3.0 • 11 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate-5.3.0.apk) |
| **Televizo_byphaptx52022** | `393939` | v5.2022 • 8 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) |
| **Hbo Max** | `2426878` | v1.0.0 • 12 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hbomax.apk) |
| **Smart tube** | `393939` | v1.0.0 • 17 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/smarttube.apk) |
| **PCRTV_4.1.0** | `4579948` | v4.1.0 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/PCRTV_%5B4.1.0%5D.apk.zip) |
| **QTV3.9_Vip** | `5508842` | v3.9 • 19 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/QTV3.9_Vip_pass123%40123.apk) |
| **Televizo_v1.9.6.50_Premium** | `393939` | v1.9.6.50 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_v1.9.6.50_Premium.apk) |
| **Televizo_byphaptx52022_zip** | `393939` | v5.2022 • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) |
| **TiviMate_5.1.6_BannerMod_Spydog** | `393939` | v5.1.6 • 12 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6___BannerM0d_Spydog.apk.zip) |
| **TiviMate_5.1.6_v2** | `393939` | v5.1.6 • 12 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6_%28v2%29.apk.zip) |

### YOUTUBE TV

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **ToTube** | `393939` | v1.0.0 • 15 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ToTube.apk) |
| **Youtube_1.0.8** | `8788599` | v1.0.8 • 31 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ytb2.apk) |
| **vanced_youtube_v20** | `393939` | v20 • 23 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced_youtube_v20.apk) |
| **vanced_youtube_music** | `393939` | v8.40.54 • 5 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced.to_vanced_youtube_music.apk) |
| **microg_v0.3.13** | `393939` | v0.3.13 • 11 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/microg_v0.3.13.apk) |
| **mapvoice** | `7701927` | v1.0.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mapvoice.apk) |
| **supervoice-mod-ATV14** | `393939` | v14.0 • 6 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice-mod-ATV14.apk) |
| **supervoice_ATV9+** | `393939` | v9.0+ • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice_ATV9%2B.apk) |
| **supperVoice-2.2** | `393939` | v2.2 • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supperVoice-2.2.apk) |

### TOOL (CÔNG CỤ)

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **UFO VPN v2.2.3** | `393939` | v1.0.0 • 1.638 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/UFOVPNv2.2.3.apk) |
| **Kiwi VPN v56.20.12** | `393939` | v1.0.0 • 1.637 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/KiwiVPNv56.20.12.apk) |
| **Coc_Coc_Lite_1.6** | `393939` | v1.6 • 7 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Coc_Coc_Lite_1.6.apk) |
| **Autostart+v4.1.1_Modded_** | `393939` | v4.1.1 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Autostart%2Bv4.1.1_Modded_.apk) |
| **_ATV_app__TV_AppsDrawer** | `393939` | v1.0.0 • 228 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/_ATV_app__TV_AppsDrawer.apk) |
| **atvTools_v1.3.0_42-mod** | `393939` | v1.3.0 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/atvTools_v1.3.0_42-mod.apk) |
| **tvQuickActions_Pro_v3.6.0__Patched** | `393939` | v3.6.0 • 2 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.6.0__Patched_.apk) |
| **TvQuickAction_3.0.8** | `393939` | v3.0.8 • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TvQuickAction_3.0.8.apk) |
| **TvQuickActions_Pro_v3.7.0** | `393939` | v3.7.0 (405) • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.7.0_%28405%29.apk) |
| **Remote_for_Android_TV_v6.0.3** | `393939` | v6.0.3 • 2 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Remote_for_Android_TV_v6.0.3_%28no_ads%29.apk) |
| **Developer_Tools_2.1.1** | `393939` | v2.1.1 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Developer_Tools_2.1.1.apk.jar) |
| **Buttons_remapper_v1.2** | `393939` | v1.2 • 2 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Buttons_remapper_v1.2.apk) |
| **Button_Mapper_v3.2** | `393939` | v3.2 • 1 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Button_Mapper_v3.2.apk.zip) |
| **Add_Tivi_Remote** | `393939` | v1.0.0 • 2 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Add_Tivi_Remote.apk) |

### GIAO DIỆN TIVI

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **ATV Launcher** | `393939` | v0136 • 20 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ATV-Launcher-v0136.apk) |
| **Pro_Launcher_(PhapViet)** | `8513629` | v1.0.0 • 15 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Pro_Launcher_%28PhapViet%29.apk) |
| **Project_Launcher** | `393939` | v1.0.0 • 9 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Project_Launcher.apk) |
| **ProTVLauncher_V5** | `6410730` | v5.0 • 8 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ProTVLauncher_V5.apk) |
| **Launcher-Manager_1.0.4** | `393939` | v1.0.4 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Launcher-Manager-1.0.4.apk) |
| **HomeTV_Launcher_6.3.1** | `393939` | v6.3.1 • 9 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HomeTV_Launcher_6.3.1.apk) |
| **Google_TV_Home_1.0.4** | `393939` | v1.0.4 • 12 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Google_TV_Home_1.0.4.apk) |

### STORE (CỬA HÀNG TẢI APP)

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **Aptoide_TV_5.1.2** | `393939` | v5.1.2 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Aptoide_TV_5.1.2.apk) |
| **DLStore_v16.0.4** | `5103033` | v16.0.4 • 46 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/DLStore_v16.0.4.apk) |
| **HDPlay_Store** | `393939` | v3.1.9 • 19 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HDPlay_Store_%5B3.1.9%5D.apk) |
| **Movie Legend Store** | `4369204` | v3.1.5 • 8 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Movie%20Legend%20Store.apk) |
| **TTV_Store_3.0** | `393939` | v3.0 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TTV_Store_3.0.apk) |
| **beecubestore2** | `393939` | v2.0 • 14 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/beecubestore2.apk) |
| **Kho_Ung_Dung_MCU** | `5212814` | v1.0 • 35 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/box_store_mcu_v1.apk) |
| **EMOTN_Store** | `393939` | v1.0.0 • 3 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/emotnstore.apk) |
| **FERRARI_DOWNLOADER** | `5356270` | v1.0.0 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) |
| **MStore_v2.0** | `393939` | v2.0 • 11 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mstore.apk) |
| **ĐôngAnhStore_25.3.2** | `393939` | v25.3.2 • 44 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Dong_Anh_TV_3.6.apk) |
| **BoxStoreMCU_v2.0** | `393939` | v2.0 • 24 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/BoxStoreMCU_v2.0.apk) |

### APP NHẬP CODE &amp; QUẢN LÝ TẬP TIN

| Ten Ung Dung | Ma Downloader | Phien Ban | Link Tai Truc Tiep (APK) |
|:---|:---:|:---|:---|
| **Downloader_AFTV_v1.4.5** | `393939` | v1.4.5 • 28 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.4.5.apk) |
| **Downloader_AFTV_v1.5.3** | `393939` | v1.5.3 • 15 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.5.3.apk) |
| **File_Manager_3.8.2** | `393939` | v3.8.2 • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/File_Manager_3.8.2.apk) |
| **Xplorer_File_Manager_Premium** | `393939` | Premium • 10 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Xplorer_File_Manager_Premium.apk) |
| **FERRARI_DOWNLOADER_zip** | `393939` | v1.0.0 • 4 lượt tải | [Tai APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) |

---

## Xu ly loi thuong gap

* **failed to connect to <IP>:5555: Connection refused**
  - Kiem tra ket noi mang giua hai thiet bi (phai cung mang LAN / Wi-Fi).
  - Khoi dong lai tinh nang USB Debugging hoac khoi dong lai Android TV.
* **device unauthorized**
  - Man hinh TV chua xac thuc khoa bao mat. Xac nhan tren TV va danh dau chon **Always allow from this computer**.
* **INSTALL_FAILED_UPDATE_INCOMPATIBLE**
  - Ung dung tren TV bi xung dot chu ky (signature) voi ban moi. Go cai dat ban cu tren TV truoc khi cai dat lai.

---

## Tuyen bo phap ly & Ban quyen (Disclaimer & DMCA)

1. **Muc dich phi thuong mai**: Du an duoc thuc hien cho muc dich nghien cuu hoc thuat, phan tich ky thuat ket noi giao thuc ADB va ho tro nguoi dung quan tri thiet bi ca nhan. Tac gia khong kinh doanh, khong thu phi va khong quang cao duoi bat ky hinh thuc nao.
2. **Khong luu tru du lieu (Zero Hosting)**: Tac gia va repository nay hoan toan khong luu tru, khong sua doi va khong truc tiep phan phoi bat ky tep tin nhi phan (APK/IPA) nao tren may chu. Toan bo duong dan duoc tong hop tu nguon cong khai tren Internet (nguon: tinhlagi).
3. **Trach nhiem nguoi dung**: Nguoi dung tu chiu trach nhiem phap ly ve viec tai ve, cai dat va su dung cac ung dung tren thiet bi cua minh phu hop voi luat phap so tai va thoa thuan nguoi dung cua tung ung dung.
4. **Chinh sach DMCA & Go bo noi dung (Notice and Takedown)**: Chu so huu ban quyen hoac nha phat trien co quyen yeu cau go bo bat ky duong dan trich dan nao lien quan den san pham cua minh. Vui long mo GitHub Issue hoac gui email ve: `nguyenlocthanh796@users.noreply.github.com`. Duong dan trich dan se duoc go bo khoi danh sach trong vong 24-48 gio sau khi xac thuc thong tin.

---

## Giay phep

Du an duoc phat hanh theo giay phep MIT License. Xem chi tiet tai tap tin `LICENSE`.

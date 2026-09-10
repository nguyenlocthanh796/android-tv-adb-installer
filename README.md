# Android TV ADB Installer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20iOS%20%7C%20Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Total Apps](https://img.shields.io/badge/Apps-110%2B%20ATV%20Applications-blue.svg)](#danh-sach-ung-dung)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

Bộ công cụ dòng lệnh mã nguồn mở hỗ trợ quản trị và cài đặt ứng dụng từ xa lên Android TV, Google TV và TV Box qua kết nối ADB không dây (Wireless ADB). Tự động quét mạng Wi-Fi tìm thiết bị TV, hỗ trợ chọn số cài đặt tức thì trên điện thoại và máy tính.

---

## Mục lục

1. [Bước chuẩn bị trên Android TV](#1-buoc-chuan-bi-tren-android-tv)
2. [Hướng dẫn chi tiết cho Điện thoại Android](#2-huong-dan-chi-tiet-cho-dien-thoai-android)
3. [Hướng dẫn cho iPhone và iPad (iOS)](#3-huong-dan-cho-iphone-va-ipad-ios)
4. [Hướng dẫn cho Máy tính (Windows, macOS, Linux)](#4-huong-dan-cho-may-tinh)
5. [Danh sách toàn bộ 110+ ứng dụng](#danh-sach-ung-dung)
6. [Xử lý lỗi thường gặp](#xu-ly-loi-thuong-gap)
7. [Tuyên bố pháp lý và Bản quyền](#tuyen-bo-phap-ly-va-ban-quyen)
8. [Giấy phép](#giay-phep)

---

## 1. Bước chuẩn bị trên Android TV

Thao tác kích hoạt một lần duy nhất, áp dụng chung cho mọi dòng TV và Box (Sony, TCL, Xiaomi, Casper, Sharp, Coocaa, Chromecast with Google TV, Onn Box, Mi Box):

1. **Kết nối mạng**: Đảm bảo **Điện thoại** và **Android TV** đang bắt chung một mạng Wi-Fi (cùng một dải modem/router).
2. **Bật chế độ Nhà phát triển**:
   - Mở **Cài đặt (Settings)** trên TV > **Tùy chọn thiết bị (Device Preferences)** hoặc **Hệ thống (System)** > **Giới thiệu (About)**.
   - Tìm dòng **Bản dựng hệ điều hành Android (Android TV OS Build)**.
   - Nhấn phím **OK** trên điều khiển **7 lần liên tiếp** cho đến khi xuất hiện thông báo: *"Bạn đã là nhà phát triển"*.
3. **Bật Gỡ lỗi mạng (ADB)**:
   - Quay lại menu trước > Chọn mục mới xuất hiện: **Tùy chọn cho nhà phát triển (Developer Options)**.
   - Gạt **Bật** mục **Gỡ lỗi USB (USB Debugging)**.
   - Gạt **Bật** mục **Gỡ lỗi qua mạng (Wireless / Network Debugging)** *(nếu thiết bị có mục này)*.
4. **Xem địa chỉ IP của TV**:
   - Mở mục **Cài đặt** > **Mạng và Internet (Network & Internet)** > Bấm vào mạng Wi-Fi đang kết nối để xem IP (ví dụ: `192.168.1.15`).

---

## 2. Hướng dẫn chi tiết cho Điện thoại Android

> [!IMPORTANT]
> **Không tải Termux từ Google Play Store** vì phiên bản trên CH Play đã ngừng phát triển từ lâu, sẽ bị lỗi không tải được các gói lệnh.

### Bước 1: Cài đặt ứng dụng Termux
Tải tập tin cài đặt Termux chính thức từ F-Droid:
* [Tải Termux APK chính thức (F-Droid)](https://f-droid.org/repo/com.termux_1000.apk)

### Bước 2: Chạy công cụ cài đặt
1. Mở ứng dụng **Termux** vừa cài đặt trên điện thoại.
2. Sao chép và dán toàn bộ lệnh bên dưới vào Termux, sau đó nhấn **Enter**:

```bash
pkg update -y && pkg install git python android-tools -y && rm -rf android-tv-adb-installer && git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git && cd android-tv-adb-installer && python installer.py
```

### Bước 3: Xác nhận kết nối trên màn hình TV
1. Chương trình sẽ tự động quét mạng nội bộ trong 1-2 giây và hiển thị địa chỉ TV tìm thấy.
2. Nhấn phím **Enter** trên bàn phím điện thoại để chọn TV.
3. **Nhìn lên màn hình TV**: TV sẽ hiện cửa sổ thông báo *"Cho phép gỡ lỗi USB?" (Allow USB debugging?)*:
   - Dùng điều khiển TV tích chọn vào ô: **"Luôn cho phép từ máy tính này" (Always allow from this computer)**.
   - Bấm **Cho phép / OK**.

### Bước 4: Chọn số ứng dụng để cài đặt
Màn hình Termux sẽ hiển thị toàn bộ 110+ ứng dụng dạng bảng 2 cột rõ ràng, được đánh số liên tục từ `[ 1]` đến `[111]`:

* **Cài 1 ứng dụng lẻ**: Nhập số thứ tự của app (ví dụ: gõ `58` để cài SmartTube YouTube không quảng cáo) rồi bấm Enter.
* **Cài nhiều ứng dụng cùng lúc**: Nhập các số cách nhau bởi dấu phẩy (ví dụ: `16, 50, 58, 108` để cài Phim4K, TiviMate, SmartTube và Downloader).
* **Cài trọn gói một danh mục**: Nhập khoảng số từ-đến (ví dụ: `1-15` để cài toàn bộ nhóm Truyền hình & Bóng đá).
* **Cài tất cả**: Nhập `all`.
* **Tìm kiếm ứng dụng**: Gõ chữ `T` để tìm theo từ khóa.

Ứng dụng sẽ tự động được tải về và cài đặt thẳng vào TV trong vài giây.

### Các lần sử dụng tiếp theo
Khi cần cài thêm ứng dụng, bạn chỉ cần mở Termux và gõ:
```bash
cd android-tv-adb-installer && python installer.py
```

---

## 3. Hướng dẫn cho iPhone và iPad (iOS)

Do iOS có cơ chế bảo mật hạn chế chạy nhị phân ADB cục bộ, bạn sử dụng 1 trong 2 phương pháp sau:

### Phương pháp A: Cài đặt qua trình duyệt Web ADB (Không cần ứng dụng)
1. Đảm bảo TV đã bật Gỡ lỗi mạng (Wireless Debugging) theo [Bước 1](#1-buoc-chuan-bi-tren-android-tv).
2. Mở trình duyệt Safari trên iPhone/iPad, truy cập [Web ADB](https://app.webadb.com/).
3. Nhập địa chỉ IP TV và kết nối qua cổng mặc định `5555`.
4. Tải tệp APK từ [Danh sách ứng dụng](#danh-sach-ung-dung) bên dưới và nạp trực tiếp vào TV.

### Phương pháp B: Chuyển tập tin qua ứng dụng Send Files to TV
1. Cài app **Send Files to TV** trên cả iPhone (App Store) và TV (Google Play).
2. Tải APK ứng dụng mong muốn về iPhone.
3. Bấm Gửi (Send) tệp APK sang TV và tiến hành cài đặt.

---

## 4. Hướng dẫn cho Máy tính

### 🪟 Windows

1. Tải toàn bộ mã nguồn: Bấm nút xanh **Code** > **Download ZIP** trên GitHub và giải nén.
2. Nhấp đúp chuột vào tập tin `install_windows.bat` *(chương trình sẽ tự tải Google Platform Tools nếu máy tính chưa có)*.
3. Hoặc mở PowerShell trong thư mục vừa tải và chạy:
```powershell
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python installer.py
```

### 🍏 macOS

1. Mở Terminal và cài môi trường qua Homebrew:
```bash
brew install android-platform-tools python
```
2. Chạy công cụ:
```bash
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python3 installer.py
```

### 🐧 Linux (Ubuntu, Debian, Fedora, Arch Linux)

1. Cài đặt ADB:
   - **Debian / Ubuntu:** `sudo apt update && sudo apt install -y adb python3 git`
   - **Fedora:** `sudo dnf install -y android-tools python3 git`
   - **Arch Linux:** `sudo pacman -S android-tools python git`
2. Chạy công cụ:
```bash
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python3 installer.py
```

---

## Danh sách ứng dụng

Toàn bộ 110+ ứng dụng được phân loại rõ ràng. Nhấp vào từng danh mục để xem chi tiết và tải lẻ từng tệp APK nếu muốn:

<details>
<summary><b>TRUYỀN HÌNH & BÓNG ĐÁ (15 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **Get Out 2 end** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.end.apk) |
| 2 | **Get Out 2.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.0.apk) |
| 3 | **SportsTV v5.2.3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV_5.2.3.apk) |
| 4 | **SportsTV v4.5** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV-v4.5-Android5.apk) |
| 5 | **SportzX v3.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_3.2v.apk) |
| 6 | **SportzX v2.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_2.6v.apk) |
| 7 | **Hóng TV** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hongtv.apk) |
| 8 | **Xem TV 5.8.8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/XemTV_v5.8.8.apk) |
| 9 | **CricHDaiTV_v5.12** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CricHDaiTV-v5.12.apk) |
| 10 | **TV365_v7** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TV365_v7.apk) |
| 11 | **vAppTV** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vAppTV.apk) |
| 12 | **VTVgoTV_v11.12.30** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVgoTV_v11.12.30.apk) |
| 13 | **VTVprime_v1.7.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVprime_v1.7.0.apk) |
| 14 | **Cricfy_V6.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Cricfy_V6.6.apk) |
| 15 | **GeeSports_V3.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/GeeSports_%28V3.6%29.apk) |

</details>

<details>
<summary><b>PHIM 4K (6 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **Phim4K TV 2.6.8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/phim4k_TV_2.6.8.apk) |
| 2 | **Phim4K Mobile** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android%20Full.apk) |
| 3 | **Phim4K Android** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android.apk) |
| 4 | **Film4k.net ATV** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-arm64-v8a-debug8.apk) |
| 5 | **Film4k.net ATV v7a** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-armeabi-v7a-debug8.apk) |
| 6 | **Film4k ATV x86_64-debug8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-x86_64-debug8.apk) |

</details>

<details>
<summary><b>XEM PHIM (23 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **Gu-Phim_v1.0_Windows** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Windows.zip) |
| 2 | **Gu-Phim_v1.0_Mobile_Tablet_TV** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Mobile-Tablet-TV.apk) |
| 3 | **Hiphim mobile** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphim150android.apk) |
| 4 | **Hiphim Tivi** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphimtv.apk) |
| 5 | **NVCPhim_v2.2.8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) |
| 6 | **NVC_Movie** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVC_Movie.apk) |
| 7 | **hieuga** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hieuga.apk) |
| 8 | **vuagiaitri** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vuagiaitri.apk) |
| 9 | **cobephim-tv** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtv.apk) |
| 10 | **cobephim mobile** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtvphone_v1.5.apk) |
| 11 | **rapphim-0.2.1-mobile** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-0-2-1-mobile.apk) |
| 12 | **rapphim-1.0.1-tv** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-1-0-1-tv.apk) |
| 13 | **saigonphim-tv** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/saigonphim.apk) |
| 14 | **Chợ_Phim** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/chophim.apk) |
| 15 | **CloudStream_4.7.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CloudStream_%5B4.7.0%5D.apk) |
| 16 | **NETFLY_v3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NETFLY_v3.apk) |
| 17 | **NVC_Movie_TV_v2.6.10** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) |
| 18 | **TiemGiaiTri_v1.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiemGiaiTri.apk) |
| 19 | **VAX_Player_1.6.5** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VAX_Player_1.6.5_%286666%29.apk) |
| 20 | **VaxPlayer_1.7.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.apk) |
| 21 | **VaxPlayer_1.7.6_iOS** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.ipa) |
| 22 | **DaoPhim_TV_1.0.3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-1.0.3-tv.apk) |
| 23 | **DaoPhim_Mobile** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-mobile.apk) |

</details>

<details>
<summary><b>PHẦN MỀM IPTV (20 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **HSTIVI_2.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HSTIVI_2.6.apk) |
| 2 | **IPTV_PRO** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/IPTV_PRO.apk) |
| 3 | **M3u-IPTV-v3.0.11-Mod** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/m3u-iptv-3.0.19.apk) |
| 4 | **OTT_Navigator_v1.7.4.1_Mod** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/OTT.apk) |
| 5 | **SparkleTV** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SparkleTV.apk) |
| 6 | **TiviMate_v5.1.6_MOD** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_v5.1.6_MOD.apk) |
| 7 | **quantv** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/quantv.apk) |
| 8 | **televizo_v1.9.6.50_premium** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/televizo_v1.9.6.50_premium.apk) |
| 9 | **tivimate_2.1.5_premium** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tivimate_2.1.5_premium.apk) |
| 10 | **Backup_Host_5.1.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Backup_Host_5.1.6.tmb) |
| 11 | **TiviMate_5.3.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate-5.3.0.apk) |
| 12 | **Televizo_byphaptx52022** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) |
| 13 | **Hbo Max** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hbomax.apk) |
| 14 | **Smart tube** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/smarttube.apk) |
| 15 | **PCRTV_4.1.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/PCRTV_%5B4.1.0%5D.apk.zip) |
| 16 | **QTV3.9_Vip** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/QTV3.9_Vip_pass123%40123.apk) |
| 17 | **Televizo_v1.9.6.50_Premium** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_v1.9.6.50_Premium.apk) |
| 18 | **Televizo_byphaptx52022_zip** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) |
| 19 | **TiviMate_5.1.6_BannerMod_Spydog** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6___BannerM0d_Spydog.apk.zip) |
| 20 | **TiviMate_5.1.6_v2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6_%28v2%29.apk.zip) |

</details>

<details>
<summary><b>YOUTUBE TV (9 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **ToTube** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ToTube.apk) |
| 2 | **Youtube_1.0.8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ytb2.apk) |
| 3 | **vanced_youtube_v20** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced_youtube_v20.apk) |
| 4 | **vanced_youtube_music** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced.to_vanced_youtube_music.apk) |
| 5 | **microg_v0.3.13** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/microg_v0.3.13.apk) |
| 6 | **mapvoice** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mapvoice.apk) |
| 7 | **supervoice-mod-ATV14** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice-mod-ATV14.apk) |
| 8 | **supervoice_ATV9+** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice_ATV9%2B.apk) |
| 9 | **supperVoice-2.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supperVoice-2.2.apk) |

</details>

<details>
<summary><b>TOOL (CÔNG CỤ) (14 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **UFO VPN v2.2.3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/UFOVPNv2.2.3.apk) |
| 2 | **Kiwi VPN v56.20.12** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/KiwiVPNv56.20.12.apk) |
| 3 | **Coc_Coc_Lite_1.6** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Coc_Coc_Lite_1.6.apk) |
| 4 | **Autostart+v4.1.1_Modded_** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Autostart%2Bv4.1.1_Modded_.apk) |
| 5 | **_ATV_app__TV_AppsDrawer** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/_ATV_app__TV_AppsDrawer.apk) |
| 6 | **atvTools_v1.3.0_42-mod** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/atvTools_v1.3.0_42-mod.apk) |
| 7 | **tvQuickActions_Pro_v3.6.0__Patched** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.6.0__Patched_.apk) |
| 8 | **TvQuickAction_3.0.8** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TvQuickAction_3.0.8.apk) |
| 9 | **TvQuickActions_Pro_v3.7.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.7.0_%28405%29.apk) |
| 10 | **Remote_for_Android_TV_v6.0.3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Remote_for_Android_TV_v6.0.3_%28no_ads%29.apk) |
| 11 | **Developer_Tools_2.1.1** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Developer_Tools_2.1.1.apk.jar) |
| 12 | **Buttons_remapper_v1.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Buttons_remapper_v1.2.apk) |
| 13 | **Button_Mapper_v3.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Button_Mapper_v3.2.apk.zip) |
| 14 | **Add_Tivi_Remote** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Add_Tivi_Remote.apk) |

</details>

<details>
<summary><b>GIAO DIỆN TIVI (7 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **ATV Launcher** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ATV-Launcher-v0136.apk) |
| 2 | **Pro_Launcher_(PhapViet)** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Pro_Launcher_%28PhapViet%29.apk) |
| 3 | **Project_Launcher** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Project_Launcher.apk) |
| 4 | **ProTVLauncher_V5** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ProTVLauncher_V5.apk) |
| 5 | **Launcher-Manager_1.0.4** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Launcher-Manager-1.0.4.apk) |
| 6 | **HomeTV_Launcher_6.3.1** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HomeTV_Launcher_6.3.1.apk) |
| 7 | **Google_TV_Home_1.0.4** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Google_TV_Home_1.0.4.apk) |

</details>

<details>
<summary><b>STORE (CỬA HÀNG TẢI APP) (12 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **Aptoide_TV_5.1.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Aptoide_TV_5.1.2.apk) |
| 2 | **DLStore_v16.0.4** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/DLStore_v16.0.4.apk) |
| 3 | **HDPlay_Store** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HDPlay_Store_%5B3.1.9%5D.apk) |
| 4 | **Movie Legend Store** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Movie%20Legend%20Store.apk) |
| 5 | **TTV_Store_3.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TTV_Store_3.0.apk) |
| 6 | **beecubestore2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/beecubestore2.apk) |
| 7 | **Kho_Ung_Dung_MCU** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/box_store_mcu_v1.apk) |
| 8 | **EMOTN_Store** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/emotnstore.apk) |
| 9 | **FERRARI_DOWNLOADER** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) |
| 10 | **MStore_v2.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mstore.apk) |
| 11 | **ĐôngAnhStore_25.3.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Dong_Anh_TV_3.6.apk) |
| 12 | **BoxStoreMCU_v2.0** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/BoxStoreMCU_v2.0.apk) |

</details>

<details>
<summary><b>APP NHẬP CODE & QUẢN LÝ TẬP TIN (5 ứng dụng)</b></summary>
<br>

| STT | Tên ứng dụng | Tải về (APK) |
|:---:|:---|:---:|
| 1 | **Downloader_AFTV_v1.4.5** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.4.5.apk) |
| 2 | **Downloader_AFTV_v1.5.3** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.5.3.apk) |
| 3 | **File_Manager_3.8.2** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/File_Manager_3.8.2.apk) |
| 4 | **Xplorer_File_Manager_Premium** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Xplorer_File_Manager_Premium.apk) |
| 5 | **FERRARI_DOWNLOADER_zip** | [Tải xuống](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) |

</details>

---

## Xử lý lỗi thường gặp

* **Lỗi `failed to connect to <IP>:5555: Connection refused`**
  - Kiểm tra xem TV và điện thoại/máy tính có đang kết nối chung một mạng Wi-Fi không.
  - Tắt và bật lại mục **Gỡ lỗi USB** trong Cài đặt TV, hoặc khởi động lại TV.
* **Lỗi `device unauthorized`**
  - TV chưa được cấp quyền kết nối. Hãy nhìn lên màn hình TV, dùng điều khiển bấm chọn **"Luôn cho phép từ máy tính này"** và chọn **OK**.
* **Lỗi `INSTALL_FAILED_UPDATE_INCOMPATIBLE`**
  - Ứng dụng đã có sẵn trên TV nhưng bị xung đột chữ ký với bản mới. Hãy gỡ cài đặt phiên bản cũ trên TV trước rồi cài lại.

---

## Tuyên bố pháp lý và Bản quyền

1. **Mục đích phi thương mại:** Dự án được xây dựng và duy trì hoàn toàn vì mục đích học thuật, nghiên cứu giao thức điều khiển thiết bị qua ADB và hỗ trợ quản trị thiết bị cá nhân. Tác giả không kinh doanh, không thu bất kỳ khoản phí nào và không phân phối quảng cáo.
2. **Không lưu trữ nội dung (Zero Hosting):** Tác giả và kho lưu trữ này hoàn toàn không lưu trữ, không chỉnh sửa và không phát tán bất kỳ tập tin nhị phân (APK/IPA) nào. Toàn bộ đường dẫn tải về được trích dẫn khách quan từ các nguồn tổng hợp công khai trên Internet (nguồn: tinhlagi).
3. **Trách nhiệm người dùng:** Người dùng hoàn toàn tự chịu trách nhiệm về tính pháp lý khi tải về, cài đặt và sử dụng các ứng dụng trên thiết bị cá nhân của mình theo quy định pháp luật sở tại.
4. **Quy trình gỡ bỏ nội dung (Notice and Takedown):** Chủ sở hữu bản quyền có quyền yêu cầu gỡ bỏ bất kỳ liên kết trích dẫn nào liên quan đến sản phẩm của mình. Vui lòng mở GitHub Issue hoặc gửi thông báo tới: `nguyenlocthanh796@users.noreply.github.com`. Liên kết sẽ được gỡ bỏ khỏi kho dữ liệu trong vòng 24 đến 48 giờ sau khi tiếp nhận thông tin hợp lệ.

---

## Giấy phép

Dự án được phát hành theo giấy phép mã nguồn mở **MIT License**. Xem chi tiết tại tập tin [LICENSE](LICENSE).

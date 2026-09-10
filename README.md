# Android TV ADB Installer (Cài App TV từ Điện Thoại)

> Tổng hợp hơn 110+ ứng dụng Android TV, Google TV, TV Box tốt nhất (Xem Phim 4K, Bóng Đá, Truyền Hình IPTV, YouTube Không Quảng Cáo, Tiện Ích) và công cụ tự động cài đặt qua ADB WiFi trực tiếp từ điện thoại Android (Termux) hoặc máy tính.

---

## Hướng dẫn cài đặt từ Điện Thoại sang TV (Không cần máy tính)

### Bước 1: Bật ADB Debugging trên Android TV
1. Vào **Cài đặt (Settings)** trên TV -> **Tùy chọn thiết bị (Device Preferences)** -> **Giới thiệu (About)**.
2. Tìm dòng **Bản dựng hệ điều hành Android (Build Number)** và bấm nút **OK/Chọn 7 lần** trên điều khiển cho đến khi hiện thông báo *"Bạn đã là nhà phát triển"*.
3. Quay lại menu trước -> vào mục **Tùy chọn cho nhà phát triển (Developer Options)**.
4. Bật:
   - **Gỡ lỗi USB (USB Debugging)**.
   - **Gỡ lỗi qua mạng (Network Debugging / Wireless Debugging)** (nếu có).
5. Vào **Cài đặt mạng (Network & Internet)** xem địa chỉ **IP của TV** (ví dụ: `192.168.1.50`). Đảm bảo TV và điện thoại cùng kết nối vào một mạng Wi-Fi.

### Bước 2: Cài đặt và chạy trên Điện Thoại Android (Termux)
1. Tải ứng dụng **Termux** từ F-Droid hoặc GitHub Termux Release.
2. Mở Termux và dán lệnh sau:
```bash
pkg update && pkg install git python android-tools -y
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python installer.py
```
*(Hoặc chạy script shell: `bash install_tv.sh`)*

3. Nhập địa chỉ **IP của TV** khi được hỏi. Nhìn lên màn hình TV và bấm chọn **"Luôn cho phép từ máy này" (Always allow)**.
4. Chọn app muốn cài từ menu, ứng dụng sẽ được tải và cài đặt tự động lên TV trong vài giây.

---

## Cách chạy trên Máy Tính (Windows / macOS / Linux)

Yêu cầu máy tính có cài sẵn `adb` và `python3`.
```bash
git clone https://github.com/nguyenlocthanh796/android-tv-adb-installer.git
cd android-tv-adb-installer
python installer.py
```

---

## Danh Sách Đầy Đủ 110+ Ứng Dụng (Link Trực Tiếp & Mã Downloader)


### 📂 TRUYỀN HÌNH - ⚽ ĐÁ BANH

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **Get Out 2 end** | `393939` | mới nhất • 158 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.end.apk) | [Mở Web](https://tinhlagi.pro/app/?download=d0278ce706af13ba9db87f5924dfe63e5f9aeb479ae4d59e7c86e5760bd16f81) |
| **Get Out 2.0** | `3074016` | v2.0 • 31 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Get_Out_2.0.apk) | [Mở Web](https://tinhlagi.pro/app/?download=d972e20211c1f55d3f6eecc1e1b82616ebad258a172771babcdf8e059731abf1) |
| **SportsTV v5.2.3** | `8705526` | v5.2.3 • 123 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV_5.2.3.apk) | [Mở Web](https://tinhlagi.pro/app/?download=5c637a86e6ba1fca54695bb6a1c050f1ca04c6aa9a7b0a1cd08c8a6edbb47c4b) |
| **SportsTV v4.5** | `393939` | v4.5 • 24 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportsTV-v4.5-Android5.apk) | [Mở Web](https://tinhlagi.pro/app/?download=8decaa90c2bb90e7b6c241758e18cc69e7d346bf4ef6d83595cd249fcfa1ba49) |
| **SportzX v3.2** | `393939` | v3.2 • 48 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_3.2v.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1f17383202c211a3836255218829910c0b82170e507f2029a180220c4ef31fd2) |
| **SportzX v2.6** | `393939` | v2.6 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SportzX_2.6v.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e85fe4c36ac13a9ba8d89678513c8282f7d33240b3c4b1b42c850307bb61e151) |
| **Hóng TV** | `7027363` | v1.1.8 • 81 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hongtv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=8f46980481a3413772e7de0e42290a31c5d33dec0c4d22d6d9df90d62b99157a) |
| **Xem TV 5.8.8** | `393939` | 5.8.8 • 59 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/XemTV_v5.8.8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a4b7fbe87445dac7faca7111f16807927a3ca9cce5da4072373f6b211bf73917) |
| **CricHDaiTV_v5.12** | `393939` | v5.12 • 23 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CricHDaiTV-v5.12.apk) | [Mở Web](https://tinhlagi.pro/app/?download=0824a086be19771845011cd792e4caa6fc1b6da5fe37074c236ca85ceee4001f) |
| **TV365_v7** | `393939` | v7.0 • 43 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TV365_v7.apk) | [Mở Web](https://tinhlagi.pro/app/?download=507efc95edf11b352b093a8c71b1ebdb4ae7dfbdefbd4ef74b515c031df84169) |
| **vAppTV** | `9788306` | v1.0.0 • 33 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vAppTV.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a58871f983b33fc0a0fb97c1448e3cf31aced3882c6b912de7e90fb3b49fd3c7) |
| **VTVgoTV_v11.12.30** | `393939` | v11.12.30 • 19 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVgoTV_v11.12.30.apk) | [Mở Web](https://tinhlagi.pro/app/?download=691c124b766e7ed91bd6d22b8bbcab7d4fe134341d78722bbebfc357b36bde9b) |
| **VTVprime_v1.7.0** | `393939` | v1.7.0 • 21 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VTVprime_v1.7.0.apk) | [Mở Web](https://tinhlagi.pro/app/?download=5e0d568e768093b7050c343ce3c3f958dd7b3d5a7faccac13414cbe0eb666bb1) |
| **Cricfy_V6.6** | `1213128` | v6.6 • 13 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Cricfy_V6.6.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ac1ac8728b5edb58f179297f6279aa9990d4f46a6ff61348479578376eea9b3d) |
| **GeeSports_V3.6** | `7266756` | v3.6 • 29 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/GeeSports_%28V3.6%29.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a7debf77f499c0ac69935f2b707e104f01c88cbc91815ffb469a65a7d53e50d5) |

### 📂 PHIM 4K

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **Phim4K TV 2.6.8** | `4411335` | v2.6.8 • 119 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/phim4k_TV_2.6.8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=efa4815b17025156434a9c38832e372a45053c3c1c53cc51f6ac7264f862b1ef) |
| **Phim4K Mobile** | `4833418` | v2.6.1 • 31 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android%20Full.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e95b7f65ea05ec03454164236b818f5deaf242915d35766976ed2fee2516054d) |
| **Phim4K Android** | `393939` | v2.6.1 • 26 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Phim4K%20v2.6.1%20Android.apk) | [Mở Web](https://tinhlagi.pro/app/?download=8970a1e5a0e699cf69f60af65c7082f047ac5203b3125327e9d82ebabf2862bc) |
| **Film4k.net ATV** | `393939` | v1.0.0 • 29 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-arm64-v8a-debug8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a84f9135cd47bd73c21f9f710b4dd732da0a0c2e7f0cbe032b9dacd46592d63c) |
| **Film4k.net ATV v7a** | `393939` | v1.0.0 • 20 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-armeabi-v7a-debug8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a6ffaf07c832de5cc7ca5206703f1cdc7fd0aea39b29856361050e07486164b4) |
| **Film4k ATV x86_64-debug8** | `393939` | v1.0.0 • 14 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Film4kATV-x86_64-debug8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1021105fcd9bb26a9c2fe9aac59739150b6ec8aa75ab71aa0472516578f3fe04) |

### 📂 XEM PHIM

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **Gu-Phim_v1.0_Windows** | `393939` | v1.0 • 27 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Windows.zip) | [Mở Web](https://tinhlagi.pro/app/?download=f1979bbe6e1636fdfbdb75f872e613d9ad9a0237587915a58afcadbca736a836) |
| **Gu-Phim_v1.0_Mobile_Tablet_TV** | `393939` | v1.0 • 20 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Gu-Phim-v1.0-Mobile-Tablet-TV.apk) | [Mở Web](https://tinhlagi.pro/app/?download=2a4be789d9aea968930192cb6d189a049487fde87f91ebff3c29f9f567cc8bcb) |
| **Hiphim mobile** | `393939` | v1.0.0 • 8 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphim150android.apk) | [Mở Web](https://tinhlagi.pro/app/?download=07ac6cd4f7564103c400e52b7f0d86bff6a171255ab69f8682a7c5d78ca622bb) |
| **Hiphim Tivi** | `393939` | v1.0.0 • 22 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hiphimtv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=50944a92e609cba5eafb0ebf05a787b4339fe059091f34a4dbe685ac21eedb04) |
| **NVCPhim_v2.2.8** | `2653652` | v2.2.8 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ef48bd95fd5440a25c8bd9251c934e1c0a5195c9a1bfbefdbc5ec098898f6a2c) |
| **NVC_Movie** | `393939` | v1.0.0 • 2 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVC_Movie.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ac731837424ec96bb0ee9e8f9a6f84aeb96ff66b5110bcdb8a03a6b9a1dfce2f) |
| **hieuga** | `1059695` | v1.0.0 • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hieuga.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e575fbcdda248b527eefb31bbff78666a8d4f385c6e6dff172335b50fe34d16d) |
| **vuagiaitri** | `7716517` | v1.0.0 • 5 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vuagiaitri.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1f201ff664042a84fddfd6f80163d080482ae280df2ab2752ab411f78d745627) |
| **cobephim-tv** | `6207062` | v1.0.0 • 31 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=2448cf57d59cc61476b67f954b91da2862192babe65121bb973971d271e3268c) |
| **cobephim mobile** | `6207062` | v1.0.0 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/cobephimtvphone_v1.5.apk) | [Mở Web](https://tinhlagi.pro/app/?download=894ef05691f44736c32a65ee4069416433f830b10eda9babf1a4023402b7cc2d) |
| **rapphim-0.2.1-mobile** | `393939` | v0.2.1 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-0-2-1-mobile.apk) | [Mở Web](https://tinhlagi.pro/app/?download=14d81041203cf76a8daf44af457f4766c19220e6f719a95e59ae9bb1c2fc4c0b) |
| **rapphim-1.0.1-tv** | `6766306` | v1.0.1 • 9 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/rapphim-1-0-1-tv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=0961ecef17593d4c819ea2d706d71c6ab717f6a64abfd5be0a77d85f93d723cd) |
| **saigonphim-tv** | `7048453` | v1.0.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/saigonphim.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ba8d4c7da8461cbdbec1d1e60d6297a52edce85ce0db65a0fd947904b7570a98) |
| **Chợ_Phim** | `5774068` | v1.0.0 • 24 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/chophim.apk) | [Mở Web](https://tinhlagi.pro/app/?download=3fecac0bba77e76f3c349c8b0119be0e8d638587d9705b58a3040bfecf960df8) |
| **CloudStream_4.7.0** | `393939` | v4.7.0 • 15 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/CloudStream_%5B4.7.0%5D.apk) | [Mở Web](https://tinhlagi.pro/app/?download=de0f6b280d84cc68ecaac166c672fba7a951b9e6f887c27b2f6712d3ba191263) |
| **NETFLY_v3** | `2844821` | v3.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NETFLY_v3.apk) | [Mở Web](https://tinhlagi.pro/app/?download=65f92f3e20939d4332f07c6a08468fb2f89a56c8f73829d6b387efb86a98a823) |
| **NVC_Movie_TV_v2.6.10** | `1659529` | v2.6.10 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/NVCPhim_v2.2.8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=b0467ddc8d58c4f2dc2a689540c4e53def1ab2b5af9e9565fc280d8cdb218edc) |
| **TiemGiaiTri_v1.0** | `393939` | v1.0.0 • 11 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiemGiaiTri.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e4ca4c7a28841800338892893700a433502e8a0fba74ba213749b9a1b89fb360) |
| **VAX_Player_1.6.5** | `1387135` | v1.6.5 • 5 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VAX_Player_1.6.5_%286666%29.apk) | [Mở Web](https://tinhlagi.pro/app/?download=16c84004a20c5ecf428af3e2765a824823d601ae80ef419cf3544e0742325cb5) |
| **VaxPlayer_1.7.6** | `393939` | v1.7.6 • 11 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.apk) | [Mở Web](https://tinhlagi.pro/app/?download=883f1283d76d03dd60cd43daafb13ab83c676655a30cc255e1838c9ac82c4cfe) |
| **VaxPlayer_1.7.6_iOS** | `393939` | v1.7.6 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/VaxPlayer1.7.6.ipa) | [Mở Web](https://tinhlagi.pro/app/?download=9d7a608ec6525aaf89ace2ce4108e05bded8ea7d70ee34d36b9116952fc05166) |
| **DaoPhim_TV_1.0.3** | `393939` | v1.0.3 • 31 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-1.0.3-tv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=023ceb75387101df2536d2fba7cdeb5944ace55131e27ca7b6131c348b489050) |
| **DaoPhim_Mobile** | `393939` | v1.0.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/daophim-mobile.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4c45424f319de3ac3ed603ac43f1e97036cbe64636b0f423e852b062d044bf42) |

### 📂 PHẦN MỀM IPTV

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **HSTIVI_2.6** | `393939` | v1.0.0 • 33 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HSTIVI_2.6.apk) | [Mở Web](https://tinhlagi.pro/app/?download=0c1fec12c6753d40487cdcc6a829099710f9776fab7328b39b68e0122c122d70) |
| **IPTV_PRO** | `393939` | v1.0.0 • 46 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/IPTV_PRO.apk) | [Mở Web](https://tinhlagi.pro/app/?download=bda24b9bf4e719070694b791d41ced167b4b522903d4915149ecc281ad2de517) |
| **M3u-IPTV-v3.0.11-Mod** | `393939` | v3.0.11 • 14 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/m3u-iptv-3.0.19.apk) | [Mở Web](https://tinhlagi.pro/app/?download=35869061431564e123699fbc4e009ecd760a765eb31203a5151151b75cf7f7a1) |
| **OTT_Navigator_v1.7.4.1_Mod** | `1995826` | v1.7.4.1 • 15 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/OTT.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e1bac048d8347d69a66469c5d6139d859e25639925170a148d0e461524f77dd4) |
| **SparkleTV** | `8439261` | v1.0.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/SparkleTV.apk) | [Mở Web](https://tinhlagi.pro/app/?download=7c732739ab00a8a4062d6eeb58004f238011176af8a823a7a59dc44ddfda977e) |
| **TiviMate_v5.1.6_MOD** | `393939` | v5.1.6 • 27 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_v5.1.6_MOD.apk) | [Mở Web](https://tinhlagi.pro/app/?download=71a5439fb2ec1868cbf6ac3a6d2c3802fdf4a49d560536a09137b05acc1c60e0) |
| **quantv** | `393939` | v1.0.0 • 17 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/quantv.apk) | [Mở Web](https://tinhlagi.pro/app/?download=cf200b15f64b18ce6adf0d4d09e9e9bc337771e62509ee6321c7874505cb0b4d) |
| **televizo_v1.9.6.50_premium** | `6508980` | v1.9.6.50 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/televizo_v1.9.6.50_premium.apk) | [Mở Web](https://tinhlagi.pro/app/?download=013bc5292ad6d863f45ff92e2a113f45a11a91a61fd70a50ff3e10af23c982ba) |
| **tivimate_2.1.5_premium** | `393939` | v2.1.5 • 14 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tivimate_2.1.5_premium.apk) | [Mở Web](https://tinhlagi.pro/app/?download=9ea73a23e97769bc52b65a5e5a0c8d5c70f96d66da08cd059669cf957b8df7ac) |
| **Backup_Host_5.1.6** | `4739677` | v5.1.6 • 7 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Backup_Host_5.1.6.tmb) | [Mở Web](https://tinhlagi.pro/app/?download=2c8672fc4f5d944c761e01a708160dbbfe27e1e7c39afabf519213f8c7f2d501) |
| **TiviMate_5.3.0** | `393939` | v5.3.0 • 11 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate-5.3.0.apk) | [Mở Web](https://tinhlagi.pro/app/?download=561969ebcd33a4d3501dcf520aef94b18a19f0ddfe25ef1f6c8d2fa64b04d059) |
| **Televizo_byphaptx52022** | `393939` | v5.2022 • 8 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=1015df0523a251b02268d700779d3e593d3c464065601b05fc6220794d679b82) |
| **Hbo Max** | `2426878` | v1.0.0 • 12 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/hbomax.apk) | [Mở Web](https://tinhlagi.pro/app/?download=6cd6f014292e1f84cc9bc66bf37ff04a76b25a41c390cbe5e418ac0d90c0e52e) |
| **Smart tube** | `393939` | v1.0.0 • 17 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/smarttube.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4a77c0cf2856d4827369ea2a7efa18ab16f450f86f865a3f03a7577bd5e8527d) |
| **PCRTV_4.1.0** | `4579948` | v4.1.0 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/PCRTV_%5B4.1.0%5D.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=4c13c6a30340d921c34506cd93813d35d87b21ef38692ce29ede5dc3a56e22ee) |
| **QTV3.9_Vip** | `5508842` | v3.9 • 19 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/QTV3.9_Vip_pass123%40123.apk) | [Mở Web](https://tinhlagi.pro/app/?download=9150e2dbfb8863a3841335145ec73f14962cad6a3e1f9bfe36198784b5887a22) |
| **Televizo_v1.9.6.50_Premium** | `393939` | v1.9.6.50 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_v1.9.6.50_Premium.apk) | [Mở Web](https://tinhlagi.pro/app/?download=da30caf02d8375991eab61d9d9a07d09d6d852050ac1402a73823aa869302fd1) |
| **Televizo_byphaptx52022_zip** | `393939` | v5.2022 • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Televizo_byphaptx52022.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=a76c6f11ec330b9a281b4bd3eddc47fda16ed7067924a6a61bb7aece8af179d9) |
| **TiviMate_5.1.6_BannerMod_Spydog** | `393939` | v5.1.6 • 12 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6___BannerM0d_Spydog.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=5b02ce0bc330f5b5332959f63af1841608dcaa7a2887f65cee506609bdcd0635) |
| **TiviMate_5.1.6_v2** | `393939` | v5.1.6 • 12 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TiviMate_5.1.6_%28v2%29.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=9656f87904b26d98bb8ea1228aa5d8dd74b38b2b2741ecb9f439b0d13d051806) |

### 📂 YOUTUBE TV

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **ToTube** | `393939` | v1.0.0 • 15 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ToTube.apk) | [Mở Web](https://tinhlagi.pro/app/?download=5b5503034a5172069285825217dc9cd5f358b72e4a55df211d55f187b795da7c) |
| **Youtube_1.0.8** | `8788599` | v1.0.8 • 31 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ytb2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=a2b14e0839fd34b7783670e9ef42c79a7619372a0346919f07b968606d2010f3) |
| **vanced_youtube_v20** | `393939` | v20 • 23 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced_youtube_v20.apk) | [Mở Web](https://tinhlagi.pro/app/?download=aec49c73dbf146174f977e1fc9a937c768bb014fae7ce74362f7865dc95fe14d) |
| **vanced_youtube_music** | `393939` | v8.40.54 • 5 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/vanced.to_vanced_youtube_music.apk) | [Mở Web](https://tinhlagi.pro/app/?download=308d2d8cb39c1ece450a41aca2d77ab6f4258c173a4ac1de9cdf45d648e20876) |
| **microg_v0.3.13** | `393939` | v0.3.13 • 11 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/microg_v0.3.13.apk) | [Mở Web](https://tinhlagi.pro/app/?download=8109cdc17fc7f4fbfc60a70bd30c132010f228ffb113ea11f8695559d7220321) |
| **mapvoice** | `7701927` | v1.0.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mapvoice.apk) | [Mở Web](https://tinhlagi.pro/app/?download=01be61aef32e265d85f79771b859ff45aa7c28ecb267abec14353357044de1c4) |
| **supervoice-mod-ATV14** | `393939` | v14.0 • 6 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice-mod-ATV14.apk) | [Mở Web](https://tinhlagi.pro/app/?download=40299003fa01db13d96a9da5fe2d571d0ca19ec721d733b090b8ee1637cc2104) |
| **supervoice_ATV9+** | `393939` | v9.0+ • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supervoice_ATV9%2B.apk) | [Mở Web](https://tinhlagi.pro/app/?download=d94fe98da87da444601a11dfeddc0390c8f1005ce740425fc585d28408f54653) |
| **supperVoice-2.2** | `393939` | v2.2 • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/supperVoice-2.2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=095174332c1998691b1aaacf0a7e94ec8d8a60d4cba62585e77e1c2eeefb5a03) |

### 📂 TOOL (CÔNG CỤ)

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **UFO VPN v2.2.3** | `393939` | v1.0.0 • 1.638 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/UFOVPNv2.2.3.apk) | [Mở Web](https://tinhlagi.pro/app/?download=614c078e5e8a5ce3f61ead632ce6330f35285ffb5261bd323e0f7bdaf4857e10) |
| **Kiwi VPN v56.20.12** | `393939` | v1.0.0 • 1.637 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/KiwiVPNv56.20.12.apk) | [Mở Web](https://tinhlagi.pro/app/?download=684d79d088c3ec0bf3f2cafc03f3a2084ebb665e2b4b9a222b8932cf6b463b6b) |
| **Coc_Coc_Lite_1.6** | `393939` | v1.6 • 7 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Coc_Coc_Lite_1.6.apk) | [Mở Web](https://tinhlagi.pro/app/?download=fb960a292f1e39d08ff2ca0278b6fd048aefe72387666b197079b638eec415d3) |
| **Autostart+v4.1.1_Modded_** | `393939` | v4.1.1 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Autostart%2Bv4.1.1_Modded_.apk) | [Mở Web](https://tinhlagi.pro/app/?download=e989e308e2827aa881b6ee2efd5db69405528206cf2cfad3a99b2d86ede46fd4) |
| **_ATV_app__TV_AppsDrawer** | `393939` | v1.0.0 • 228 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/_ATV_app__TV_AppsDrawer.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1eb58ee93f8c0e39249819b457ec294b3b752750ae188551acda5d731adc6f05) |
| **atvTools_v1.3.0_42-mod** | `393939` | v1.3.0 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/atvTools_v1.3.0_42-mod.apk) | [Mở Web](https://tinhlagi.pro/app/?download=362adb6e1a1acbf306fb2a183fc9f3ff65a07f811482d9226ebfeabae20b603c) |
| **tvQuickActions_Pro_v3.6.0__Patched** | `393939` | v3.6.0 • 2 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.6.0__Patched_.apk) | [Mở Web](https://tinhlagi.pro/app/?download=112c4485323cb8eee26d174035d6a2a38c351181ebca9be2c8726c76c67e5387) |
| **TvQuickAction_3.0.8** | `393939` | v3.0.8 • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TvQuickAction_3.0.8.apk) | [Mở Web](https://tinhlagi.pro/app/?download=83023a2f7b77fbad901d6d67a51b5546169d68e5e2325a646d6e55aaabdea385) |
| **TvQuickActions_Pro_v3.7.0** | `393939` | v3.7.0 (405) • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/tvQuickActions_Pro_v3.7.0_%28405%29.apk) | [Mở Web](https://tinhlagi.pro/app/?download=6f08972918a45a7f47a2656a43e399be86e78e0d701c368cddf45d244f5c20f9) |
| **Remote_for_Android_TV_v6.0.3** | `393939` | v6.0.3 • 2 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Remote_for_Android_TV_v6.0.3_%28no_ads%29.apk) | [Mở Web](https://tinhlagi.pro/app/?download=6b35ce2c581bfeb9ca1c265137545a0162b9c80004908e7ab7afc30ce3da4ecb) |
| **Developer_Tools_2.1.1** | `393939` | v2.1.1 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Developer_Tools_2.1.1.apk.jar) | [Mở Web](https://tinhlagi.pro/app/?download=ee37ddd31781979ac49fe1d3d1d782122d2caeb87e5b9f602f1c7fc79a6845aa) |
| **Buttons_remapper_v1.2** | `393939` | v1.2 • 2 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Buttons_remapper_v1.2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=edc2a6a55144a32778d9e3cfdedfcc5afdee42a562f4e8bf0f6b3615b5acdd10) |
| **Button_Mapper_v3.2** | `393939` | v3.2 • 1 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Button_Mapper_v3.2.apk.zip) | [Mở Web](https://tinhlagi.pro/app/?download=af15ea26f62d7a791282f402348e65841af733ef80a58da2a4bd9e5e0f557803) |
| **Add_Tivi_Remote** | `393939` | v1.0.0 • 2 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Add_Tivi_Remote.apk) | [Mở Web](https://tinhlagi.pro/app/?download=d93eef933e6fff9ba3c2b8fa68d9e165569aac5479695951b1e3d5c8f15a216f) |

### 📂 GIAO DIỆN TIVI

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **ATV Launcher** | `393939` | v0136 • 20 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ATV-Launcher-v0136.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ed9442c0f2c14041574dbdd496e1ed6f391d18c308538f432997c60848757ec6) |
| **Pro_Launcher_(PhapViet)** | `8513629` | v1.0.0 • 15 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Pro_Launcher_%28PhapViet%29.apk) | [Mở Web](https://tinhlagi.pro/app/?download=55d93eca94497a2e29ceaf6322aabec78dc7dbb903643e525bd6e98e15974691) |
| **Project_Launcher** | `393939` | v1.0.0 • 9 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Project_Launcher.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1dcbdac6c711835b682cad86e7f8a41953a39f31fc5a76fce0267c0e5edcade2) |
| **ProTVLauncher_V5** | `6410730` | v5.0 • 8 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ProTVLauncher_V5.apk) | [Mở Web](https://tinhlagi.pro/app/?download=26de27ef2fd5c4df236753d2bc6593874d45a445acceb08a891431d77a7b5c9e) |
| **Launcher-Manager_1.0.4** | `393939` | v1.0.4 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Launcher-Manager-1.0.4.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ffcdb95fcb068f8692913b078915bc492bfe847576be47d73697a74559a31b14) |
| **HomeTV_Launcher_6.3.1** | `393939` | v6.3.1 • 9 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HomeTV_Launcher_6.3.1.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4c5aba192a85c412e310bdd815337eaae0f1852cffd84f6085f80b9ab5110eec) |
| **Google_TV_Home_1.0.4** | `393939` | v1.0.4 • 12 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Google_TV_Home_1.0.4.apk) | [Mở Web](https://tinhlagi.pro/app/?download=025aef5f86530c04b412afefeb0ece9f580ede1eddbc1d518707efc155934107) |

### 📂 STORE (CỬA HÀNG TẢI APP)

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **Aptoide_TV_5.1.2** | `393939` | v5.1.2 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Aptoide_TV_5.1.2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ff11912048727a6ffd130e2327b1cb7175eccb0536588b0248f0e8dfbcb81462) |
| **DLStore_v16.0.4** | `5103033` | v16.0.4 • 46 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/DLStore_v16.0.4.apk) | [Mở Web](https://tinhlagi.pro/app/?download=fd734e3d7616e26555a271592cb11f8151f53d9f059859af4b8b2726fd152a89) |
| **HDPlay_Store** | `393939` | v3.1.9 • 19 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/HDPlay_Store_%5B3.1.9%5D.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4187df488bca1b5071bde94f3d6d444e56eb9e8e99b1c12b7e64c2df006f07a0) |
| **Movie Legend Store** | `4369204` | v3.1.5 • 8 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Movie%20Legend%20Store.apk) | [Mở Web](https://tinhlagi.pro/app/?download=1bce2ae7ce6bc38550d8cd929dca3fe3d375cbccc28828a88849ccd4d79a955e) |
| **TTV_Store_3.0** | `393939` | v3.0 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/TTV_Store_3.0.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ae2e9970a40dd8c0d7ddb76a947709085d63d34a5ea4d763b9bc70612b939bf4) |
| **beecubestore2** | `393939` | v2.0 • 14 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/beecubestore2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=9bb26704b25650104623dbf73791d07f4aacc97eb8dd812bd496f57a33ea1ba2) |
| **Kho_Ung_Dung_MCU** | `5212814` | v1.0 • 35 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/box_store_mcu_v1.apk) | [Mở Web](https://tinhlagi.pro/app/?download=93f8ad7d3d61ccf732d16e178edaba006fe7826757570b938b08ea37712c2f15) |
| **EMOTN_Store** | `393939` | v1.0.0 • 3 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/emotnstore.apk) | [Mở Web](https://tinhlagi.pro/app/?download=d69f1678ff60976b75b09f5cea06b685caed82c19e88882da784f65ed5433817) |
| **FERRARI_DOWNLOADER** | `5356270` | v1.0.0 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) | [Mở Web](https://tinhlagi.pro/app/?download=87f456be6ff0947c95ce9ee4a91f73895f3ad42b791aa2963fc7f75b536eebbf) |
| **MStore_v2.0** | `393939` | v2.0 • 11 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/mstore.apk) | [Mở Web](https://tinhlagi.pro/app/?download=cf9efb496fe2d294e6550d22ea12e8442642b5f1e572f397c6c9053ee80e5025) |
| **ĐôngAnhStore_25.3.2** | `393939` | v25.3.2 • 44 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Dong_Anh_TV_3.6.apk) | [Mở Web](https://tinhlagi.pro/app/?download=c8e998cff27d910eeba79c673a6e4552a1c83be692e2849e65342f6953fe83a1) |
| **BoxStoreMCU_v2.0** | `393939` | v2.0 • 24 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/BoxStoreMCU_v2.0.apk) | [Mở Web](https://tinhlagi.pro/app/?download=ce5bec21483aabc3884e81555f626c384ab14fd5c2d7e6f85170c85bfe3b9e63) |

### 📂 APP NHẬP CODE &amp; QUẢN LÝ TẬP TIN

| Tên Ứng Dụng | Mã Downloader | Phiên Bản | Link Tải Trực Tiếp (APK) | Web |
|:---|:---:|:---|:---|:---:|
| **Downloader_AFTV_v1.4.5** | `393939` | v1.4.5 • 28 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.4.5.apk) | [Mở Web](https://tinhlagi.pro/app/?download=06f44b47fc32ea8bee800ad987651613651c03071c94e5e0de452a7cd0003365) |
| **Downloader_AFTV_v1.5.3** | `393939` | v1.5.3 • 15 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Downloader_AFTV_v1.5.3.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4c67119dc676f0c78e87d5de273ee90b9e4e42df2590a944d7d6d567f71f735f) |
| **File_Manager_3.8.2** | `393939` | v3.8.2 • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/File_Manager_3.8.2.apk) | [Mở Web](https://tinhlagi.pro/app/?download=4baa129791c9772fe7b3615754059b17dfd6cb6298190596c70f4ef4832ad6f9) |
| **Xplorer_File_Manager_Premium** | `393939` | Premium • 10 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/Xplorer_File_Manager_Premium.apk) | [Mở Web](https://tinhlagi.pro/app/?download=65e5d441005ee35dbbff208b03639538803b236da559e38b5b04ec2b42f89620) |
| **FERRARI_DOWNLOADER_zip** | `393939` | v1.0.0 • 4 lượt tải | [Tải APK](https://pub-fb13fe1daa2c4cf0acf3075c535924da.r2.dev/app/ferraridownloader.apk) | [Mở Web](https://tinhlagi.pro/app/?download=3cef29cd9b0d850055a0f073f3311ee64081a95d92d557392e7245febe2ea969) |

---

## Nguồn dữ liệu & Ghi chú
- Dữ liệu trích xuất từ kho ứng dụng [tinhlagi.pro](https://tinhlagi.pro/app/).
- Mã Downloader sử dụng trực tiếp trên ứng dụng **Downloader by AFTVnews** trên Android TV / Fire TV.
- Bản quyền các ứng dụng thuộc về nhà phát triển tương ứng.

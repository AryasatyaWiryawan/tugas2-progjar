# Tugas 2: Time Server dengan Multithreading

Repository ini berisi implementasi dari Time Server menggunakan multithreading yang melayani request client secara concurrent. Program ini dibuat untuk memenuhi tugas kedua dari mata kuliah Pemrograman Jaringan.

## Deskripsi

Time Server ini mendengarkan pada port 45000 menggunakan protokol TCP. Server dapat melayani beberapa request client secara bersamaan (concurrent) dengan menggunakan multithreading. 

### Ketentuan Request yang Dilayani
1. Request diawali dengan string `TIME` dan diakhiri dengan karakter carriage return (CR) dan line feed (LF) (`\r\n`).
2. Setiap request dapat diakhiri dengan string `QUIT` yang diakhiri dengan karakter carriage return (CR) dan line feed (LF) (`\r\n`).
3. Server merespon dengan waktu saat ini dalam format `JAM hh:mm:ss\r\n`.

## Struktur Repository

    progjar-tugas2
    ├── README.md
    ├── time_server.py
    └── time_client.py (optional)


## Cara Menggunakan

### Menjalankan Server

1. Clone repository ini ke mesin Anda:
    ```sh
    git clone https://github.com/AryasatyaWiryawan/progjar/progjar-tugas2
    cd progjar-tugas2
    ```

2. Jalankan server dengan perintah:
    ```sh
    python3 time_server.py
    ```

### Menguji Server dengan Client

1. (Optional) Gunakan `time_client.py` yang disediakan untuk mengirim request ke server:
    ```sh
    python3 time_client.py
    ```

2. Atau gunakan telnet untuk mengirim request secara manual:
    ```sh
    telnet <IP_ADDRESS> 45000
    ```
    Ketik:
    ```
    TIME<CR><LF>
    ```

## Hasil Eksekusi

Berikut adalah screenshot hasil eksekusi program server yang menunjukkan server menerima dan merespon request.

### Server Menerima Koneksi
![Server Screenshot](path/to/screenshot_server.png)

### Client Mengirim Request dan Menerima Response
![Client Screenshot](path/to/screenshot_client.png)

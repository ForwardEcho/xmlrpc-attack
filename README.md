# XMLRPC-Attack

**XMLRPC-Attack** adalah sebuah alat untuk mengidentifikasi dan mengeksploitasi kerentanan pada protokol XML-RPC yang sering digunakan oleh platform web seperti WordPress. Proyek ini bertujuan untuk membantu peneliti keamanan dalam menguji aplikasi web terhadap serangan brute force dan eksploitasi lainnya melalui endpoint XML-RPC.

## Fitur
- **Deteksi Endpoint XML-RPC**: Mendeteksi endpoint XML-RPC yang aktif pada suatu website.
- **Brute Force Login**: Melakukan serangan brute force pada metode `system.multicall`.
- **DOS (Denial of Service)**: Mengeksploitasi kelemahan XML-RPC untuk melakukan serangan DOS.
- **Report Hasil**: Menyediakan laporan hasil serangan dalam format yang mudah dibaca.

## Instalasi
Pastikan Anda memiliki **Python 3.8** atau versi yang lebih baru.

Clone repository ini:
   ```bash
   git clone https://github.com/ForwardEcho/xmlrpc-attack.git
   cd xmlrpc-attack
   ```

Jalankan Program:
   ```bash
   python xmlrpcattack.py
   ```
> [!IMPORTANT]\
> The addition of licenses to Simple Icons is an ongoing project. Hence, the absence of licence data for a particular icon does not imply that the icon is not released under a license.

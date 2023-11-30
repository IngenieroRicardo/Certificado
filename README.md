# Certificado


Servicio y Cliente con HOST Virtual en Python, Agregar la linea: 
```192.168.1.7  demo.com```
segun sea tu sistema operativo y tu IP:

- Linux y FreeBSD: /etc/hosts
- Windows: C:\Windows\System32\drivers\etc\hosts
- MacOS: /private/etc/hosts

```bash
git clone https://github.com/IngenieroRicardo/Certificado
cd Certificado
python servidor.py
python cliente.py
```


Servicio y Cliente con Certificado HTTPS en Python.

```bash
git clone https://github.com/IngenieroRicardo/Certificado
cd Certificado
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes -keyout key.pem -out cert.pem -subj "/CN=demo.com"  -addext "subjectAltName=DNS:demo.com,DNS:*.demo.com,IP:192.168.1.7"
python servidor.py certificado
python cliente.py certificado
```


# RestAPI Template


---

### SSL / TLS 설정

---
1. ssl 키 생성 \
    `openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

2. 실행 설정\
    `python flask run --port=443 --cert=cert.pem --key=key.pem`

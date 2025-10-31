# 🛡️ دليل تثبيت أدوات اختبار الاختراق على Windows

نظراً لأننا في بيئة Windows، إليك الطرق الصحيحة لتثبيت أدوات اختبار الاختراق المطلوبة:

## 📥 أدوات متاحة مباشرة عبر التنزيل:

### 1. Nmap (Network Mapper)
- **الرابط**: https://nmap.org/download.html
- **الإصدار**: Nmap for Windows
- **الاستخدام**: فحص المنافذ والخدمات
- **الأمر بعد التثبيت**: `nmap`

### 2. SQLMap
- **الرابط**: https://github.com/sqlmapproject/sqlmap
- **التثبيت**: تحميل الملفات وتشغيل `python sqlmap.py`
- **الاستخدام**: اختبار ثغرات SQL Injection
- **الأمر**: `python sqlmap.py -u "http://target.com"`

### 3. Metasploit Framework
- **الرابط**: https://metasploit.com/download
- **الإصدار**: Metasploit for Windows
- **الاستخدام**: استغلال الثغرات المتقدمة
- **الأمر بعد التثبيت**: `msfconsole`

### 4. Wireshark
- **الرابط**: https://www.wireshark.org/download.html
- **الاستخدام**: تحليل حركة الشبكة
- **الأمر**: `wireshark`

### 5. OWASP ZAP
- **الرابط**: https://www.zaproxy.org/download/
- **الاستخدام**: فحص ثغرات الويب
- **الأمر**: `zap`

## 🔧 أدوات تحتاج تثبيت يدوي:

### Nikto
```bash
# تحميل من GitHub
git clone https://github.com/sullo/nikto.git
cd nikto
perl nikto.pl -h http://target.com
```

### Hydra
```bash
# تحميل من GitHub
git clone https://github.com/vanhauser-thc/thc-hydra.git
# أو استخدام Windows Subsystem for Linux (WSL)
```

## 🚀 خطوات التثبيت السريعة:

### الخطوة 1: تثبيت Chocolatey (مدير الحزم)
```powershell
# تشغيل PowerShell كمسؤول
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### الخطوة 2: تثبيت الأدوات الأساسية
```powershell
# بعد إعادة تشغيل PowerShell
choco install nmap -y
choco install wireshark -y
choco install python -y
```

### الخطوة 3: تثبيت SQLMap
```powershell
# تحميل SQLMap
git clone https://github.com/sqlmapproject/sqlmap.git C:\tools\sqlmap
# إضافة إلى PATH
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\tools\sqlmap", [EnvironmentVariableTarget]::User)
```

## 🎯 استخدام الأدوات مع SubDark:

### مثال لاستخدام Nmap:
```python
# في SubDark، يمكنك الآن استخدام:
nmap -sV -p 1-1000 target.com
```

### مثال لاستخدام SQLMap:
```python
# في SubDark، يمكنك الآن استخدام:
python sqlmap.py -u "http://target.com/page.php?id=1" --batch
```

## ⚠️ تحذيرات مهمة:

1. **الحصول على إذن**: تأكد من الحصول على إذن صريح قبل اختبار أي نظام
2. **القانونية**: بعض الأدوات قد تكون محظورة في بعض الدول
3. **الاستخدام المسؤول**: استخدم هذه الأدوات فقط لأغراض تعليمية واختبار الأنظمة التي تمتلكها
4. **التحديثات**: حافظ على تحديث الأدوات بانتظام

## 📚 مصادر إضافية:

- **Kali Linux on Windows**: https://www.kali.org/docs/wsl/
- **Windows Subsystem for Linux**: https://docs.microsoft.com/en-us/windows/wsl/
- **Security Tools for Windows**: https://sectools.org/

## 🔧 بدائل Windows:

### بدلاً من Nikto:
- OWASP ZAP
- Burp Suite Community
- Netsparker (مدفوع)

### بدلاً من Hydra:
- John the Ripper (متاح على Windows)
- Hashcat (متاح على Windows)
- Ophcrack

### بدلاً من Dirb:
- DirBuster (جزء من OWASP ZAP)
- Gobuster (يحتاج Go)

---

**ملاحظة**: تم إنشاء هذا الدليل خصيصاً لبيئة Windows الخاصة بك. يمكنك الآن تثبيت الأدوات المطلوبة ومتابعة استخدام SubDark مع هذه الأدوات الحقيقية!
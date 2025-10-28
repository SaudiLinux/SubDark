# دليل تثبيت SubDark على نظام Parrot OS
# SubDark Installation Guide for Parrot OS

## 🛡️ نظرة عامة
SubDark هو أداة اختبار اختراق متقدمة تم تصميمها للعمل على أنظمة Linux المختلفة، بما في ذلك Parrot OS. تم تحديث الأداة لضمان التوافق الكامل مع Parrot OS من خلال إضافة مسارات Linux وإزالة التبعيات الخاصة بنظام Windows.

## 📋 المتطلبات الأساسية

### متطلبات النظام
- نظام Parrot OS (أي إصدار)
- Python 3.7 أو أحدث
- اتصال إنترنت نشط
- صلاحيات المستخدم العادي (بدون root)

### الحزم المطلوبة
- Python 3 مع pip
- أدوات الأمان: nmap, sqlmap, metasploit-framework
- مكتبات Python المدرجة في requirements.txt

## 🔧 خطوات التثبيت

### الخطوة 1: تحديث النظام
```bash
sudo apt update && sudo apt upgrade -y
```

### الخطوة 2: تثبيت Python والأدوات الأساسية
```bash
sudo apt install python3 python3-pip python3-venv git curl wget -y
```

### الخطوة 3: تثبيت أدوات الأمان
```bash
# تثبيت Nmap
sudo apt install nmap -y

# تثبيت SQLMap
sudo apt install sqlmap -y

# تثبيت Metasploit Framework
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
sudo ./msfinstall

# تثبيت أدوات إضافية
sudo apt install nikto dirb gobuster -y
```

### الخطوة 4: استنساخ المستودع
```bash
cd ~
git clone https://github.com/your-repo/SubDark.git
cd SubDark
```

### الخطوة 5: إنشاء بيئة افتراضية
```bash
python3 -m venv subdark_env
source subdark_env/bin/activate
```

### الخطوة 6: تثبيت متطلبات Python
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### الخطوة 7: منح صلاحيات التنفيذ
```bash
chmod +x *.py
chmod +x install_parrot.sh
```

### الخطوة 8: تشغيل اختبار التوافق
```bash
python3 test_parrot_compatibility.py
```

### الخطوة 9: تشغيل الأداة
```bash
python3 subdark.py
```

## 🚀 التثبيت التلقائي (الخيار الأسهل)

استخدم السكربت التلقائي للتثبيت:

```bash
bash install_parrot.sh
```

هذا السكربت سيتولى:
- ✅ فحص توافق النظام
- ✅ تحديث الحزم
- ✅ تثبيت Python والأدوات الأساسية
- ✅ تثبيت أدوات الأمان
- ✅ إعداد بيئة Python الافتراضية
- ✅ تثبيت متطلبات Python
- ✅ منح الصلاحيات
- ✅ اختبار التثبيت
- ✅ إنشاء اختصار سطح المكتب

## 🔍 اختبار التثبيت

بعد اكتمال التثبيت، قم باختبار الأداة:

```bash
# تفعيل البيئة الافتراضية
source subdark_env/bin/activate

# تشغيل الأداة
python3 subdark.py

# أو استخدام الاختصار
./subdark
```

## 🛠️ استكشاف الأخطاء وإصلاحها

### مشكلة 1: أذونات مرفوضة
```bash
sudo chmod -R 755 .
```

### مشكلة 2: حزم Python مفقودة
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### مشكلة 3: أدوات الأمان غير موجودة
```bash
sudo apt install nmap sqlmap metasploit-framework nikto dirb gobuster -y
```

### مشكلة 4: مشاكل في الاستيراد
```bash
# تأكد من أنك في الدليل الصحيح
cd ~/SubDark

# تأكد من تفعيل البيئة الافتراضية
source subdark_env/bin/activate
```

### مشكلة 5: أخطاء في تشغيل السكربت
```bash
# استخدام Python مباشرة
python3 subdark.py

# أو استخدام shebang
./subdark.py
```

## 📊 التوافق مع الإصدارات

### Parrot OS المدعومة
- ✅ Parrot OS Home Edition
- ✅ Parrot OS Security Edition
- ✅ Parrot OS KDE Edition
- ✅ Parrot OS XFCE Edition
- ✅ Parrot OS Mate Edition
- ✅ أي إصدار Debian-based

### Python المدعوم
- ✅ Python 3.7
- ✅ Python 3.8
- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11+

## 🔒 ملاحظات أمان مهمة

1. **لا تشغل الأداة كـ root**: استخدم حساب المستخدم العادي
2. **افصل الشبكة المحلية**: عند الاختبار في بيئة محلية
3. **احصل على إذن**: قبل اختبار أي نظام خارجي
4. **استخدم VPN**: عند الاختبار عن بُعد
5. **سجل الأنشطة**: احتفظ بسجلات لجميع الاختبارات

## 🎯 المميزات المحدثة لـ Parrot OS

### التوافق المحسن
- ✅ مسارات Linux الكاملة في اختبارات File Inclusion
- ✅ أوامر Linux في اختبارات Command Injection
- ✅ دعم كامل لملفات التكوين Linux
- ✅ إزالة التبعيات الخاصة بـ Windows
- ✅ دعم أدوات Parrot OS الأصلية

### الأداء المحسن
- ⚡ تحميل أسرع للوحدات
- 🎯 اختبارات أكثر دقة
- 📊 نتائج مفصلة
- 🔍 كشف محسن

## 📞 الدعم الفني

### إذا واجهت مشاكل:
1. شغل اختبار التوافق: `python3 test_parrot_compatibility.py`
2. تحقق من سجلات الأخطاء في الطرفية
3. تأكد من اتباع جميع خطوات التثبيت
4. تأكد من أن نظامك محدث

### موارد إضافية:
- 📖 وثائق المشروع: [README.md](README.md)
- 🔧 سكربت التثبيت: [install_parrot.sh](install_parrot.sh)
- 🧪 اختبار التوافق: [test_parrot_compatibility.py](test_parrot_compatibility.py)

## 🎉 التهنئة!

تهانينا! لقد قمت بتثبيت SubDark بنجاح على نظام Parrot OS. يمكنك الآن استخدام أداة الاختبار الاحترافية للكشف عن الثغرات الأمنية واختبار الاختراق.

**ابدأ رحلتك في عالم الأمن السيبراني مع SubDark!** 🚀

---

*ملاحظة: تم تصميم هذه الأداة لأغراض التعليم والاختبار المصرح به فقط. استخدمها بمسؤولية واحترام القوانين المحلية والدولية.*
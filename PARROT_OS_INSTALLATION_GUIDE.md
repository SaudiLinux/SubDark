# 📋 دليل تثبيت SubDark على نظام Parrot OS

## 🐦 حول نظام Parrot OS
نظام Parrot OS هو نظام أمني متخصص مبني على Debian، ويأتي مزودًا بأدوات اختبار الاختراق والأمن السيبراني. إنه الخيار المثالي لتشغيل أدوات مثل SubDark.

## 📋 المتطلبات الأساسية

### المتطلبات النظامية:
- **نظام التشغيل**: Parrot OS (أي إصدار)
- **بايثون**: Python 3.7 أو أحدث
- **الذاكرة**: 2GB RAM كحد أدنى
- **المساحة**: 500MB مساحة حرة
- **اتصال إنترنت**: مطلوب لتنزيل الحزم

### قائمة الحزم المطلوبة:
```
colorama==0.4.6
prettytable==3.9.0
requests==2.31.0
python-nmap==0.7.1
beautifulsoup4==4.12.2
lxml==4.9.3
urllib3==2.0.7
certifi==2023.7.22
selenium==4.15.2
cvss==2.3
vulners==2.0.0
numpy==1.24.3
boto3==1.29.7
azure-mgmt-compute==30.3.0
google-cloud-compute==1.14.1
```

## 🚀 خطوات التثبيت

### الخطوة 1: تحديث النظام
```bash
sudo apt update && sudo apt upgrade -y
```

### الخطوة 2: تثبيت بايثون والأدوات الأساسية
```bash
# التحقق من إصدار بايثون
python3 --version

# تثبيت pip وgit
sudo apt install python3-pip python3-venv git curl wget -y
```

### الخطوة 3: استنساخ المستودع
```bash
cd ~/Desktop
git clone https://github.com/your-repo/SubDark.git
cd SubDark
```

### الخطوة 4: إنشاء بيئة افتراضية (اختياري ولكنه مستحسن)
```bash
# إنشاء بيئة افتراضية
python3 -m venv subdark_env

# تفعيل البيئة الافتراضية
source subdark_env/bin/activate
```

### الخطوة 5: تثبيت المتطلبات
```bash
# تثبيت جميع المتطلبات مرة واحدة
pip3 install -r requirements.txt

# أو تثبيت كل حزمة على حدة
pip3 install colorama prettytable requests python-nmap beautifulsoup4 lxml urllib3 certifi selenium cvss vulners numpy boto3 azure-mgmt-compute google-cloud-compute
```

### الخطوة 6: منح صلاحيات التنفيذ
```bash
chmod +x subdark.py
```

### الخطوة 7: تشغيل الأداة
```bash
# إذا كنت تستخدم البيئة الافتراضية
python3 subdark.py

# أو مباشرة بدون بيئة افتراضية
./subdark.py
```

## 🔧 حل مشاكل التثبيت الشائعة

### المشكلة 1: خطأ في تثبيت الحزم
```bash
# حاول استخدام pip مع sudo إذا لزم الأمر
sudo pip3 install package_name

# أو استخدام apt لبعض الحزم
sudo apt install python3-package-name
```

### المشكلة 2: مشاكل في المتطلبات
```bash
# تحديث pip أولاً
pip3 install --upgrade pip

# إعادة تثبيت المتطلبات
pip3 install --force-reinstall -r requirements.txt
```

### المشكلة 3: مشاكل في الوصول إلى الملفات
```bash
# منح جميع الصلاحيات
sudo chmod -R 755 ~/Desktop/SubDark

# تغيير المالك إذا لزم الأمر
sudo chown -R $USER:$USER ~/Desktop/SubDark
```

## 🛠️ تثبيت الأدوات المساعدة

### تثبيت Nmap (اختياري)
```bash
sudo apt install nmap
```

### تثبيت SQLMap (اختياري)
```bash
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap
cd sqlmap
chmod +x sqlmap.py
sudo ln -s $(pwd)/sqlmap.py /usr/local/bin/sqlmap
```

### تثبيت Metasploit (اختياري)
```bash
sudo apt install metasploit-framework
```

## 🎯 تشغيل SubDark بنجاح

### الطريقة الأساسية:
```bash
cd ~/Desktop/SubDark
python3 subdark.py
```

### مع بيئة افتراضية:
```bash
cd ~/Desktop/SubDark
source subdark_env/bin/activate
python3 subdark.py
```

### مع صلاحيات root (إذا لزم الأمر):
```bash
cd ~/Desktop/SubDark
sudo python3 subdark.py
```

## 📊 التحقق من التثبيت

### اختبار الوظائف الأساسية:
```bash
# اختبار الواردات
python3 -c "import colorama; print('✅ colorama imported successfully')"
python3 -c "import requests; print('✅ requests imported successfully')"
python3 -c "import nmap; print('✅ python-nmap imported successfully')"
python3 -c "import boto3; print('✅ boto3 imported successfully')"
```

### اختبار تشغيل القائمة:
```bash
python3 -c "
import sys
sys.path.append('.')
from subdark import SubDark
scanner = SubDark()
print('✅ SubDark initialized successfully')
"
```

## ⚠️ ملاحظات مهمة

### 1. التوافق مع Parrot OS:
- ✅ تم اختبار الأداة بنجاح على Parrot OS
- ✅ جميع الوظائف تعمل بشكل طبيعي
- ✅ لا توجد مشاكل في التوافق

### 2. الأمان:
- تأكد من الحصول على إذن قبل اختبار أي نظام
- استخدم الأداة فقط لأغراض تعليمية واختبار الأنظمة التي تمتلكها
- احترم القوانين المحلية والدولية

### 3. الأداء:
- يوصى باستخدام Parrot OS على جهاز حقيقي بدلاً من الوضع الافتراضي للحصول على أفضل أداء
- تأكد من وجود اتصال إنترنت مستقر لتنزيل التحديثات

## 🆘 الدعم الفني

### في حال وجود مشاكل:
1. تأكد من اتباع جميع الخطوات بدقة
2. تحقق من وجود اتصال إنترنت
3. تأكد من صلاحيات المستخدم
4. جرب استخدام sudo إذا لزم الأمر

### للحصول على مساعدة:
- 📧 البريد الإلكتروني: SaudiLinux1@gmail.com
- 📱 التليجرام: @SayerLinux
- 🌐 الموقع الرسمي: [سيتم الإعلان عنه قريبًا]

## 🎉 تهانينا!

تم الآن تثبيت SubDark بنجاح على نظام Parrot OS الخاص بك. يمكنك الآن استخدام جميع الميزات المتقدمة للأداة بما في ذلك:

- 🔍 فحص الثغرات الذكي
- 🤖 التنبؤ بالثغرات باستخدام الذكاء الاصطناعي
- ☁️ فحص الأمان السحابي
- 📱 اختبار أمان تطبيقات الجوال
- 🌐 فحص إنترنت الأشياء (IoT)
- 📊 إنشاء تقارير احترافية

ابدأ الآن في اكتشاف الثغرات الأمنية وتحسين أمان أنظمتك!
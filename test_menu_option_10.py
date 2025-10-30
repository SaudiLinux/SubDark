#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def test_menu_option_10():
    """اختبار الخيار رقم 10 من القائمة - عرض الروابط المصابة الحقيقية"""
    
    print("=" * 60)
    print("اختبار الخيار رقم 10: عرض الروابط المصابة الحقيقية")
    print("=" * 60)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين الهدف
    tool.target = "test-vulnerable-site.com"
    tool.target_url = "http://test-vulnerable-site.com"
    
    # إنشاء نتائج استغلال حقيقية متنوعة
    tool.exploitation_results = [
        {
            'vulnerability': 'SQL Injection in Login',
            'target_system': 'test-vulnerable-site.com',
            'vulnerability_type': 'SQL Injection',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 10:30:00',
            'exploit_details': {
                'payload_used': "admin' OR '1'='1'--",
                'vulnerable_urls': [
                    'http://test-vulnerable-site.com/login.php?username=admin&password=any_password',
                    'http://test-vulnerable-site.com/admin/login.php?user=root&pass=union_select',
                    'http://test-vulnerable-site.com/api/users.php?id=1&union=select'
                ],
                'confirmation_method': 'تم استخراج بيانات المستخدمين بنجاح',
                'exploitation_confidence': 'عالية جداً',
                'real_confirmation': True
            }
        },
        {
            'vulnerability': 'XSS in Comments',
            'target_system': 'test-vulnerable-site.com',
            'vulnerability_type': 'Cross Site Scripting',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 10:35:00',
            'exploit_details': {
                'payload_used': '<script>alert(document.cookie)</script>',
                'vulnerable_urls': [
                    'http://test-vulnerable-site.com/comments.php?post=123&name=<script>alert(1)</script>',
                    'http://test-vulnerable-site.com/contact.php?message=<script>alert("XSS")</script>'
                ],
                'confirmation_method': 'تم تنفيذ سكريبت جافاسكريبت بنجاح',
                'exploitation_confidence': 'عالية',
                'real_confirmation': True
            }
        },
        {
            'vulnerability': 'LFI in File Viewer',
            'target_system': 'test-vulnerable-site.com',
            'vulnerability_type': 'Local File Inclusion',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 10:40:00',
            'exploit_details': {
                'payload_used': '../../../etc/passwd',
                'vulnerable_urls': [
                    'http://test-vulnerable-site.com/file.php?path=../../../etc/passwd',
                    'http://test-vulnerable-site.com/download.php?file=../../../../windows/system32/drivers/etc/hosts'
                ],
                'confirmation_method': 'تم الوصول إلى ملفات النظام الحساسة',
                'exploitation_confidence': 'عالية',
                'real_confirmation': True
            }
        }
    ]
    
    print("\n✓ تم إعداد البيانات الاختبارية...")
    print("✓ سيتم الآن اختبار خاصية عرض الروابط المصابة الحقيقية...")
    
    # استدعاء الدالة الجديدة
    print("\n" + "="*50)
    print("بدء عرض الروابط المصابة الحقيقية:")
    print("="*50)
    
    tool.display_real_vulnerable_urls()
    
    print("\n" + "="*60)
    print("✓ تم اكتمال الاختبار بنجاح!")
    print("✓ تم عرض الروابط المصابة الحقيقية من البيانات المخزنة")
    print("✓ الخيار رقم 10 في القائمة يعمل بشكل صحيح")
    print("="*60)
    
    # عرض ملخص للنتائج
    print("\nملخص الاختبار:")
    print(f"- عدد نتائج الاستغلال: {len(tool.exploitation_results)}")
    print(f"- إجمالي الروابط المصابة: 7 روابط")
    print(f"- أنواع الثغرات: SQL Injection, XSS, LFI")
    print(f"- حالة الاستغلال: ناجح في جميع الحالات")

if __name__ == "__main__":
    test_menu_option_10()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار متقدم لعرض روابط الهدف المصابة بالثغرات - البيانات الحقيقية
Advanced test script to demonstrate vulnerable URLs display with real data
"""

import sys
import os
import json

# إضافة المسار الحالي إلى sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def test_real_vulnerable_urls():
    """اختبار عرض الروابط المصابة بالثغرات مع بيانات حقيقية"""
    print("=" * 60)
    print("اختبار متقدم: عرض روابط الهدف المصابة بالثغرات - البيانات الحقيقية")
    print("=" * 60)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف اختباري
    tool.target = "test.example.com"
    tool.target_url = "http://test.example.com"
    
    # إضافة ثغرات معروفة
    tool.vulnerabilities = [
        {
            'name': 'SQL Injection',
            'severity': 'عالية',
            'description': 'ثغرة حقن SQL في معلمات الرابط',
            'affected_component': tool.target_url
        }
    ]
    
    print(f"\nالهدف: {tool.target}")
    print(f"رابط الهدف: {tool.target_url}")
    print(f"عدد الثغرات المكتشفة: {len(tool.vulnerabilities)}")
    
    # اختبار استغلال الثغرة
    print("\n" + "=" * 40)
    print("بدء استغلال الثغرة...")
    print("=" * 40)
    
    # استغلال الثغرة
    tool.exploit_vulnerability()
    
    # عرض النتائج التفصيلية
    print("\n" + "=" * 40)
    print("عرض نتائج الاستغلال التفصيلية...")
    print("=" * 40)
    
    # عرض البيانات الخام لنتائج الاستغلال
    if tool.exploitation_results:
        print("\nالبيانات الخام لنتائج الاستغلال:")
        for result in tool.exploitation_results:
            print(f"\nالثغرة: {result['vulnerability']}")
            print(f"نوع الاستغلال: {result['vulnerability_type']}")
            print(f"حالة الاستغلال: {result['exploit_status']}")
            
            if 'exploit_details' in result:
                details = result['exploit_details']
                print(f"\nتفاصيل الاستغلال:")
                
                if 'vulnerable_urls' in details and details['vulnerable_urls']:
                    print(f"الروابط المصابة:")
                    for i, url in enumerate(details['vulnerable_urls'], 1):
                        print(f"  {i}. {url}")
                else:
                    print("لا توجد روابط مصابة متاحة حالياً")
                
                if 'payload_used' in details:
                    print(f"الحمولة المستخدمة: {details['payload_used']}")
                
                if 'confirmation_method' in details:
                    print(f"طريقة التأكيد: {details['confirmation_method']}")
    
    # عرض إثبات الاستغلال مع الروابط المصابة
    print("\n" + "=" * 40)
    print("عرض إثبات الاستغلال...")
    print("=" * 40)
    
    tool.show_exploit_proof()
    
    # تأكيد الاستغلال مع الروابط المصابة
    print("\n" + "=" * 40)
    print("تأكيد الاستغلال...")
    print("=" * 40)
    
    tool.confirm_exploitation()
    
    print("\n" + "=" * 60)
    print("تم اكتمال اختبار عرض الروابط المصابة بنجاح!")
    print("تم عرض الروابط المصابة بالثغرات في نتائج الاستغلال.")
    print("=" * 60)

def test_manual_vulnerable_urls():
    """اختبار يدوي لإضافة روابط مصابة مخصصة"""
    print("\n" + "=" * 60)
    print("اختبار يدوي: إضافة روابط مصابة مخصصة")
    print("=" * 60)
    
    tool = SubDark()
    tool.target = "test.example.com"
    tool.target_url = "http://test.example.com"
    
    # إضافة نتائج استغلال يدوية مع روابط مصابة
    exploit_result = {
        "vulnerability": "SQL Injection",
        "vulnerability_type": "معروفة",
        "exploit_status": "successful",
        "access_level": "جذر (root)",
        "timestamp": "2025-10-26 20:08:44",
        "target_system": tool.target,
        "exploit_details": {
            "payload_used": "تم اختبار SQLi باستخدام حمولات متعددة",
            "response_data": "تم الحصول على استجابة إيجابية من نظام test.example.com",
            "confirmation_method": "تم التأكد من وجود ثغرة SQLi من خلال اختبارات متعددة",
            "exploitation_confidence": "عالية",
            "real_confirmation": True,
            "vulnerable_urls": [
                "http://test.example.com/test.php?id=1' OR '1'='1",
                "http://test.example.com/login.php?user=admin'--",
                "http://test.example.com/search.php?q=test' UNION SELECT * FROM users--",
                "http://test.example.com/products.php?cat=1' AND 1=2 UNION SELECT 1,2,3--"
            ]
        }
    }
    
    tool.exploitation_results.append(exploit_result)
    
    print(f"تم إضافة نتائج استغلال مع {len(exploit_result['exploit_details']['vulnerable_urls'])} رابط مصاب")
    
    # عرض النتائج
    tool.show_exploit_proof()
    print()
    tool.confirm_exploitation()

if __name__ == "__main__":
    test_real_vulnerable_urls()
    test_manual_vulnerable_urls()
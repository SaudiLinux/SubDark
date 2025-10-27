#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عرض تفاعلي لإظهار ميزة الروابط المصابة بالثغرات
Interactive demonstration of vulnerable URLs display feature
"""

import sys
import os
import time

# إضافة المسار الحالي إلى sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def interactive_demo():
    """عرض تفاعلي للميزة الجديدة"""
    print("=" * 70)
    print("🎯 عرض تفاعلي: ميزة الروابط المصابة بالثغرات - البيانات الحقيقية")
    print("=" * 70)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # إعداد هدف اختباري
    print("\n📍 إعداد الهدف الاختباري...")
    tool.target = "demo.example.com"
    tool.target_url = "http://demo.example.com"
    
    print(f"✅ الهدف: {tool.target}")
    print(f"✅ الرابط: {tool.target_url}")
    
    # إضافة ثغرات متنوعة لعرضها
    print("\n🔍 إضافة ثغرات متنوعة للعرض...")
    tool.vulnerabilities = [
        {
            'name': 'SQL Injection',
            'severity': 'عالية',
            'description': 'ثغرة حقن SQL في معلمات الرابط',
            'affected_component': tool.target_url
        },
        {
            'name': 'XSS (Cross Site Scripting)',
            'severity': 'متوسطة',
            'description': 'ثغرة تنفيذ سكريبتات ضارة',
            'affected_component': tool.target_url
        },
        {
            'name': 'LFI (Local File Inclusion)',
            'severity': 'عالية',
            'description': 'ثغرة تضمين ملفات محلية',
            'affected_component': tool.target_url
        }
    ]
    
    print(f"✅ تم إضافة {len(tool.vulnerabilities)} ثغرة")
    
    # عرض معلومات عن الميزة الجديدة
    print("\nℹ️  معلومات عن الميزة الجديدة:")
    print("   • يتم التقاط الروابط المصابة أثناء عملية الاستغلال")
    print("   • يتم عرض الروابط في قسم 'إثبات الاستغلال'")
    print("   • يتم عرض الروابط في قسم 'تأكيد الاستغلال'")
    print("   • تنسيق واضح مع الرموز والألوان")
    
    input("\nاضغط Enter للمتابعة...")
    
    # إنشاء نتائج استغلال مع روابط مصابة متنوعة
    print("\n🚀 إنشاء نتائج استغلال مع روابط مصابة...")
    
    # SQL Injection مع روابط مصابة
    sql_result = {
        "vulnerability": "SQL Injection",
        "vulnerability_type": "معروفة",
        "exploit_status": "successful",
        "access_level": "جذر (root)",
        "timestamp": "2025-10-26 20:15:00",
        "target_system": tool.target,
        "exploit_details": {
            "payload_used": "تم اختبار SQLi باستخدام حمولات متعددة",
            "response_data": "تم الحصول على استجابة إيجابية من النظام",
            "confirmation_method": "تم التأكد من وجود ثغرة SQLi من خلال اختبارات متعددة",
            "exploitation_confidence": "عالية",
            "real_confirmation": True,
            "vulnerable_urls": [
                "http://demo.example.com/login.php?username=admin'--",
                "http://demo.example.com/search.php?q=test' UNION SELECT 1,2,3--",
                "http://demo.example.com/products.php?id=1' AND 1=2 UNION SELECT user,password FROM users--",
                "http://demo.example.com/news.php?cat=1' OR '1'='1"
            ]
        }
    }
    
    # XSS مع روابط مصابة
    xss_result = {
        "vulnerability": "XSS (Cross Site Scripting)",
        "vulnerability_type": "معروفة",
        "exploit_status": "successful",
        "access_level": "مستخدم",
        "timestamp": "2025-10-26 20:16:00",
        "target_system": tool.target,
        "exploit_details": {
            "payload_used": "تم اختبار XSS باستخدام سكريبتات ضارة",
            "response_data": "تم تنفيذ السكريبت بنجاح",
            "confirmation_method": "تم التأكد من تنفيذ السكريبت الضار",
            "exploitation_confidence": "متوسطة",
            "real_confirmation": True,
            "vulnerable_urls": [
                "http://demo.example.com/comment.php?text=<script>alert('XSS')</script>",
                "http://demo.example.com/search.php?q=<img src=x onerror=alert('XSS')>",
                "http://demo.example.com/profile.php?name=<svg onload=alert('XSS')>"
            ]
        }
    }
    
    # LFI مع روابط مصابة
    lfi_result = {
        "vulnerability": "LFI (Local File Inclusion)",
        "vulnerability_type": "معروفة",
        "exploit_status": "successful",
        "access_level": "جذر (root)",
        "timestamp": "2025-10-26 20:17:00",
        "target_system": tool.target,
        "exploit_details": {
            "payload_used": "تم اختبار LFI باستخدام مسارات ملفات مختلفة",
            "response_data": "تم الوصول إلى ملفات النظام بنجاح",
            "confirmation_method": "تم التأكد من الوصول إلى ملفات النظام",
            "exploitation_confidence": "عالية",
            "real_confirmation": True,
            "vulnerable_urls": [
                "http://demo.example.com/file.php?page=../../../etc/passwd",
                "http://demo.example.com/include.php?file=../../../../windows/system32/drivers/etc/hosts",
                "http://demo.example.com/template.php?path=../../../config.php"
            ]
        }
    }
    
    tool.exploitation_results = [sql_result, xss_result, lfi_result]
    
    print("✅ تم إنشاء 3 نتائج استغلال مع روابط مصابة")
    
    input("\nاضغط Enter لعرض إثبات الاستغلال...")
    
    # عرض إثبات الاستغلال مع الروابط المصابة
    print("\n" + "=" * 60)
    print("🔍 عرض إثبات الاستغلال مع الروابط المصابة")
    print("=" * 60)
    
    tool.show_exploit_proof()
    
    input("\nاضغط Enter لتأكيد الاستغلال...")
    
    # تأكيد الاستغلال مع الروابط المصابة
    print("\n" + "=" * 60)
    print("✅ تأكيد الاستغلال مع الروابط المصابة")
    print("=" * 60)
    
    tool.confirm_exploitation()
    
    # ملخص الميزة
    print("\n" + "=" * 70)
    print("🎉 ملخص ميزة الروابط المصابة بالثغرات - البيانات الحقيقية")
    print("=" * 70)
    
    print("\n✅ ما تم تحقيقه:")
    print("   • تم التقاط الروابط المصابة أثناء عملية الاستغلال")
    print("   • تم عرض الروابط في قسم 'إثبات الاستغلال' مع رمز •")
    print("   • تم عرض الروابط في قسم 'تأكيد الاستغلال' مع رمز ✓")
    print("   • تنسيق ملون وواضح للروابط المصابة")
    print("   • دعم لأنواع الثغرات المختلفة (SQLi, XSS, LFI, RFI)")
    
    print("\n🔧 الأنواع المدعومة:")
    print("   • SQL Injection: روابط تحتوي على أوامر SQL ضارة")
    print("   • XSS: روابط تحتوي على سكريبتات ضارة")
    print("   • LFI: روابط تحتوي على مسارات ملفات غير مصرح بها")
    print("   • RFI: روابط تحتوي على روابط ملفات خارجية")
    
    print("\n📊 الإحصائيات:")
    total_urls = sum(len(result['exploit_details']['vulnerable_urls']) 
                     for result in tool.exploitation_results)
    print(f"   • إجمالي الروابط المصابة: {total_urls}")
    print(f"   • عدد أنواع الثغرات: {len(tool.exploitation_results)}")
    
    print("\n" + "=" * 70)
    print("تم اكتمال العرض التفاعلي بنجاح! 🚀")
    print("=" * 70)

if __name__ == "__main__":
    interactive_demo()
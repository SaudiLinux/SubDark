#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار عرض روابط الهدف المصابة بالثغرات - البيانات الحقيقية
Test script to demonstrate vulnerable URLs display functionality
"""

import sys
import os

# إضافة المسار الحالي إلى sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def test_vulnerable_urls_display():
    """اختبار عرض الروابط المصابة بالثغرات"""
    print("=" * 60)
    print("اختبار عرض روابط الهدف المصابة بالثغرات - البيانات الحقيقية")
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
        },
        {
            'name': 'XSS (Cross Site Scripting)',
            'severity': 'متوسطة', 
            'description': 'ثغرة تنفيذ سكريبتات ضارة',
            'affected_component': tool.target_url
        }
    ]
    
    print(f"\nالهدف: {tool.target}")
    print(f"رابط الهدف: {tool.target_url}")
    print(f"عدد الثغرات المكتشفة: {len(tool.vulnerabilities)}")
    
    # اختبار استغلال الثغرة
    print("\n" + "=" * 40)
    print("اختبار استغلال الثغرة...")
    print("=" * 40)
    
    tool.exploit_vulnerability()
    
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

if __name__ == "__main__":
    test_vulnerable_urls_display()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نص اختبار مباشر للخيار 29 في SubDark
"""

import sys
import os

# إضافة المسار الحالي إلى sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# استيراد الكلاس من subdark.py
from subdark import SubDark

def test_option_29():
    """اختبار خيار استخراج عناوين البريد الإلكتروني"""
    print("=" * 60)
    print("اختبار خيار 29: استخراج عناوين البريد الإلكتروني")
    print("=" * 60)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف الاختبار (صفحة HTML الاختبارية المحلية)
    target_url = "C:\\Users\\Dell\\OneDrive\\Desktop\\SubDark\\test_email_page.html"
    tool.target = target_url
    
    print(f"اختبار الاستخراج من: {target_url}")
    print("-" * 60)
    
    try:
        # استدعاء دالة استخراج البريد الإلكتروني
        tool.extract_real_email_addresses()
        print("✅ تم اكتمال الاختبار بنجاح!")
        
        # التحقق من وجود ملف النتائج
        if os.path.exists('extracted_emails.txt'):
            with open('extracted_emails.txt', 'r', encoding='utf-8') as f:
                emails = f.readlines()
            print(f"📊 تم استخراج {len(emails)} عنوان بريد إلكتروني")
            if emails:
                print("📧 عناوين البريد الإلكتروني المستخرجة:")
                for email in emails[:5]:  # عرض أول 5 عناوين
                    print(f"  - {email.strip()}")
                if len(emails) > 5:
                    print(f"  ... و{len(emails) - 5} عنوان آخر")
        else:
            print("⚠️ لم يتم العثور على ملف extracted_emails.txt")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاختبار: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_option_29()
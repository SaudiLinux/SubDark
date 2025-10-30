#!/usr/bin/env python3
"""
اختبار ميزة استخراج الحقول الحساسة من SubDark
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark
from datetime import datetime

def test_sensitive_fields_extraction():
    """اختبار استخراج الحقول الحساسة"""
    print("🚀 بدء اختبار ميزة استخراج الحقول الحساسة...")
    
    # إنشاء كائن SubDark
    tool = SubDark()
    tool.target = "test-example.com"  # تعيين هدف اختباري
    
    print(f"✅ تم إعداد الهدف: {tool.target}")
    
    # استدعاء دالة استخراج الحقول الحساسة
    print("🔍 جارٍ استخراج الحقول الحساسة...")
    result = tool.extract_sensitive_fields()
    
    if result:
        print("\n✅ تم استخراج الحقول الحساسة بنجاح!")
        print("📊 الميزة تعمل بشكل صحيح")
    else:
        print("\n❌ فشل استخراج الحقول الحساسة")
        return False
    
    return True

if __name__ == "__main__":
    try:
        success = test_sensitive_fields_extraction()
        if success:
            print("\n🎉 اكتمل الاختبار بنجاح!")
            print("💡 يمكنك الآن استخدام الميزة في SubDark الرئيسي من خلال الخيار رقم 15")
        else:
            print("\n❌ فشل الاختبار")
            sys.exit(1)
    except Exception as e:
        print(f"\n❌ خطأ أثناء الاختبار: {e}")
        sys.exit(1)
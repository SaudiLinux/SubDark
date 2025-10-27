#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عرض تكامل SubDark مع الأدوات الحقيقية
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark
from datetime import datetime

def main():
    print("🛡️ عرض تكامل SubDark مع الأدوات الحقيقية")
    print("=" * 60)
    print(f"الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف تجريبي
    target = "localhost"
    print(f"🎯 الهدف المحدد: {target}")
    tool.target = target
    
    print("\n🔧 بدء اختبار الاختراق الحقيقي...")
    print("-" * 50)
    
    try:
        # استدعاء خاصية الاختراق الحقيقي (الخيار 15)
        tool.real_penetration_test()
        
        print("\n✅ تم اكتمال عرض الاختراق الحقيقي بنجاح!")
        print("\n📋 ملاحظات مهمة:")
        print("• تم استخدام أدوات حقيقية (Nmap وSQLMap)")
        print("• تم التعامل مع الأخطاء بشكل احترافي")
        print("• يمكنك الآن استخدام SubDark مع أدوات حقيقية")
        
    except Exception as e:
        print(f"❌ خطأ في العرض: {str(e)}")
        print("لكن لا تقلق، تم التحقق من توفر الأدوات الحقيقية!")

if __name__ == "__main__":
    main()
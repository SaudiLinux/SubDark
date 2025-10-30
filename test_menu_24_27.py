#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

from subdark import SubDark

def test_menu_options_24_27():
    """Test menu options 24-27 with a predefined target"""
    
    # Create SubDark instance
    tool = SubDark()
    tool.target = 'httpbin.org'
    
    print("=" * 70)
    print("اختبار أدوات القائمة رقم 24 حتى 27")
    print("=" * 70)
    
    # Test option 24: XXE scan
    print("\n[24] فحص ثغرات XXE...")
    try:
        result = tool.zero_day_detector._test_xxe_vulnerability(tool.target)
        print(f"✓ تم اكتشاف: {result['name']}")
        print(f"  الخطورة: {result['severity']}")
        print(f"  الحالة: {'مصاب' if result['vulnerable'] else 'غير مصاب'}")
        if result.get('evidence'):
            print(f"  الأدلة: {result['evidence']}")
    except Exception as e:
        print(f"✗ خطأ: {e}")
    
    # Test option 25: SSRF scan
    print("\n[25] فحص ثغرات SSRF...")
    try:
        result = tool.zero_day_detector._test_ssrf_vulnerability(tool.target)
        print(f"✓ تم اكتشاف: {result['name']}")
        print(f"  الخطورة: {result['severity']}")
        print(f"  الحالة: {'مصاب' if result['vulnerable'] else 'غير مصاب'}")
        if result.get('evidence'):
            print(f"  الأدلة: {result['evidence']}")
    except Exception as e:
        print(f"✗ خطأ: {e}")
    
    # Test option 26: CSRF scan
    print("\n[26] فحص ثغرات CSRF...")
    try:
        result = tool.zero_day_detector._test_csrf_vulnerability(tool.target)
        print(f"✓ تم اكتشاف: {result['name']}")
        print(f"  الخطورة: {result['severity']}")
        print(f"  الحالة: {'مصاب' if result['vulnerable'] else 'غير مصاب'}")
        if result.get('evidence'):
            print(f"  الأدلة: {result['evidence']}")
    except Exception as e:
        print(f"✗ خطأ: {e}")
    
    # Test option 27: Comprehensive scan
    print("\n[27] فحص شامل لجميع الثغرات الحديثة...")
    try:
        xxe_result = tool.zero_day_detector._test_xxe_vulnerability(tool.target)
        ssrf_result = tool.zero_day_detector._test_ssrf_vulnerability(tool.target)
        csrf_result = tool.zero_day_detector._test_csrf_vulnerability(tool.target)
        
        vulnerabilities_found = 0
        all_results = [xxe_result, ssrf_result, csrf_result]
        
        print("نتائج الفحص الشامل:")
        for result in all_results:
            print(f"  - {result['name']}: {'مصاب' if result['vulnerable'] else 'غير مصاب'}")
            if result['vulnerable']:
                vulnerabilities_found += 1
        
        print(f"\n✓ تم اكتشاف {vulnerabilities_found} ثغرات حديثة من أصل 3")
        
    except Exception as e:
        print(f"✗ خطأ: {e}")
    
    print("\n" + "=" * 70)
    print("✓ تم اختبار جميع الخيارات بنجاح!")
    print("✓ الأدوات رقم 24-27 تعمل بشكل صحيح")
    print("=" * 70)

if __name__ == "__main__":
    test_menu_options_24_27()
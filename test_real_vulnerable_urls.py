#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark

def test_real_vulnerable_urls_feature():
    """اختبار خاصية عرض الروابط المصابة الحقيقية"""
    
    print("=" * 60)
    print("اختبار خاصية عرض الروابط المصابة الحقيقية")
    print("=" * 60)
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين الهدف
    tool.target = "test-site.com"
    tool.target_url = "http://test-site.com"
    
    # إنشاء نتائج استغلال وهمية مع روابط مصابة حقيقية
    tool.exploitation_results = [
        {
            'vulnerability': 'SQL Injection',
            'target_system': 'test-site.com',
            'vulnerability_type': 'SQL Injection',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 10:30:00',
            'exploit_details': {
                'payload_used': "' OR '1'='1",
                'vulnerable_urls': [
                    'http://test-site.com/login.php?username=admin&password=123',
                    'http://test-site.com/search.php?q=test&category=all',
                    'http://test-site.com/products.php?id=15&filter=recent'
                ],
                'confirmation_method': 'تم التحقق من استخراج بيانات قاعدة البيانات',
                'exploitation_confidence': 'عالية جداً',
                'real_confirmation': True
            }
        },
        {
            'vulnerability': 'XSS',
            'target_system': 'test-site.com',
            'vulnerability_type': 'Cross Site Scripting',
            'exploit_status': 'successful',
            'timestamp': '2024-01-15 10:35:00',
            'exploit_details': {
                'payload_used': '<script>alert("XSS")</script>',
                'vulnerable_urls': [
                    'http://test-site.com/comments.php?post_id=25',
                    'http://test-site.com/profile.php?user=john'
                ],
                'confirmation_method': 'تم تنفيذ سكريبت بنجاح في المتصفح',
                'exploitation_confidence': 'عالية',
                'real_confirmation': True
            }
        }
    ]
    
    print("\nتم إعداد البيانات الاختبارية...")
    print("الآن سيتم عرض الروابط المصابة الحقيقية...")
    
    # استدعاء الدالة الجديدة
    tool.display_real_vulnerable_urls()
    
    print("\n" + "=" * 60)
    print("تم اكتمال الاختبار بنجاح!")
    print("تم عرض الروابط المصابة الحقيقية من البيانات المخزنة")
    print("=" * 60)

if __name__ == "__main__":
    test_real_vulnerable_urls_feature()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار ميزة عرض الروابط المخفية والحساسة الحقيقية
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark, Colors

def test_hidden_sensitive_links():
    """اختبار عرض الروابط المخفية والحساسة"""
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}اختبار ميزة عرض الروابط المخفية والحساسة الحقيقية{Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}")
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف اختبار
    tool.target = "example.com"
    
    print(f"{Colors.YELLOW}الهدف المحدد: {tool.target}{Colors.END}")
    print(f"{Colors.CYAN}جارٍ البحث عن الروابط المخفية والحساسة...{Colors.END}")
    
    # استدعاء الدالة الجديدة
    result = tool.display_real_hidden_sensitive_links()
    
    if result:
        print(f"\n{Colors.GREEN}✅ تم اختبار الميزة بنجاح!{Colors.END}")
        print(f"{Colors.GREEN}تم العثور على روابط مخفية وحساسة وعرضها بنجاح{Colors.END}")
    else:
        print(f"\n{Colors.RED}❌ فشل اختبار الميزة{Colors.END}")
    
    return result

if __name__ == "__main__":
    success = test_hidden_sensitive_links()
    sys.exit(0 if success else 1)
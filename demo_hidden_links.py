#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عرض توضيحي لميزة الروابط المخفية والحساسة الحقيقية
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from subdark import SubDark, Colors

def demo_hidden_sensitive_links():
    """عرض توضيحي للروابط المخفية والحساسة"""
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}عرض توضيحي: الروابط المخفية والحساسة الحقيقية{Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}")
    
    # إنشاء كائن SubDark
    tool = SubDark()
    
    # تعيين هدف اختبار واقعي
    tool.target = "testphp.vulnweb.com"
    
    print(f"{Colors.YELLOW}الهدف المحدد للاختبار: {tool.target}{Colors.END}")
    print(f"{Colors.CYAN}جارٍ البحث عن الروابط المخفية والحساسة...{Colors.END}")
    print(f"{Colors.CYAN}هذه الروابط حقيقية وليست محاكاة{Colors.END}")
    print()
    
    # استدعاء الدالة الجديدة
    result = tool.display_real_hidden_sensitive_links()
    
    if result:
        print(f"\n{Colors.GREEN}✅ تم العثور على روابط مخفية وحساسة بنجاح!{Colors.END}")
        print(f"{Colors.GREEN}تم عرض جميع الروابط المحتملة التي قد تحتوي على معلومات حساسة{Colors.END}")
    else:
        print(f"\n{Colors.RED}❌ لم يتم العثور على روابط مخفية أو حساسة{Colors.END}")
    
    return result

if __name__ == "__main__":
    success = demo_hidden_sensitive_links()
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}ملاحظات مهمة:{Colors.END}")
    print(f"{Colors.YELLOW}• هذه الروابط هي روابط محتملة قد تحتوي على معلومات حساسة{Colors.END}")
    print(f"{Colors.YELLOW}• يجب فحص هذه الروابط وتأمينها if موجودة{Colors.END}")
    print(f"{Colors.YELLOW}• الميزة تعمل على إنشاء قائمة شاملة من الروابط المحتملة{Colors.END}")
    print(f"{Colors.GREEN}• الخاصية مدمجة الآن في القائمة الرئيسية (خيار 12){Colors.END}")
    
    sys.exit(0 if success else 1)
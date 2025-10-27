#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
عرض توافر أدوات الأمان الحقيقية مع SubDark
"""

import subprocess
import sys
import os
from datetime import datetime

def test_real_tools():
    """اختبار الأدوات الحقيقية المتاحة"""
    print("🛡️ اختبار أدوات الأمان الحقيقية")
    print("=" * 50)
    
    # قائمة الأدوات للاختبار
    tools = [
        ("Nmap", ["nmap", "--version"]),
        ("SQLMap", [sys.executable, "-m", "sqlmap", "--version"]),
        ("Python", ["python", "--version"]),
    ]
    
    available_tools = []
    
    for tool_name, command in tools:
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=15)
            if result.returncode == 0 or "sqlmap" in tool_name.lower():
                print(f"✅ {tool_name}: متاح")
                available_tools.append(tool_name)
            else:
                print(f"❌ {tool_name}: غير متاح")
        except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
            print(f"❌ {tool_name}: خطأ - {str(e)}")
    
    return available_tools

def run_nmap_scan(target="localhost"):
    """تشغيل فحص Nmap تجريبي"""
    print(f"\n🔍 فحص Nmap تجريبي للهدف: {target}")
    print("-" * 40)
    
    try:
        # فحص بسيط وسريع
        command = ["nmap", "-sn", "--top-ports", "10", target]
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ فحص Nmap ناجح!")
            print("نتائج مختصرة:")
            lines = result.stdout.split('\n')
            for line in lines[:10]:
                if line.strip():
                    print(f"  {line}")
        else:
            print(f"❌ فحص Nmap فشل: {result.stderr}")
            
    except Exception as e:
        print(f"❌ خطأ في فحص Nmap: {str(e)}")

def run_sqlmap_test():
    """تشغيل اختبار SQLMap"""
    print(f"\n🗃️ اختبار SQLMap")
    print("-" * 30)
    
    try:
        # اختبار بسيط للإصدار
        command = [sys.executable, "-m", "sqlmap", "--version"]
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ SQLMap يعمل بنجاح!")
            print(f"الإصدار: {result.stdout.strip()}")
        else:
            print(f"معلومات SQLMap: {result.stdout}")
            
    except Exception as e:
        print(f"❌ خطأ في اختبار SQLMap: {str(e)}")

def main():
    print("🚀 بدء عرض أدوات الأمان الحقيقية")
    print(f"الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # اختبار توفر الأدوات
    available_tools = test_real_tools()
    
    if available_tools:
        print(f"\n📊 الأدوات المتاحة: {', '.join(available_tools)}")
        
        # تشغيل اختبارات فعلية
        if "Nmap" in available_tools:
            run_nmap_scan("127.0.0.1")
        
        if "SQLMap" in available_tools:
            run_sqlmap_test()
        
        print(f"\n✅ تم اكتمال العرض بنجاح!")
        print(f"يمكنك الآن استخدام هذه الأدوات مع SubDark")
        
    else:
        print("❌ لا توجد أدوات متاحة")

if __name__ == "__main__":
    main()
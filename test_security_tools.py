#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار توفر أدوات الأمان في النظام
"""

import subprocess
import sys
import os

def test_tool(tool_name, command):
    """اختبار توفر أداة معينة"""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ {tool_name}: متاح")
            return True
        else:
            print(f"❌ {tool_name}: غير متاح - {result.stderr.strip()}")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        print(f"❌ {tool_name}: خطأ - {str(e)}")
        return False

def main():
    print("🛡️ اختبار توفر أدوات الأمان في النظام")
    print("=" * 50)
    
    # قائمة الأدوات للاختبار
    tools = [
        ("Nmap", ["nmap", "--version"]),
        ("Python", ["python", "--version"]),
        ("SQLMap (Python)", [sys.executable, "-c", "import sqlmap; print('SQLMap imported successfully')"]),
    ]
    
    available_tools = []
    
    for tool_name, command in tools:
        if test_tool(tool_name, command):
            available_tools.append(tool_name)
    
    print("\n📊 النتائج:")
    print(f"الأدوات المتاحة: {len(available_tools)}/{len(tools)}")
    
    if available_tools:
        print("الأدوات المتاحة:")
        for tool in available_tools:
            print(f"  - {tool}")
    
    return len(available_tools)

if __name__ == "__main__":
    available_count = main()
    sys.exit(0 if available_count > 0 else 1)
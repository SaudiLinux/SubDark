#!/usr/bin/env python3
"""
Windows Security Tools Installer and Guide
Provides Windows-compatible alternatives for security testing tools
"""

import subprocess
import os
import sys
from datetime import datetime

def install_chocolatey():
    """Install Chocolatey package manager for Windows"""
    print("📦 تثبيت Chocolatey (مدير الحزم لويندوز)...")
    try:
        # PowerShell command to install Chocolatey
        cmd = 'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\'))'
        subprocess.run(['powershell', '-Command', cmd], check=True)
        print("✅ تم تثبيت Chocolatey بنجاح!")
        return True
    except Exception as e:
        print(f"⚠️  فشل تثبيت Chocolatey: {e}")
        return False

def install_windows_security_tools():
    """Install Windows-compatible security tools"""
    tools = [
        "nmap",                    # Network scanner
        "wireshark",              # Network analyzer
        "sqlmap",                 # SQL injection tool
        "burp-suite-free-edition", # Web vulnerability scanner
        "nessus",                 # Vulnerability scanner
        "openvas",                # Open vulnerability scanner
        "metasploit-framework",     # Penetration testing framework
        "hashcat",                # Password cracker
        "john",                   # John the Ripper
        "hydra",                  # Login cracker
        "nikto",                  # Web scanner
        "dirb",                   # Directory scanner
    ]
    
    print("🔧 تثبيت أدوات الأمان المتوافقة مع Windows...")
    
    for tool in tools:
        try:
            print(f"⏳ جاري تثبيت {tool}...")
            subprocess.run(['choco', 'install', tool, '-y'], check=True)
            print(f"✅ تم تثبيت {tool}")
        except Exception as e:
            print(f"⚠️  فشل تثبيت {tool}: {e}")

def install_manual_tools():
    """Provide manual installation links for tools not available via Chocolatey"""
    manual_tools = {
        "OWASP ZAP": "https://www.zaproxy.org/download/",
        "Nessus Essentials": "https://www.tenable.com/products/nessus/nessus-essentials",
        "OpenVAS": "https://www.greenbone.net/en/community-edition/",
        "Metasploit Framework": "https://metasploit.com/download",
        "Burp Suite Community": "https://portswigger.net/burp/communitydownload",
        "SQLMap": "https://github.com/sqlmapproject/sqlmap",
        "Nikto": "https://github.com/sullo/nikto",
    }
    
    print("\n📥 أدوات تتطلب تثبيت يدوي:")
    for tool, url in manual_tools.items():
        print(f"• {tool}: {url}")

def create_windows_security_environment():
    """Create a comprehensive Windows security testing environment"""
    print("🏗️  إنشاء بيئة اختبار أمان متكاملة لنظام Windows...")
    print(f"⏰ وقت البدء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Step 1: Check if Chocolatey is installed
    try:
        subprocess.run(['choco', '--version'], check=True, capture_output=True)
        print("✅ Chocolatey مثبت بالفعل")
    except:
        print("⚠️  Chocolatey غير مثبت")
        if install_chocolatey():
            print("✅ تم تثبيت Chocolatey")
        else:
            print("❌ فشل تثبيت Chocolatey")
            return False
    
    # Step 2: Install security tools
    install_windows_security_tools()
    
    # Step 3: Provide manual installation guide
    install_manual_tools()
    
    # Step 4: Create shortcuts and environment setup
    print("\n🔧 إعداد بيئة العمل...")
    
    # Add tools to PATH
    tools_paths = [
        "C:\\Program Files\\Nmap",
        "C:\\Program Files\\Wireshark",
        "C:\\metasploit-framework\\bin",
        "C:\\Program Files\\Hashcat",
    ]
    
    print("📋 للإضافة إلى PATH المتغير البيئي:")
    for path in tools_paths:
        if os.path.exists(path):
            print(f"✅ {path}")
        else:
            print(f"⚠️  {path} - غير موجود")
    
    print(f"\n⏰ وقت الانتهاء: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🎉 تم اكتمال إعداد بيئة اختبار الأمان!")

def main():
    print("🛡️  برنامج تثبيت أدوات الأمان لنظام Windows")
    print("=" * 60)
    print("هذا البرنامج يساعدك في تثبيت أدوات اختبار الاختراق المتوافقة مع Windows")
    print()
    
    print("📋 الخيارات المتاحة:")
    print("1. تثبيت Chocolatey (مدير الحزم)")
    print("2. تثبيت جميع أدوات الأمان عبر Chocolatey")
    print("3. عرض روابط التثبيت اليدوي")
    print("4. إنشاء بيئة اختبار أمان متكاملة")
    print("5. الخروج")
    print()
    
    choice = input("اختر خياراً (1-5): ").strip()
    
    if choice == "1":
        install_chocolatey()
    elif choice == "2":
        install_windows_security_tools()
    elif choice == "3":
        install_manual_tools()
    elif choice == "4":
        create_windows_security_environment()
    elif choice == "5":
        print("👋 تم الخروج من البرنامج")
        sys.exit(0)
    else:
        print("❌ خيار غير صحيح")

if __name__ == "__main__":
    main()
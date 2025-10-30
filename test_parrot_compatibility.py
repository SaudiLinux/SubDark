#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
اختبار توافق SubDark مع نظام Parrot OS
Test SubDark compatibility with Parrot OS
"""

import os
import sys
import platform
import subprocess
import importlib
from pathlib import Path

class ParrotCompatibilityTester:
    """فحص توافق SubDark مع Parrot OS"""
    
    def __init__(self):
        self.results = {}
        self.is_parrot = self._check_parrot_os()
        self.is_debian_based = self._check_debian_based()
        
    def _check_parrot_os(self):
        """التحقق من نظام Parrot OS"""
        try:
            with open('/etc/os-release', 'r') as f:
                os_info = f.read().lower()
                return 'parrot' in os_info or 'debian' in os_info
        except:
            return False
    
    def _check_debian_based(self):
        """التحقق من نظام Debian-based"""
        return os.path.exists('/etc/debian_version')
    
    def test_python_version(self):
        """اختبار إصدار Python"""
        version = sys.version_info
        compatible = version.major == 3 and version.minor >= 7
        self.results['python_version'] = {
            'version': f"{version.major}.{version.minor}.{version.micro}",
            'compatible': compatible,
            'message': "✅ Python version compatible" if compatible else "❌ Python version too old"
        }
        return compatible
    
    def test_required_packages(self):
        """اختبار الحزم المطلوبة"""
        required_packages = [
            'colorama', 'prettytable', 'requests', 'nmap', 'bs4', 
            'lxml', 'urllib3', 'certifi', 'selenium', 'cvss', 'vulners'
        ]
        
        missing_packages = []
        for package in required_packages:
            try:
                importlib.import_module(package)
            except ImportError:
                missing_packages.append(package)
        
        self.results['required_packages'] = {
            'missing': missing_packages,
            'installed': len(required_packages) - len(missing_packages),
            'total': len(required_packages),
            'message': f"✅ All packages installed" if not missing_packages else f"❌ Missing packages: {', '.join(missing_packages)}"
        }
        
        return len(missing_packages) == 0
    
    def test_security_tools(self):
        """اختبار أدوات الأمان المتوفرة"""
        tools = {
            'nmap': ['nmap', '--version'],
            'sqlmap': ['sqlmap', '--version'],
            'metasploit': ['msfconsole', '--version'],
            'nikto': ['nikto', '--Version'],
            'dirb': ['dirb'],
            'gobuster': ['gobuster', 'version']
        }
        
        available_tools = {}
        for tool, cmd in tools.items():
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                available_tools[tool] = result.returncode == 0 or "version" in result.stdout.lower()
            except:
                available_tools[tool] = False
        
        self.results['security_tools'] = {
            'available': available_tools,
            'count': sum(1 for x in available_tools.values() if x),
            'message': f"✅ Security tools: {sum(1 for x in available_tools.values() if x)}/{len(tools)} available"
        }
        
        return available_tools
    
    def test_file_permissions(self):
        """اختبار صلاحيات الملفات"""
        test_files = [
            'subdark.py',
            'subdark_banner.py',
            'automated_exploit_generator.py'
        ]
        
        permissions = {}
        for file in test_files:
            if os.path.exists(file):
                permissions[file] = {
                    'readable': os.access(file, os.R_OK),
                    'writable': os.access(file, os.W_OK),
                    'executable': os.access(file, os.X_OK)
                }
            else:
                permissions[file] = 'file_not_found'
        
        self.results['file_permissions'] = {
            'permissions': permissions,
            'message': "✅ File permissions OK" if all(
                isinstance(p, dict) and p['readable'] for p in permissions.values()
            ) else "❌ Some files have permission issues"
        }
        
        return permissions
    
    def test_network_connectivity(self):
        """اختبار الاتصال بالشبكة"""
        test_urls = [
            'http://httpbin.org/get',
            'https://www.google.com',
            'https://cve.mitre.org'
        ]
        
        connectivity = {}
        for url in test_urls:
            try:
                import requests
                response = requests.get(url, timeout=5)
                connectivity[url] = response.status_code < 400
            except:
                connectivity[url] = False
        
        self.results['network_connectivity'] = {
            'connectivity': connectivity,
            'working': sum(1 for x in connectivity.values() if x),
            'message': f"✅ Network: {sum(1 for x in connectivity.values() if x)}/{len(test_urls)} URLs accessible"
        }
        
        return connectivity
    
    def test_subdark_imports(self):
        """اختبار استيراد وحدات SubDark"""
        modules_to_test = [
            'subdark_banner',
            'automated_exploit_generator'
        ]
        
        import_results = {}
        for module in modules_to_test:
            try:
                if module == 'subdark_banner':
                    from subdark_banner import display_subdark_banner
                    display_subdark_banner()
                elif module == 'automated_exploit_generator':
                    from automated_exploit_generator import AutomatedExploitGenerator
                    generator = AutomatedExploitGenerator()
                    import_results[module] = "✅ Imported successfully"
            except Exception as e:
                import_results[module] = f"❌ Import failed: {str(e)}"
        
        self.results['subdark_imports'] = import_results
        return import_results
    
    def generate_report(self):
        """توليد تقرير شامل"""
        print("\n" + "="*60)
        print("🛡️  SubDark Parrot OS Compatibility Test Report")
        print("="*60)
        
        print(f"\n📋 System Information:")
        print(f"   OS: {platform.system()} {platform.release()}")
        print(f"   Python: {sys.version}")
        print(f"   Is Parrot/Debian: {'✅ Yes' if self.is_parrot or self.is_debian_based else '❌ No'}")
        
        print(f"\n🔍 Test Results:")
        for test_name, result in self.results.items():
            message = result.get('message', f"✅ {test_name} test completed")
            print(f"   {message}")
        
        # Overall compatibility score
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results.values() 
                           if '✅' in r.get('message', ''))
        
        compatibility_score = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        print(f"\n📊 Compatibility Score: {compatibility_score:.1f}%")
        
        if compatibility_score >= 80:
            print("🎉 Excellent! SubDark should work perfectly on your Parrot OS system.")
        elif compatibility_score >= 60:
            print("⚠️  Good! SubDark should work with minor adjustments.")
        else:
            print("❌ Issues detected. Please check the installation requirements.")
        
        print("\n" + "="*60)
        
        return compatibility_score
    
    def run_all_tests(self):
        """تشغيل جميع اختبارات التوافق"""
        print("🚀 Starting SubDark Parrot OS compatibility tests...")
        
        self.test_python_version()
        self.test_required_packages()
        self.test_security_tools()
        self.test_file_permissions()
        self.test_network_connectivity()
        self.test_subdark_imports()
        
        return self.generate_report()

def main():
    """الدالة الرئيسية"""
    print("🛡️  SubDark Parrot OS Compatibility Tester")
    print("Testing system compatibility for SubDark security tool...")
    
    tester = ParrotCompatibilityTester()
    score = tester.run_all_tests()
    
    if score < 80:
        print("\n🔧 Suggested fixes:")
        print("1. Install missing Python packages: pip install -r requirements.txt")
        print("2. Install security tools: sudo apt install nmap sqlmap metasploit-framework")
        print("3. Run the installation script: bash install_parrot.sh")
        print("4. Make scripts executable: chmod +x *.py")

if __name__ == "__main__":
    main()
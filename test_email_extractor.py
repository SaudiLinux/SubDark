#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نص اختباري لأداة استخراج عناوين البريد الإلكتروني
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin, urlparse

class EmailExtractor:
    def __init__(self):
        self.emails = set()
        self.visited_urls = set()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def extract_emails_from_text(self, text):
        """استخراج عناوين البريد الإلكتروني من النص"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return [email for email in emails if self.is_valid_email(email)]
    
    def is_valid_email(self, email):
        """التحقق من صحة عنوان البريد الإلكتروني"""
        # تصفية البريد المؤقت والغير حقيقي
        temp_domains = [
            'tempmail', 'temp-mail', '10minutemail', 'guerrillamail',
            'mailinator', 'throwaway', 'fakeemail', 'tempmailo'
        ]
        
        domain = email.split('@')[1].lower() if '@' in email else ''
        
        # التحقق من النطاق المؤقت
        for temp_domain in temp_domains:
            if temp_domain in domain:
                return False
        
        # التحقق من صيغة البريد الإلكتروني
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return False
        
        return True
    
    def extract_from_mailto_links(self, soup):
        """استخراج البريد الإلكتروني من روابط mailto"""
        mailto_links = soup.find_all('a', href=re.compile(r'^mailto:', re.I))
        emails = []
        
        for link in mailto_links:
            href = link.get('href', '')
            if 'mailto:' in href:
                email = href.replace('mailto:', '').split('?')[0]
                if self.is_valid_email(email):
                    emails.append(email)
        
        return emails
    
    def extract_from_input_fields(self, soup):
        """استخراج البريد الإلكتروني من حقول الإدخال"""
        emails = []
        
        # البحث عن حقول الإدخال من نوع email
        email_inputs = soup.find_all('input', {'type': 'email'})
        for input_field in email_inputs:
            if 'value' in input_field.attrs:
                email = input_field['value']
                if self.is_valid_email(email):
                    emails.append(email)
        
        # البحث عن حقول الإدخال بأسماء تحتوي على email
        email_name_inputs = soup.find_all('input', {'name': re.compile(r'email', re.I)})
        for input_field in email_name_inputs:
            if 'value' in input_field.attrs and input_field['value']:
                email = input_field['value']
                if self.is_valid_email(email):
                    emails.append(email)
        
        return emails
    
    def extract_from_comments(self, soup):
        """استخراج البريد الإلكتروني من التعليقات HTML"""
        comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
        emails = []
        
        for comment in comments:
            comment_emails = self.extract_emails_from_text(str(comment))
            emails.extend(comment_emails)
        
        return emails
    
    def extract_from_hidden_elements(self, soup):
        """استخراج البريد الإلكتروني من العناصر المخفية"""
        hidden_elements = soup.find_all(style=re.compile(r'display:\s*none', re.I))
        emails = []
        
        for element in hidden_elements:
            text = element.get_text()
            element_emails = self.extract_emails_from_text(text)
            emails.extend(element_emails)
        
        return emails
    
    def extract_emails_from_url(self, url):
        """استخراج عناوين البريد الإلكتروني من URL معين"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # استخراج البريد من النص العادي
            text_emails = self.extract_emails_from_text(soup.get_text())
            
            # استخراج البريد من روابط mailto
            mailto_emails = self.extract_from_mailto_links(soup)
            
            # استخراج البريد من حقول الإدخال
            input_emails = self.extract_from_input_fields(soup)
            
            # استخراج البريد من التعليقات
            comment_emails = self.extract_from_comments(soup)
            
            # استخراج البريد من العناصر المخفية
            hidden_emails = self.extract_from_hidden_elements(soup)
            
            # دمج جميع العناوين
            all_emails = text_emails + mailto_emails + input_emails + comment_emails + hidden_emails
            
            return list(set(all_emails))  # إزالة التكرارات
            
        except Exception as e:
            print(f"خطأ في استخراج البريد من {url}: {e}")
            return []
    
    def get_internal_links(self, url, soup):
        """الحصول على الروابط الداخلية للموقع"""
        internal_links = []
        base_domain = urlparse(url).netloc
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            
            # التحقق من أن الرابط داخلي
            if urlparse(full_url).netloc == base_domain:
                internal_links.append(full_url)
        
        return list(set(internal_links))
    
    def extract_emails_from_website(self, base_url, max_pages=5):
        """استخراج عناوين البريد الإلكتروني من الموقع الكامل"""
        print(f"بدء استخراج عناوين البريد الإلكتروني من: {base_url}")
        
        # استخراج البريد من الصفحة الرئيسية
        main_emails = self.extract_emails_from_url(base_url)
        self.emails.update(main_emails)
        
        try:
            # الحصول على الروابط الداخلية
            response = self.session.get(base_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            internal_links = self.get_internal_links(base_url, soup)
            
            print(f"تم العثور على {len(internal_links)} رابط داخلي")
            
            # استخراج البريد من الصفحات الداخلية (بحد أقصى max_pages)
            pages_crawled = 0
            for link in internal_links[:max_pages]:
                if link not in self.visited_urls:
                    self.visited_urls.add(link)
                    
                    print(f"استخراج البريد من: {link}")
                    page_emails = self.extract_emails_from_url(link)
                    self.emails.update(page_emails)
                    
                    pages_crawled += 1
                    time.sleep(1)  # تأخير لتجنب الحظر
            
            print(f"تم زيارة {pages_crawled} صفحة داخلية")
            
        except Exception as e:
            print(f"خطأ في استكشاف الروابط الداخلية: {e}")
        
        return list(self.emails)
    
    def save_emails_to_file(self, emails, filename="extracted_emails.txt"):
        """حفظ عناوين البريد الإلكتروني في ملف"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("عناوين البريد الإلكتروني المستخرجة:\n")
                f.write("=" * 50 + "\n")
                
                for email in sorted(emails):
                    f.write(f"{email}\n")
                
                f.write(f"\nالعدد الإجمالي: {len(emails)} عنوان بريد إلكتروني\n")
                f.write(f"تاريخ الاستخراج: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            print(f"تم حفظ {len(emails)} عنوان بريد إلكتروني في ملف: {filename}")
            return True
            
        except Exception as e:
            print(f"خطأ في حفظ الملف: {e}")
            return False

def main():
    """اختبار أداة استخراج البريد الإلكتروني"""
    print("=" * 60)
    print("أداة استخراج عناوين البريد الإلكتروني")
    print("=" * 60)
    
    # اختبار على ملف HTML محلي
    test_file = "test_email_page.html"
    
    # قراءة الملف المحلي
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print(f"اختبار الاستخراج من الملف: {test_file}")
        print("-" * 40)
        
        # استخراج البريد من المحتوى
        extractor = EmailExtractor()
        emails = extractor.extract_emails_from_text(html_content)
        
        # استخراج البريد من روابط mailto
        soup = BeautifulSoup(html_content, 'html.parser')
        mailto_emails = extractor.extract_from_mailto_links(soup)
        emails.extend(mailto_emails)
        
        # استخراج البريد من حقول الإدخال
        input_emails = extractor.extract_from_input_fields(soup)
        emails.extend(input_emails)
        
        # استخراج البريد من التعليقات
        comment_emails = extractor.extract_from_comments(soup)
        emails.extend(comment_emails)
        
        # استخراج البريد من العناصر المخفية
        hidden_emails = extractor.extract_from_hidden_elements(soup)
        emails.extend(hidden_emails)
        
        # إزالة التكرارات
        unique_emails = list(set(emails))
        
        if unique_emails:
            print(f"✅ تم العثور على {len(unique_emails)} عنوان بريد إلكتروني:")
            for email in sorted(unique_emails):
                print(f"  📧 {email}")
        else:
            print("❌ لم يتم العثور على عناوين بريد إلكتروني")
        
        # حفظ النتائج
        if unique_emails:
            extractor.save_emails_to_file(unique_emails)
        
    except FileNotFoundError:
        print(f"❌ لم يتم العثور على الملف: {test_file}")
    except Exception as e:
        print(f"❌ خطأ في الاختبار: {e}")
    
    print("\n" + "=" * 60)
    print("✅ اكتمل الاختبار!")
    print("=" * 60)

if __name__ == "__main__":
    main()
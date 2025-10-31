# عرض روابط الهدف المصابة بالثغرات - البيانات الحقيقية

## نظرة عامة
تم تحديث نظام SubDark ليعرض الروابط المصابة بالثغرات بشكل فعلي وحقيقي أثناء عملية استغلال الثغرات. هذه الميزة الجديدة تتيح للمستخدمين رؤية الروابط الدقيقة التي تم استغلالها والتي تحتوي على الثغرات الأمنية.

## المميزات الجديدة

### 1. التقاط الروابط المصابة
- يتم التقاط الروابط المصابة أثناء عملية اختبار الاستغلال
- يتم حفظ الروابط التي أظهرت استجابات إيجابية للثغرات
- يتم تخزين الروابط في قاعدة بيانات نتائج الاستغلال

### 2. عرض الروابط في نتائج الاستغلال
- عرض الروابط المصابة في قسم "إثبات الاستغلال"
- عرض الروابط المصابة في قسم "تأكيد الاستغلال"
- تنسيق واضح مع الرموز والألوان للتمييز

### 3. دعم أنواع الثغرات المختلفة
- **SQL Injection**: عرض الروابط التي تحتوي على أوامر SQL ضارة
- **XSS**: عرض الروابط التي تحتوي على سكريبتات ضارة
- **LFI**: عرض الروابط التي تحتوي على مسارات ملفات غير مصرح بها
- **RFI**: عرض الروابط التي تحتوي على روابط ملفات خارجية

## أمثلة على الروابط المصابة

### ثغرة SQL Injection
```
الروابط المصابة:
  • http://test.example.com/test.php?id=1' OR '1'='1
  • http://test.example.com/login.php?user=admin'--
  • http://test.example.com/search.php?q=test' UNION SELECT * FROM users--
```

### ثغرة XSS
```
الروابط المصابة:
  • http://test.example.com/search.php?q=<script>alert('XSS')</script>
  • http://test.example.com/comment.php?text=<img src=x onerror=alert('XSS')>
```

### ثغرة LFI
```
الروابط المصابة:
  • http://test.example.com/file.php?page=../../../etc/passwd
  • http://test.example.com/include.php?file=../../../../windows/system32/drivers/etc/hosts
```

## كيفية الاستخدام

### الطريقة 1: الاستخدام التلقائي
```python
# إنشاء كائن SubDark
tool = SubDark()
tool.target = "example.com"
tool.target_url = "http://example.com"

# استغلال الثغرات تلقائياً
tool.exploit_vulnerability()

# عرض النتائج مع الروابط المصابة
tool.show_exploit_proof()
tool.confirm_exploitation()
```

### الطريقة 2: إضافة روابط يدوياً
```python
# إضافة نتائج استغلال يدوية مع روابط مصابة
exploit_result = {
    "vulnerability": "SQL Injection",
    "vulnerability_type": "معروفة",
    "exploit_status": "successful",
    "exploit_details": {
        "vulnerable_urls": [
            "http://example.com/vulnerable.php?id=1' OR '1'='1",
            "http://example.com/login.php?user=admin'--"
        ]
    }
}

tool.exploitation_results.append(exploit_result)
tool.show_exploit_proof()
```

## الملفات المحدثة

### subdark.py
- تم تحديث دوال اختبار الاستغلال (`_test_sql_injection`, `_test_xss_exploitation`, `_test_lfi_exploitation`, `_test_rfi_exploitation`)
- تم تحديث دالة `_real_exploit_test` لدعم الروابط المصابة
- تم تحديث دالة `exploit_vulnerability` لتخزين الروابط المصابة
- تم تحديث دالتي `show_exploit_proof` و `confirm_exploitation` لعرض الروابط المصابة

### ملفات الاختبار
- `test_vulnerable_urls.py`: اختبار أساسي لعرض الروابط المصابة
- `test_vulnerable_urls_advanced.py`: اختبار متقدم مع أمثلة حقيقية

## مثال على النتائج

```
إثبات استغلال ثغرة SQL Injection:
الهدف: test.example.com
نوع الاستغلال: معروفة
النتيجة: successful
الوقت: 2025-10-26 20:08:44

الروابط المصابة:
  • http://test.example.com/test.php?id=1' OR '1'='1
  • http://test.example.com/login.php?user=admin'--
  • http://test.example.com/search.php?q=test' UNION SELECT * FROM users--

تأكيد استغلال ثغرة SQL Injection:
الهدف: test.example.com
نوع الاستغلال: معروفة
النتيجة: successful

الروابط المصابة بالثغرة:
  ✓ http://test.example.com/test.php?id=1' OR '1'='1
  ✓ http://test.example.com/login.php?user=admin'--
  ✓ http://test.example.com/search.php?q=test' UNION SELECT * FROM users--
```

## فوائد هذه الميزة

1. **شفافية كاملة**: يمكن للمستخدمين رؤية الروابط الدقيقة التي تم استغلالها
2. **تحليل دقيق**: يسهل تحليل نقاط الضعف في كل رابط على حدة
3. **تقرير احترافي**: يوفر تقارير مفصلة مع الروابط المصابة
4. **تسهيل الإصلاح**: يساعد المطورين في تحديد المواقع الدقيقة التي تحتاج إلى إصلاح

## ملاحظات مهمة

- يتم عرض الروابط المصابة فقط عند وجود نتائج إيجابية من اختبارات الاستغلال
- يتم تنسيق الروابط بشكل واضح مع الرموز (• و ✓) للتمييز بين الأقسام المختلفة
- يتم استخدام ألوان مختلفة لجعل الروابط أكثر وضوحاً
- يمكن إضافة روابط يدوياً أو الحصول عليها تلقائياً من عملية الاستغلال
from django.core.serializers import serialize
from django.apps import apps
import os
import django
import json

# تعیین مسیر فایل تنظیمات پروژه
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "config.settings")  # مسیر خودت رو چک کن

# راه‌اندازی Django
django.setup()


# لیست اپ‌ها و مدل‌ها
app_labels = ['portfolio']  # اپ خودت رو اضافه کن
all_objects = []

for app_label in app_labels:
    app_config = apps.get_app_config(app_label)
    for model in app_config.get_models():
        data = serialize('json', model.objects.all(), ensure_ascii=False)
        all_objects.extend(json.loads(data))  # تبدیل به دیکشنری برای ترکیب

# ذخیره در فایل JSON واحد با UTF-8
with open('db_utf8.json', 'w', encoding='utf-8') as f:
    json.dump(all_objects, f, ensure_ascii=False, indent=2)

print("All data dumped successfully to db_utf8.json!")

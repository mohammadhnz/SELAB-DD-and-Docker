# SELAB-DD-and-Docker

## روال انجام آزمایش
### ساختار پروژه
<div dir="rtl">
در این آزمایش یک سرویس ساده برای مدیریت تسک ایجاد کردیم که برای ذخیره و بازیابی داده‌هایش از پایگاه داده‌ی Postgresql استفاده میکند. و کل سرویس در پشت یک لایه nginx که وظیفه reverse-proxy و load-balance را دارد قرار دارد. خود پروژه هم با Django پیاده سازی شده. که صرفا یک مدل تسک و یک ViewSet برای مدل تسک پیاده سازی شده‌است.
</div>

### نمودار UML
![d drawio](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/0c26ba7a-25ef-45d5-9c93-e49811ce6479)


### داکرهای پروژه

برای این منظور یک Dockerfile برای پروژه django مینویسیم:
![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/8be98806-9d52-49d6-96a2-a98e5ebd9d6d)


سپس برای سرویس پایگاه داده و nginx از داکر کامپوز استفاده میکنیم. دقت کنید که چون نتوورکی تعریف نکردیم به جای ip از اسم ایمیج ها برای وصل شدن به آن ها استفاده میکنیم و برای دیتایس هم volume تعریف میکنیم تا persistant باشد. همینطور در کامند اجرای web دقت میکنیم که باید مایگریشن‌های دیتابیس را اجرا کنیم تا روی هر سیستم جدید قابل اجرا باشند. :
 ![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/3fae2f0f-8aa3-4c31-8a62-4277ba81f325)
![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/cdbe6d0a-9891-4a6b-bfe9-99acb40fd233)


### اجرای اپ
برای این منظور وقتی  به دایرکتوری اپ cd میکنیم از کامند زیر استفاده میکنیم:
‍‍‍
```
sudo docker-compose up -d --build
```
### عکس اجرا و ساخت کانتینر ها
![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/34bf90ad-8d2b-4970-85ab-fb95cfcfbc4c)

### عکس لیست ایمیج‌ها و کانتینرها
![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/36fa3290-f6b0-4142-a2a0-dd06da9a0b4b)

### تصاویر تست‌های پایتونی کنار پروژه
![image](https://github.com/mohammadhnz/SELAB-DD-and-Docker/assets/59181719/b2e6611c-0b6f-4f7a-ab90-5e3391ef1dfc)
### تصاویر درخواست‌های پست من


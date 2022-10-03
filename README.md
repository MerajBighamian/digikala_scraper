# پروژه دریافت اطلاعات محصولات دسته بندی موبایل دیجی کالا و ذخیره آن ها در دیتابیس

## این پروژه با استفاده از django و django rest framework نوشته شده است.

### برای راه اندازی این پروژه کافیست، آن را clone کرده و پس از این عملیات  به مسیر پروژه رفته ( که در آن فایل manage.py وجود دارد) و دستور ‍‍`pip install -r requirement.txt` را زده و از دو دستور زیر را برای ساخت دیتابیس و مدل ها بزنید :
`python manage.py makemigrations` و `python manage.py migrate`

**سپس کافیست دستور `python manage.py runserver` را زده تا پروژه بصورت لوکال اجرا شود.**

حالا میتوانید به مسیر `http://127.0.0.1:8000` رفته و api را به صورت browsable api  تست کنید

همچنین میتوانید با ارسال درخواست `post` به آدرس بالا از api استفاده کنید.
**این api فقط درخواست های ارسال شده با متود `post` را مجاز میداند**

**درخواست شما باید با ساختار زیر باشد:**


`{
"url":"https://www.digikala.com/search/category-mobile-phone/product-list/?page=page_number"
}`

**نکته : درخواست باید دقیقا به شکل بالا باشد**

**نکته : ساختار لینک باید دقیقا به شکل بالا باشد اما شماره صفحه میتواند بر اساس خواست کاربر متفاوت باشد **

**ساختار لینک : `https://www.digikala.com/search/category-mobile-phone/product-list/?page=page_number`**

**به جای `page_number` در ساختار لینک باید صفحه مورد نظر از کالا های موبایل دیجیکالا میتواند باید**

**میتوانید از دسته بندی موبایل در دیجی کالا هر صفحه دلخواهی را انتخاب کرده و لینک آن صفحه از محصولات را به api داده تا آن محصولات در دیتابیس ذخیره شود.**

**در قسمت `test.py` ۹ تست نوشته شده است که ۴ تای آن برای بررسی حالات درست url و ۵ تای آن برای بررسی حالات اشتباه دریافت url است**

**این api به عنوان پاسخ به شما لیست محصولات دریافت شده از لینک مورد نظر را از دیتابیس فراخوانده در به صورت json برای شما بر میگرداند و شما میتواند از این json در فرانت پروژه خود استفاده کنید.**

در این پروژه سعی شده که براساس اصول `clean code` و قوانینی مانند `DRY` , `single Responsibility` و .... پروژه طراحی و اجرا شود 
** با این حال به دلیل نیاز نبودن داکیومنت نویسی از docsrting ها استفاده شده تا توسعه دهنده بهتر با پروژه آشنا شود.**

**در این پروژه از دیتابیس `sqlite` استفاده شده که در صورت نیاز میتوانید آن را به `postgresql`**

**در تسک این پروژه خواسته نشده است که تمام اطلاعات دریافتی از محصولات را به عنوان json برگشت داده شود اما من سعی کردم که تمام اطلاعات موجود محصولات را که در دیتابیس ذخیره شده است را به صورت json به عنوان نتیجه برگردانم**

**در این پروژه برای سریعتر شدن روند میتوان اطلاعات دریافتی از scrapper را به صورت مستقیم و به شکل json به سمت front end ارسال کرد و در در back end نیز ‌آن اطلاعات را در دیتابیس ذخیره کرد ولی مقصود این task چیز دیگری بود**

**حالات مختلف خرابی لینک یا خرابی درخواست handle شده است**

**برای توسعه بیشتر این پروژه میتوان آن را برای تمام دسته بندی محصولات سایت دیجی کالا برنامه ریزی کرد و همچنین میتوان تمامی مشخصامحصولات را نیز در دیتابیس ذخیره کنیم**

این پروژه حدود یک روز زده شده است


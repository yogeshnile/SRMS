# SRMS :notebook: &nbsp;[![](https://camo.githubusercontent.com/17fa56d1fbad7bb4082c9711a77b984b85e79446/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e362d627269676874677265656e2e737667)](https://python.org)

 - In this Repo I developed a Student Result declaration system using Django.

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

# How to run the project? :thinking:
**1).** Run all command manually
  - Clone github repository in your local system  `git clone https://github.com/yogeshnile/SRMS.git`
  - Move in SRMS repository  `cd SRMS`
  - Create new virtual python environment  `python3 -m venv venv`
  - Activate virtual python environment  `source venv/bin/activate`
  - Install all the libraries mentioned in [requirements.txt](https://github.com/yogeshnile/SRMS/blob/master/requirements.txt)  using  `pip install -r requirements.txt`
  - Run Django project  `python manage.py runserver`
  - Go to your browser and type http://127.0.0.1:8000/ in the address bar.
  - Hurray! That's it. <br>


**2).** Run Shell Script
  - Clone github repository in your local system  `git clone https://github.com/yogeshnile/unix.git`
  - Give execute permission to [SRMS.sh](https://github.com/yogeshnile/unix/blob/master/SRMS.sh) file via  `chmod +x SRMS.sh`
  - Run SRMS.sh file using `./SRMS.sh`
  - Go to your browser and type http://127.0.0.1:8000/ in the address bar.
  - Finished...

# Technology used in Project :hotsprings:
<img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/django.png" width="300">

# Directory Tree :cactus:
<details><summary>Show Tree</summary>
  
  ```bash
  .
├── db.sqlite3
├── first_year.csv
├── Images
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   └── 5.png
├── LICENSE
├── manage.py
├── professor
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20200921_1310.py
│   │   ├── 0003_auto_20200921_1510.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_auto_20200921_1310.cpython-36.pyc
│   │       ├── 0003_auto_20200921_1510.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── second_year.csv
├── srms
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── 404
│   │   ├── main.scss
│   │   ├── style.css
│   │   └── style.css.map
│   ├── css
│   │   ├── animate-css
│   │   │   └── animate.min.css
│   │   ├── bootstrap.css
│   │   ├── bootstrap.min.css
│   │   ├── font-awesome.css
│   │   ├── font-awesome.min.css
│   │   ├── lobipanel
│   │   │   ├── lobipanel.css
│   │   │   └── lobipanel.min.css
│   │   ├── main2.css
│   │   ├── main.css
│   │   ├── prism
│   │   │   └── prism.css
│   │   └── util.css
│   ├── fonts
│   │   ├── font-awesome-4.7.0
│   │   │   ├── css
│   │   │   │   ├── font-awesome.css
│   │   │   │   └── font-awesome.min.css
│   │   │   ├── fonts
│   │   │   │   ├── FontAwesome.otf
│   │   │   │   ├── fontawesome-webfont.eot
│   │   │   │   ├── fontawesome-webfont.svg
│   │   │   │   ├── fontawesome-webfont.ttf
│   │   │   │   ├── fontawesome-webfont.woff
│   │   │   │   └── fontawesome-webfont.woff2
│   │   │   ├── HELP-US-OUT.txt
│   │   │   ├── less
│   │   │   │   ├── animated.less
│   │   │   │   ├── bordered-pulled.less
│   │   │   │   ├── core.less
│   │   │   │   ├── fixed-width.less
│   │   │   │   ├── font-awesome.less
│   │   │   │   ├── icons.less
│   │   │   │   ├── larger.less
│   │   │   │   ├── list.less
│   │   │   │   ├── mixins.less
│   │   │   │   ├── path.less
│   │   │   │   ├── rotated-flipped.less
│   │   │   │   ├── screen-reader.less
│   │   │   │   ├── stacked.less
│   │   │   │   └── variables.less
│   │   │   └── scss
│   │   │       ├── _animated.scss
│   │   │       ├── _bordered-pulled.scss
│   │   │       ├── _core.scss
│   │   │       ├── _fixed-width.scss
│   │   │       ├── font-awesome.scss
│   │   │       ├── _icons.scss
│   │   │       ├── _larger.scss
│   │   │       ├── _list.scss
│   │   │       ├── _mixins.scss
│   │   │       ├── _path.scss
│   │   │       ├── _rotated-flipped.scss
│   │   │       ├── _screen-reader.scss
│   │   │       ├── _stacked.scss
│   │   │       └── _variables.scss
│   │   ├── iconic
│   │   │   ├── css
│   │   │   │   ├── material-design-iconic-font.css
│   │   │   │   └── material-design-iconic-font.min.css
│   │   │   └── fonts
│   │   │       ├── Material-Design-Iconic-Font.eot
│   │   │       ├── Material-Design-Iconic-Font.svg
│   │   │       ├── Material-Design-Iconic-Font.ttf
│   │   │       ├── Material-Design-Iconic-Font.woff
│   │   │       └── Material-Design-Iconic-Font.woff2
│   │   ├── Linearicons-Free-v1.0.0
│   │   │   ├── icon-font.min.css
│   │   │   └── WebFont
│   │   │       ├── Linearicons-Free.eot
│   │   │       ├── Linearicons-Free.svg
│   │   │       ├── Linearicons-Free.ttf
│   │   │       ├── Linearicons-Free.woff
│   │   │       └── Linearicons-Free.woff2
│   │   ├── poppins
│   │   │   ├── Poppins-BlackItalic.ttf
│   │   │   ├── Poppins-Black.ttf
│   │   │   ├── Poppins-BoldItalic.ttf
│   │   │   ├── Poppins-Bold.ttf
│   │   │   ├── Poppins-ExtraBoldItalic.ttf
│   │   │   ├── Poppins-ExtraBold.ttf
│   │   │   ├── Poppins-ExtraLightItalic.ttf
│   │   │   ├── Poppins-ExtraLight.ttf
│   │   │   ├── Poppins-Italic.ttf
│   │   │   ├── Poppins-LightItalic.ttf
│   │   │   ├── Poppins-Light.ttf
│   │   │   ├── Poppins-MediumItalic.ttf
│   │   │   ├── Poppins-Medium.ttf
│   │   │   ├── Poppins-Regular.ttf
│   │   │   ├── Poppins-SemiBoldItalic.ttf
│   │   │   ├── Poppins-SemiBold.ttf
│   │   │   ├── Poppins-ThinItalic.ttf
│   │   │   └── Poppins-Thin.ttf
│   │   └── ubuntu
│   │       ├── Ubuntu-BoldItalic.ttf
│   │       ├── Ubuntu-Bold.ttf
│   │       ├── Ubuntu-Italic.ttf
│   │       ├── Ubuntu-LightItalic.ttf
│   │       ├── Ubuntu-Light.ttf
│   │       ├── Ubuntu-MediumItalic.ttf
│   │       ├── Ubuntu-Medium.ttf
│   │       ├── Ubuntu-Regular.ttf
│   │       └── UFL.txt
│   ├── images
│   │   └── icons
│   │       ├── index.ico
│   │       └── login.ico
│   ├── index
│   │   ├── css
│   │   │   ├── main.css
│   │   │   └── util.css
│   │   ├── fonts
│   │   │   ├── font-awesome-4.7.0
│   │   │   │   ├── css
│   │   │   │   │   ├── font-awesome.css
│   │   │   │   │   └── font-awesome.min.css
│   │   │   │   ├── fonts
│   │   │   │   │   ├── FontAwesome.otf
│   │   │   │   │   ├── fontawesome-webfont.eot
│   │   │   │   │   ├── fontawesome-webfont.svg
│   │   │   │   │   ├── fontawesome-webfont.ttf
│   │   │   │   │   ├── fontawesome-webfont.woff
│   │   │   │   │   └── fontawesome-webfont.woff2
│   │   │   │   ├── HELP-US-OUT.txt
│   │   │   │   ├── less
│   │   │   │   │   ├── animated.less
│   │   │   │   │   ├── bordered-pulled.less
│   │   │   │   │   ├── core.less
│   │   │   │   │   ├── fixed-width.less
│   │   │   │   │   ├── font-awesome.less
│   │   │   │   │   ├── icons.less
│   │   │   │   │   ├── larger.less
│   │   │   │   │   ├── list.less
│   │   │   │   │   ├── mixins.less
│   │   │   │   │   ├── path.less
│   │   │   │   │   ├── rotated-flipped.less
│   │   │   │   │   ├── screen-reader.less
│   │   │   │   │   ├── stacked.less
│   │   │   │   │   └── variables.less
│   │   │   │   └── scss
│   │   │   │       ├── _animated.scss
│   │   │   │       ├── _bordered-pulled.scss
│   │   │   │       ├── _core.scss
│   │   │   │       ├── _fixed-width.scss
│   │   │   │       ├── font-awesome.scss
│   │   │   │       ├── _icons.scss
│   │   │   │       ├── _larger.scss
│   │   │   │       ├── _list.scss
│   │   │   │       ├── _mixins.scss
│   │   │   │       ├── _path.scss
│   │   │   │       ├── _rotated-flipped.scss
│   │   │   │       ├── _screen-reader.scss
│   │   │   │       ├── _stacked.scss
│   │   │   │       └── _variables.scss
│   │   │   ├── iconic
│   │   │   │   ├── css
│   │   │   │   │   ├── material-design-iconic-font.css
│   │   │   │   │   └── material-design-iconic-font.min.css
│   │   │   │   └── fonts
│   │   │   │       ├── Material-Design-Iconic-Font.eot
│   │   │   │       ├── Material-Design-Iconic-Font.svg
│   │   │   │       ├── Material-Design-Iconic-Font.ttf
│   │   │   │       ├── Material-Design-Iconic-Font.woff
│   │   │   │       └── Material-Design-Iconic-Font.woff2
│   │   │   └── montserrat
│   │   │       ├── Montserrat-BlackItalic.ttf
│   │   │       ├── Montserrat-Black.ttf
│   │   │       ├── Montserrat-BoldItalic.ttf
│   │   │       ├── Montserrat-Bold.ttf
│   │   │       ├── Montserrat-ExtraBoldItalic.ttf
│   │   │       ├── Montserrat-ExtraBold.ttf
│   │   │       ├── Montserrat-ExtraLightItalic.ttf
│   │   │       ├── Montserrat-ExtraLight.ttf
│   │   │       ├── Montserrat-Italic.ttf
│   │   │       ├── Montserrat-LightItalic.ttf
│   │   │       ├── Montserrat-Light.ttf
│   │   │       ├── Montserrat-MediumItalic.ttf
│   │   │       ├── Montserrat-Medium.ttf
│   │   │       ├── Montserrat-Regular.ttf
│   │   │       ├── Montserrat-SemiBoldItalic.ttf
│   │   │       ├── Montserrat-SemiBold.ttf
│   │   │       ├── Montserrat-ThinItalic.ttf
│   │   │       ├── Montserrat-Thin.ttf
│   │   │       └── OFL.txt
│   │   ├── images
│   │   │   ├── bg-01.jpg
│   │   │   ├── icons
│   │   │   │   └── favicon.ico
│   │   │   └── img-01.png
│   │   ├── js
│   │   │   └── main.js
│   │   └── vendor
│   │       ├── animate
│   │       │   └── animate.css
│   │       ├── animsition
│   │       │   ├── css
│   │       │   │   ├── animsition.css
│   │       │   │   └── animsition.min.css
│   │       │   └── js
│   │       │       ├── animsition.js
│   │       │       └── animsition.min.js
│   │       ├── bootstrap
│   │       │   ├── css
│   │       │   │   ├── bootstrap.css
│   │       │   │   ├── bootstrap.css.map
│   │       │   │   ├── bootstrap-grid.css
│   │       │   │   ├── bootstrap-grid.css.map
│   │       │   │   ├── bootstrap-grid.min.css
│   │       │   │   ├── bootstrap-grid.min.css.map
│   │       │   │   ├── bootstrap.min.css
│   │       │   │   ├── bootstrap.min.css.map
│   │       │   │   ├── bootstrap-reboot.css
│   │       │   │   ├── bootstrap-reboot.css.map
│   │       │   │   ├── bootstrap-reboot.min.css
│   │       │   │   └── bootstrap-reboot.min.css.map
│   │       │   └── js
│   │       │       ├── bootstrap.js
│   │       │       ├── bootstrap.min.js
│   │       │       ├── popper.js
│   │       │       ├── popper.min.js
│   │       │       └── tooltip.js
│   │       ├── countdowntime
│   │       │   └── countdowntime.js
│   │       ├── css-hamburgers
│   │       │   ├── hamburgers.css
│   │       │   └── hamburgers.min.css
│   │       ├── daterangepicker
│   │       │   ├── daterangepicker.css
│   │       │   ├── daterangepicker.js
│   │       │   ├── moment.js
│   │       │   └── moment.min.js
│   │       ├── jquery
│   │       │   └── jquery-3.2.1.min.js
│   │       ├── noui
│   │       │   ├── nouislider.css
│   │       │   ├── nouislider.js
│   │       │   ├── nouislider.min.css
│   │       │   └── nouislider.min.js
│   │       ├── perfect-scrollbar
│   │       │   ├── perfect-scrollbar.css
│   │       │   └── perfect-scrollbar.min.js
│   │       └── select2
│   │           ├── select2.css
│   │           ├── select2.js
│   │           ├── select2.min.css
│   │           └── select2.min.js
│   ├── js
│   │   ├── bootstrap
│   │   │   ├── bootstrap.js
│   │   │   └── bootstrap.min.js
│   │   ├── iscroll
│   │   │   └── iscroll.js
│   │   ├── jquery
│   │   │   ├── jquery-2.2.4.js
│   │   │   └── jquery-2.2.4.min.js
│   │   ├── lobipanel
│   │   │   ├── lobipanel.js
│   │   │   └── lobipanel.min.js
│   │   ├── main2.js
│   │   ├── main.js
│   │   ├── modernizr
│   │   │   ├── modernizr.js
│   │   │   └── modernizr.min.js
│   │   ├── pace
│   │   │   └── pace.min.js
│   │   └── prism
│   │       ├── prism.js
│   │       ├── prism-line-numbers.js
│   │       └── prism.min.js
│   └── vendor
│       ├── animate
│       │   └── animate.css
│       ├── animsition
│       │   ├── css
│       │   │   ├── animsition.css
│       │   │   └── animsition.min.css
│       │   └── js
│       │       ├── animsition.js
│       │       └── animsition.min.js
│       ├── bootstrap
│       │   ├── css
│       │   │   ├── bootstrap.css
│       │   │   ├── bootstrap.css.map
│       │   │   ├── bootstrap-grid.css
│       │   │   ├── bootstrap-grid.css.map
│       │   │   ├── bootstrap-grid.min.css
│       │   │   ├── bootstrap-grid.min.css.map
│       │   │   ├── bootstrap.min.css
│       │   │   ├── bootstrap.min.css.map
│       │   │   ├── bootstrap-reboot.css
│       │   │   ├── bootstrap-reboot.css.map
│       │   │   ├── bootstrap-reboot.min.css
│       │   │   └── bootstrap-reboot.min.css.map
│       │   └── js
│       │       ├── bootstrap.js
│       │       ├── bootstrap.min.js
│       │       ├── popper.js
│       │       ├── popper.min.js
│       │       └── tooltip.js
│       ├── countdowntime
│       │   └── countdowntime.js
│       ├── css-hamburgers
│       │   ├── hamburgers.css
│       │   └── hamburgers.min.css
│       ├── daterangepicker
│       │   ├── daterangepicker.css
│       │   ├── daterangepicker.js
│       │   ├── moment.js
│       │   └── moment.min.js
│       ├── jquery
│       │   └── jquery-3.2.1.min.js
│       ├── perfect-scrollbar
│       │   ├── perfect-scrollbar.css
│       │   └── perfect-scrollbar.min.js
│       └── select2
│           ├── select2.css
│           ├── select2.js
│           ├── select2.min.css
│           └── select2.min.js
├── student
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_second_year_third_year.py
│   │   ├── 0003_csv.py
│   │   ├── 0004_auto_20200923_1752.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-36.pyc
│   │       ├── 0002_second_year_third_year.cpython-36.pyc
│   │       ├── 0003_csv.cpython-36.pyc
│   │       ├── 0004_auto_20200923_1752.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── apps.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates
    ├── 404.html
    ├── dashboard.html
    ├── index.html
    ├── login.html
    └── result.html

85 directories, 325 files
  ```
</details>

## ScreenShot :camera_flash:
![](https://github.com/yogeshnile/SRMS/blob/master/Images/1.png)    ![](https://github.com/yogeshnile/SRMS/blob/master/Images/2.png)
![](https://github.com/yogeshnile/SRMS/blob/master/Images/3.png)    ![](https://github.com/yogeshnile/SRMS/blob/master/Images/4.png)
![](https://github.com/yogeshnile/SRMS/blob/master/Images/5.png)

## Bug / Feature Request :man_technologist:
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/yogeshnile/SRMS/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/yogeshnile/SRMS/issues/new). Please include sample queries and their corresponding results.


## Connect with me! 🌐
Known on internet as **Yogesh Nile**

[![][I_LinkedIn]][LinkedIn]  [![][I_Github]][Github] [![][I_Twitter]][Twitter] [![][I_Telegram]][Telegram] [![][I_Instagram]][Instagram]  [![][I_Instagram Personal]][Instagram Personal]   [![][I_discord]][discord]

## Email Me :e-mail:

[![][I_Email]][E-mail]


[LinkedIn]: https://bit.ly/2Ky3ho6
[Github]: https://bit.ly/2yoggit
[Twitter]: https://bit.ly/3dbLJLC
[Telegram]: https://t.me/yogeshnile
[Instagram]: https://bit.ly/3b9Qeo4
[Instagram Personal]: https://bit.ly/32SXHV0
[E-mail]: mailto:yogeshnile.work4u@gmail.com
[discord]: https://discord.gg/R2ug3gR

[I_discord]: https://img.icons8.com/bubbles/100/000000/discord-logo.png
[I_LinkedIn]: https://img.icons8.com/bubbles/100/000000/linkedin.png
[I_Github]: https://img.icons8.com/bubbles/100/000000/github.png
[I_Twitter]: https://img.icons8.com/bubbles/100/000000/twitter.png
[I_Telegram]: https://img.icons8.com/bubbles/100/000000/telegram-app.png
[I_Instagram]: https://img.icons8.com/bubbles/100/000000/instagram-new.png
[I_Instagram Personal]: https://img.icons8.com/bubbles/100/000000/instagram.png
[I_Email]: https://img.icons8.com/bubbles/100/000000/secured-letter.png


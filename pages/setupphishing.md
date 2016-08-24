title: Setup A Simple Phishing Site
sub_title: Very easy way to make a fake site.
date: 2016-06-14
tags: [phishing, setup, template]


In this blog, I will demonstrate a easy way to setup a phishing site.

It’s very simple even for newbies without coding experience, and this
method is used by lots of phishing templates we have collected during
phishing detection research.

Before you start, pay attention, I write this is just for education
purpose and you are supposed to deploy and test it locally. I am not
responsible if anyone use this for negative purpose.

Step 1
======

Preparation:
------------

You will need a linux server which can host website.

I will use ubuntu 14.04 as an example.

**Install apache server:**

> *$ sudo apt-get install apache2*

**Install php7:**

> *$ sudo apt-get install php7.0*

> *$ sudo apt-get install libapache2-mod-php7.0*

**Restart apache2**

> *$ sudo service apache2 restart*

**Install sendmail:**

> *$ sudo apt-get install sendmail*

Step 2
======

Create Webpage
--------------

Visit the website you want to target on.

In this step, I suggest to use single-page-login web pages held on
popular sites like [*Paypal*](https://www.paypal.com/signin),
[*Dropbox*](https://www.dropbox.com/login), but do not choose
multiple-page-login pages such as
[*Google*](https://accounts.google.com/login) or
[*Yahoo*](https://login.yahoo.com/) unless you want to write javascript
or backend code by your own.

The reason is that for these multiple-page-login pages, it always
involves at least two steps input which means users have to input
username first and click next and then input password after username
validation. The interaction between client and backend server is complex
and is hard to bypass. (But if you do find a way to bypass and reuse
validation interaction, it also helps phishing attackers to validate
their credentials. I will demonstrate how to use this technique in the
future posts.)

<img src="https://lh3.googleusercontent.com/b936Npu4iJPks1EL8t6jhrTqu63OmLWuYX8hbkS3KYAyWopDgpjXzA0mnL6oeZUIvWu13eWQ3yRO3pr82Qu-T8L5P64aYqo2bD3_MV9JJSDGM4QKwJezN5oF78nv0W0AftE5mDqr" style="border: medium none; transform: rotate(0rad);" width="350">
<img src="https://lh6.googleusercontent.com/X3Vzc7eLypwHbr1VmY0bj2Mx53la79nPbkHkf6HxfemVd1OKvq4YMF-WYap_yUjDrJHL-0GKXKMZ5oBsc6X_K-TaYQY1yXMSxfrlL66fGNGE-Wh3GEykXyaEQ5DeoTt4lfFMhChp" style="border: medium none; transform: rotate(0rad);"  width="330">
<br>multiple-page -login

<img src="https://lh5.googleusercontent.com/czZzJasAD7HpJLeG0ZxebXLwhMRqSZT68451OqE-YSYMCq_0QOwKy9JkZu1okdLt7-5fxBx_lLYA1gJEU6oGi9Q1vsW2EToYzG486P-qXoInn2_VC36a_jxu1glE8uJetlgqgmq2" style="-webkit-transform: rotate(0.00rad); border: none; transform: rotate(0.00rad);"  width="350">
<br>single-page-login

In this blog, I will use [*Paypal*](https://www.paypal.com/signin) as an
example.

Open your browser and visit [*Paypal*](https://www.paypal.com/signin)
login page. Then right click the page and click “save as” to save page.

After this step you will notice an html file and a resource folder is
saved. Change the name to be index.html.

> *$ mv Log\\ in\\ to\\ your\\ PayPal\\ account.html index.html*

If you double click the index html, you can see the webpage is working
file offline.

Step 3
======

Edit file
---------

In the same folder as index.html, create a file called “sigin.php”

> *$ touch signin.php*

Edit this file,

> *$ vim signin.php*

Copy paste the code.

<script src="https://gist.github.com/rundongliu/1b9d1aa868eb1ec176103691eef516c8.js"></script>

Replace your email in the code. Save.

Open index.html

Search for “action=”, immediately after that, replace “signin” with
“signin.php” which points to the file you created just now.

Then move all the files to /var/www/html/

> *$ sudo mv \* /var/www/html/*

Step 4
======

Test and Finish
---------------

If you now visit your website, you can see the paypal phishing website
is held on your server.

But when you test it, you can get the credentials users have input but
it fails to redirect to paypal official sites after that. This is
because some javascript was running in your browser and did some error
checking in the backgrond.

To fix that

Remove all js files in the resource folder.

> *$ sudo rm /var/www/html/Log\\ in\\ to\\ your\\ PayPal\\
account\_files/\*.js*

After that, your phishing site is good to go!

Conclusion:
===========

In this blog, I demonstrated the easiest way to create a phishing
template. This is the simplest way and is also the most popular way
attackers use.

Other templates may include advanced features such as redirection, code
obfuscation, anti-robot and others. But they all developed from this
basic method.

**Visit**
[***blogger***](https://rundongliu.blogspot.com/2016/06/setup-simple-phishing-site.html)
**to comment.**

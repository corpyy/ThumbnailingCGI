#!/usr/bin/env python
# -*- coding: utf-8 -*-

html_body= '''
<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../css/style.css">
<title>Thumbnailing</title>
<!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
</head>

<body>

<div id="wrap">

<header>
<h1>
どちらのサムネイル画像が良いですか？
</h1>
<h2>
スマートフォンで表示するためのサムネイル画像として，下の２つ（緑枠 or 黄枠）のサムネイル画像のうちどちらが良いですか？　右下の３つの選択肢から選び，元ページに戻って選択して下さい．
</h2>
<h2>
<font color="#ff0000">
※注意事項
  <ul>
    <li>画像が適切に表示されない場合は，ページを更新して下さい </li>
    <li>不正防止のため、設問の合間にかんたんなチェック設問が入ります </li>
    <li>チェック設問の誤解答が多い場合、続けてタスクを実施できなくなります </li>
  </ul>
</font>
</h2>
</header>

<div id="sidenavi">
<h2>
<h2>
<img src="images/clip/%s" width="200" alt="Thumbnail1" title="サムネイル画像1" style="border:solid 3px #00FF41" class="appIconBig"></h2>
<h2><div align="center">OR</div></h2>
<img src="images/clip/%s" width="200" alt="Thumbnail1" title="サムネイル画像2" style="border:solid 3px #FFFF00" class="appIconBig"></h2>
<br>
<h2>   
  <ul>
    <li>緑枠のサムネイル画像の方が良い． </li>
    <li>どちらも同じくらい． </li>
    <li>黄枠のサムネイル画像の方が良い． </li>
   </ul>
</h2>
</div>

<div id="contents">
<h2>
<img src="images/ed/%s" alt="Origin" title="オリジナル画像" class="appIconBig"></h2>
</div>

<footer>
<h2>
</footer>

</div>

</body>
</html>'''

import cgi
form = cgi.FieldStorage()

print 'Content-type: text/html\n'
print html_body % (form['thumb1'].value, form['thumb2'].value, form ['img'].value)

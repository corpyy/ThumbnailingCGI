#!/usr/bin/env python
# -*- coding: utf-8 -*-

html_body= '''
<!DOCTYPE html>
<html>
<head>
  <title>Thumbnailing</title>
  <meta http-equiv="Content-type" content="text/html;charset=UTF-8" />

<script src="../js/jquery.min.js"></script>
<script src="../js/jquery.Jcrop.js"></script>
<script type="text/javascript">
  jQuery(function($){

    // Create variables (in this scope) to hold the API and image size
    var jcrop_api,
        boundx,
        boundy,

        // Grab some information about the preview pane
        $preview = $('#preview-pane'),
        $pcnt = $('#preview-pane .preview-container'),
        $pimg = $('#preview-pane .preview-container img'),

        xsize = $pcnt.width(),
        ysize = $pcnt.height();
    
    console.log('init',[xsize,ysize]);
    $('#target').Jcrop({
      onChange: updatePreview,
      onSelect: updatePreview,
      aspectRatio: xsize / ysize
    },function(){
      // Use the API to get the real image size
      var bounds = this.getBounds();
      boundx = bounds[0];
      boundy = bounds[1];
      // Store the API in the jcrop_api variable
      jcrop_api = this;

      // Move the preview into the jcrop container for css positioning
      $preview.appendTo(jcrop_api.ui.holder);
    });

    function updatePreview(c)
    {
      if (parseInt(c.w) > 0)
      {
        var rx = xsize / c.w;
        var ry = ysize / c.h;

        $pimg.css({
          width: Math.round(rx * boundx) + 'px',
          height: Math.round(ry * boundy) + 'px',
          marginLeft: '-' + Math.round(rx * c.x) + 'px',
          marginTop: '-' + Math.round(ry * c.y) + 'px'
        });
      document.getElementById("area").textContent="(" + c.x + ", " + c.y + ") - (" + Math.round(c.w) + ", " + Math.round(c.h) + ")";
      }
    };

  });


</script>
<link rel="stylesheet" href="demo_files/main.css" type="text/css" />
<link rel="stylesheet" href="demo_files/demos.css" type="text/css" />
<link rel="stylesheet" href="../css/jquery.Jcrop.css" type="text/css" />
<style type="text/css">

/* Apply these styles only when #preview-pane has
   been placed within the Jcrop widget */
.jcrop-holder #preview-pane {
  display: block;
  position: absolute;
  z-index: 2000;
  top: 10px;
  right: -280px;
  padding: 6px;
  border: 1px rgba(0,0,0,.4) solid;
  background-color: white;

  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;

  -webkit-box-shadow: 1px 1px 5px 2px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 1px 1px 5px 2px rgba(0, 0, 0, 0.2);
  box-shadow: 1px 1px 5px 2px rgba(0, 0, 0, 0.2);
}

/* The Javascript code will set the aspect ratio of the crop
   area based on the size of the thumbnail preview,
   specified here */
#preview-pane .preview-container {
  width: 242px;
  height: 100px;
  overflow: hidden;
}

</style>

</head>
<body>

<div class="container">
<div class="row">
<div class="span12">
<div class="jc-demo-box">

<div class="page-header">
<h1>黒い領域を含まないように赤い領域をを矩形で選択して下さい．</h1>
</div>

  <img src="http://%s" id="target" alt="[Image Example]" />

  <div id="preview-pane">
    <div>スマートフォンでの表示サイズ</div>
    <div class="preview-container">
      <img src="http://%s"  class="jcrop-preview" alt="Preview" />
    </div>
  </div>

  <div class="description">
  <p>
    <div id="area"></div>
    <font size="4" color="#ff0000"><b>上の座標をコピーしてリンク元ページのフォームに貼り付けて下さい．</b></font>
  </p>
  </div>

<div class="clearfix"></div>

</div>
</div>
</div>
</div>

</body>
</html>'''

import cgi
form = cgi.FieldStorage()

print 'Content-type: text/html\n'
print html_body % (form['img'].value, form ['img'].value)


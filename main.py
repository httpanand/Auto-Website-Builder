__author__ = 'Http Anand'

import time
name = input('Enter website name : \n')
header_img = input('Enter header image link : \n')
bg_img = input('Enter background image link : \n')
title = input('Enter title for your website : \n')
t_color = input('Enter colour for title : \n')
tlbar_img = input('Enter titleBar image link : \n')

html = f''' 
<html>
<head> 
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,700;1,400&display=swap');
</style>
     <title>{name}</title>
	 <link rel = "icon" href ="{tlbar_img}">
	 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

</head>
<body style="background:url('{bg_img}')no-repeat center center fixed;;-webkit-background-size: cover; -moz-background-size: cover; background-size: cover; -o-background-size: cover; height:100%; overflow: hidden;">

<section id="sticky-header">
<nav style="background-color: #000000;opacity:90%" class="navbar fixed-top navbar-expand-lg navbar-light" >
  <a id="strs" class="navbar-brand" href="#"><img height="40px" src="{header_img}"></a>
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a id="home" style="color:white" class="nav-link" href="#">HOME<span class="sr-only">(current)</span></a>
      </li>
    
    </ul>
  </div>
</nav>
</section>

<div class="container-fluid text-center">
<h1 id="title" style="font-family: 'Roboto Mono', monospace;font-size:100px;color:{t_color};padding-top:300px;"> {title} </h1>
</div>


''' 


f = open("html.html","w")
f.write(html)
f.close()

res = '''
<style>
@media (orientation: portrait) {
  #title{
    font-size : 130px !important ; 
    padding-top: 800px !important; 
   
  }
 </style>
  </body>
  </html>
'''

end = '''
  </body>
  </html>
'''

responsive = input('Do you want to make your website mobile responsive ?')
if(responsive == 'yes'):
	fi = open("html.html","a")
	fi.write(res)
	fi.close()
else:
	fj = open("html.html","a")
	fj.write(end)
	fj.close()

print('Website building...')
time.sleep(3)
print('Website Built succesfully - open html.html')
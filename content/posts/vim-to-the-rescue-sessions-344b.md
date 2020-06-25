---
title: 'Vim to the rescue: Sessions'
date: '2020-05-04T10:34:53.300Z'
excerpt: >-
  Introduction   One of the reasons that people go for IDEs is that the moment
  you open one, y...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--DcQxWjwb--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--6gAxEDL2--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/l139ond5ng96j2149yjj.png
comments_count: 0
positive_reactions_count: 9
tags:
  - vim
  - linux
  - tutorial
  - todayilearned
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-sessions-344b'
layout: post
---
## Introduction

One of the reasons that people go for IDEs is that the moment you open one, you have everything exactly how you want it. With a file browser on the left hand side, coding window on the right and an attached terminal below. But whenever you open vim, you have to open the file browser and terminal from scratch. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/99v0jx3o6pairkzjtfsx.png)

Well there is a quick way around it. You can actually store sessions in vim. You can then open that particular session to see exactly what you want to see.

---

## Creating a session in vim

Open vim. Now open the programs that you want to see in your session. Let us open the **Lex** file browser:


```vimscript
:Lex
```

Now let us open any file, and the open a terminal below by running the following command:


```vimscript
:bel term
```


To save a session, you can use the 
`mks[ession]`
 command. Note that all sessions have a 
`.vim`
 extension. Vim sessions also store the split sizes, so feel free to resize your terminal without worrying about ever doing it again after opening vim


```vimscript
:mks session.vim
```


You can now safely exit out of vim without worrying about loosing your layout. You will be able to see a 
`session.vim`
 file in your current directory. To open it use the **-S** flag in vim:


```sh
vim -S session.vim
```
 

---

## A few things to note

* If you add a **!** symbol after 
`mks`
, it overwrites the file you specify.
* If no file name is supplied then the default file is **Session.vim**
* Want to store multiple files open on multiple tabs? Go ahead!
* Want to use additional UI details while opening a session? Go ahead and create a **x.vim** file in the same directory and go ahead.



*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-sessions-344b)*


<script>
const parent = document.getElementsByTagName('head')[0];
const script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.1.1/iframeResizer.min.js';
script.charset = 'utf-8';
script.onload = function() {
    window.iFrameResize({}, '.liquidTag');
};
parent.appendChild(script);
</script>    

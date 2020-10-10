---
title: 'Vim to the rescue: Subduing the Shell'
date: '2020-05-26T15:21:08.088Z'
excerpt: >-
  Introduction   How many times have you ran a command on your terminal and copy
  pasted its ou...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--3xqVYQUI--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/kj1tcgo9jn3mxv72nx0m.png
comments_count: 1
positive_reactions_count: 6
tags:
  - vim
  - todayilearned
  - productivity
  - linux
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-subduing-the-shell-2500'
layout: post
---
## Introduction

How many times have you ran a command on your terminal and copy pasted its output to vim? Maybe you want to include some terminal output data, or maybe you want to create an issue on github by editing it in vim first. 

In this blog we will be learning how to get the output of shell commands in your current vim buffer. 

For reference, here is what we are going to achieve:


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=euwcDjaBOxI" style="border: 0; width: 100%;"></iframe>



## Getting the output of a script

* You can take the output of any shell script and paste it after your cursor position by using the following command:


```vimscript
" . means current line
:.! <shell_command>
```


* Additionally you can take your cursor to the position where the command output ends:


```vimscript
:r! <shell_command>
```


* The best part about this is that you can use the text inside your vim buffer and pass it through the command line. For example if your current buffer contains something like this:


```
My cow says:

cowsay "Hello, World"
```


You can go over to the cowsay command and press the following keys to get the output right in your buffer:


```vimscript
" passes the current line through a shell
:.!$SHELL
```


You will get an output like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/om9i6q9xkz9is80tm1yz.png)

* Not only this, you can take the text from any line and paste its output:


```vimscript
" takes the text in the 5th line as input
:5!$SHELL
```


## Mapping the madness

I have mapped 
`<Shift> + q`
 to the 
`.!$SHELL`
 command. So pressing the keybinding instantaneously returns the output of the current line when ran through a shell.


```vimscript
noremap Q !!$SHELL<CR>
```



*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-subduing-the-shell-2500)*


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

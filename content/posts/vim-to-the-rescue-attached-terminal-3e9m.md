---
title: 'Vim to the rescue: Attached Terminal'
date: '2020-05-14T11:08:24.204Z'
excerpt: >-
  Introduction   I was recently working on some C++ code using vim and had to
  switch to a term...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--S_0UlAuQ--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--nVH8keJQ--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/b2ddkf07dthib4vwkm24.png
comments_count: 0
positive_reactions_count: 9
tags:
  - vim
  - todayilearned
  - tutorial
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-attached-terminal-3e9m'
layout: post
---
## Introduction

I was recently working on some C++ code using vim and had to switch to a terminal to compile the code everytime I wanted to test it. Granted that this problem can be solved by installing a plugin which compiles on save, but I wanted an intuitive attached terminal instead.

The problem with terminals inside vim is that they open either in a new tab or in a new split pane. By default, a terminal in vim looks like this:


```
:term
```


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/z558w3qtckhz53yy92sc.png)

---

## What can be better

In the screenshot above, there are a few problems:

* The split pane is too big, and occupies half of the screen
* You have to enter a command everytime you want a terminal, it is slow
* The split pane opens up in the top part of the screen by default

---

## What we want to achieve

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zcusgrmeti1vp8fvqmkd.png)

The benefits we get here are:

* The terminal opens at the bottom (like it should)
* The size of the attached terminal is ideal
* The whole action is bound to a key, so it is fast

To configure your attached terminal this way, you can add the following lines in your **.vimrc**:


```vimscript
" SpawnTern function
" To add a terminal at the bottom
function SpawnTern()
	" spawn terminal below
	bel term

	" Decrease split size by 15 words
	15winc -
endfunction

" We bind the control+x keys to spawn the terminal
noremap <c-x> :call SpawnTern()<CR>
```


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-attached-terminal-3e9m)*


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

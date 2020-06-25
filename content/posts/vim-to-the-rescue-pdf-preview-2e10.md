---
title: 'Vim to the rescue: PDF Preview'
date: '2020-06-01T12:07:33.190Z'
excerpt: >-
  Introduction   Some time ago, I was writing my resume. People suggested
  writing it in LaTeX....
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--Mk6Wc8xf--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--SkBVlTSu--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/cgl903ugf8afzvixj6t1.png
comments_count: 0
positive_reactions_count: 7
tags:
  - vim
  - todayilearned
  - tutorial
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-pdf-preview-2e10'
layout: post
---
## Introduction

Some time ago, I was writing my resume. People suggested writing it in [LaTeX](https://www.latex-project.org/get/). So I started reading up on it. Then I stumbled upon a tool called [groff](https://www.gnu.org/software/groff/) and found it much easier, faster and less bloat than LaTeX. 

Both of these tools are used to write documents that can be converted into PDFs. I wanted a solution in vim so that I could live preview these PDFs as I was writing them. So I decided to make a vim plugin that does so:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=L04DB4L4NC3R%2Ftexgroff.vim" style="border: 0; width: 100%;"></iframe>


It supports LaTeX, groff, as well as markdown.

---

## What we are going to use

* **Zathura**: It is a very minimalist PDF reader for vim users.
* **Groff**: The GNU document parser. It is installed by default on most linux systems
* **Pandoc**: It is the general purpose document conversion tool. See my blog on pandoc:


<iframe class="liquidTag" src="https://dev.to/embed/link?args=https%3A%2F%2Fdev.to%2Fl04db4l4nc3r%2Fpresentable-dev-posts-with-pandoc-56pc" style="border: 0; width: 100%;"></iframe>


All of these tools are already available in most official linux repositories and can be downloaded using your vanilla packet manager:


```sh
sudo apt install groff pandoc zathura
```


On Arch based distros, 
`zathura-pdf-poppler`
 needs to be downloaded in addition. 

---

## What we want

We want that the 
`\ + q`
 keybinding to compile the document we are working on into a PDF and the 
`\ + p`
 keybinding to preview the PDF in zathura after compiling it.



```sh
# Compiling Markdown to PDF:
pandoc curr.md -s -o /tmp/op.pdf

# Compiling LaTeX to PDF: 
pandoc -f latex -t latex curr.tex -o /tmp/op.pdf

# Compiling Groff (ms macro) to PDF:
groff -ms curr.ms -T pdf > /tmp/op.pdf
```


---

## Getting to the vim script

The following code divides the process into 2 functions, namely 
`Compile`
 and 
`Preview`
. The former checks our current file type and applies the appropriate compilation command to it. The latter opens up the output PDF in zathura. Add the following code in your **~/.vimrc**:



```vimscript
let mapleader="\\"

" Call compile
" Open the PDF from /tmp/
function! Preview()
		:call Compile()<CR><CR>
		execute "! zathura /tmp/op.pdf &"
endfunction

" [1] Get the extension of the file
" [2] Apply appropriate compilation command
" [3] Save PDF as /tmp/op.pdf
function! Compile()
		let extension = expand('%:e')
		if extension == "ms"
				execute "! groff -ms % -T pdf > /tmp/op.pdf"
		elseif extension == "tex"
				execute "! pandoc -f latex -t latex % -o /tmp/op.pdf"
		elseif extension == "md"
				execute "! pandoc % -s -o /tmp/op.pdf"
		endif
endfunction

" map \ + p to preview
noremap <leader>p :call Preview()<CR><CR><CR>

" map \ + q to compile
noremap <leader>q :call Compile()<CR><CR>
```


When we press preview, our zathura instance opens up. Now the best thing about zathura is that it watches the opened file. So after you press preview for the very first time, you don't have to press it again. Simply compile to view the changes in the PDF. Here is what our extension looks like:


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=s4gVmJafKf0" style="border: 0; width: 100%;"></iframe>



*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-pdf-preview-2e10)*


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

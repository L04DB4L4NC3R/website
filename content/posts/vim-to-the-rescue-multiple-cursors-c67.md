---
title: 'Vim to the rescue: Multiple Cursors'
date: '2020-04-28T15:39:02.525Z'
excerpt: >-
  I have faced loads of situations where there is a large block of text which
  needs a particular action...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--cmMLwSAq--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/si56jzdixtyswfxasm7e.png
comments_count: 4
positive_reactions_count: 6
tags:
  - vim
  - tutorial
  - productivity
  - todayilearned
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-multiple-cursors-c67'
layout: post
---
I have faced loads of situations where there is a large block of text which needs a particular action performed per line. This can easily be done using a macro in vim. But when we use vim, we care about efficiency. So we will be seeing how it can be done by using the 
`visual block mode`
 in vim.

---

## Visual Block Mode

The visual block mode in vim is used to visually select multiple lines/block of text in vim and perform a certain action on it. This action can be anything ranging from an insertion to a deletion. This action is then reflected in each and every line of the block of text just like you would use multiple cursors in an IDE like VS Code. 

To activate visual block mode, press **Ctrl + v**. Now you can select lines horizontally/vertically by using the navigation keys:


```
[num]h|j|k|l
```


Once you select a block of text, you can press any of the vim's keybindings for performing actions on the block. For example, you can press **d** to delete the block.

---

## Line by line operation in visual block mode


To insert/delete text on a line-by-line basis, press **I** to go into insert mode in the visual block or **A** to go into append mode. Once you do that, It will deselect the block and take you to the top line. Perform your desired action there and press escape. This action will then be reflected in each and very line of the visual block.

![Visual Block Mode](https://dev-to-uploads.s3.amazonaws.com/i/lpue4p5js0b75czf5wk9.gif)

---

## Incrementing numbers in a list

Imagine that you have to make a long list of incremental numbers. What would you do? 

There is a very easy way to do this in vim using the visual block mode. Let us say we need to write numbers from 1 to 100. Follow the following steps:

* Write 1 and a newline and copy it a 100 times by typing: **y1j**. Now paste it a 100 times using **100p**.

* Go to the visual block mode **Ctrl + v** and select the number block from the second 1, using **99j**.

* Press **g** and then **Ctrl a**. The latter is used to increment numbers and the former makes sure that the global context of numbers in a visual block is realized.

![Increment Integers](https://dev-to-uploads.s3.amazonaws.com/i/egracmuld8fk04ftxyh5.gif)


---

## Indenting a block of code

A block of code can be effortlessly indented using the visual block mode. Select a block using **Ctrl + v** and the navigation keys. Then hit **>>** for right indentation and **<<** for left indentation.

The **o** button can be used to go to the other side of the selected text in visual block mode, in addition to using **$**. The latter will take you to the end of a line rather than the end of the highlighted block.

![Indentation](https://dev-to-uploads.s3.amazonaws.com/i/bsabv3fi8auf6nlx8275.gif)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-multiple-cursors-c67)*


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

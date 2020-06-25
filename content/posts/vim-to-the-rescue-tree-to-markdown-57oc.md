---
title: 'Vim to the rescue: Tree to Markdown'
date: '2020-04-24T10:55:26.533Z'
excerpt: >-
  The What   Recently, I was working on my competitive-coding skills to land a
  job. But like a...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--JSM756KR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/qd1hybdwsjbuob5raxq6.png
comments_count: 0
positive_reactions_count: 5
tags:
  - vim
  - tutorial
  - todayilearned
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-tree-to-markdown-57oc'
layout: post
---
## The What

Recently, I was working on my competitive-coding skills to land a job. But like a developer I was pushing each and every program that I made to GitHub. I wanted a way to list down all the files I made in my README.md file in a readable format. 

The **tree** command is a very useful utility to list out the hierarchy inside a project. My aim was to convert this hierarchial structure into a markdown list:

*Before*: 


```
.
├── arrays
│   ├── k-smallest-fastest.cpp
│   ├── k-smallest-using-set.cpp
│   └── rotate.cpp
```


*After*:


```md
* arrays
   * k-smallest-fastest.cpp
   * k-smallest-using-set.cpp
   * rotate.cpp
```


To see what we are going to make in detail, check this video out: 


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=FY23ah7wukM" style="border: 0; width: 100%;"></iframe>


---

### The How

Working with the hierarchy that we have, we need to perform a series of find and replace operations to get our output. The only challenge is that our symbols 
`| |-- --`
 are not utf-8 encoded. Which means that we cannot type them using our standard keyboard. So to search for these tags, we need to copy paste them.

![Flow](https://dev-to-uploads.s3.amazonaws.com/i/br8w2asvw4x1yduxebsc.png)

---

### Removing the left-most pipe

Now let us perform our first operation: 


```vim
:%s/│//
```


This will search for all 
`│`
 (which are in the left side of the hierarchy) and delete them. Now to type this command, you can copy paste the 
`│`
 character from your file, or you can directly go into the vim command line with 
`│`
 in your cursor and press 
`Ctrl + r + "`
 to paste it there, which is a more intuitive way of approaching the problem. We get this as our output:


```
.
|── arrays
   ├── k-smallest-fastest.cpp
   ├── k-smallest-using-set.cpp
   └── rotate.cpp
```


---

### Replacing the sub-element pipe with a star

To convert our hierarchy to a list, every sub-element needs to remain in the same position and have a * next to it. This can be achieved by replacing the 
`├──`
 character by a 
`*`
:


```vim
:%s/├──/*/
```


Our output now look like this:


```
.
* arrays
   * k-smallest-fastest.cpp
   * k-smallest-using-set.cpp
   └── rotate.cpp
```


---

### Replacing the last sub-element pipe with a star

Notice that the last sub-element still has the pipe character in front of it. It can be replaced by the following and subsequent output is given below:


```vim
:%s/└──/*/
```



```
.
* arrays
   * k-smallest-fastest.cpp
   * k-smallest-using-set.cpp
   * rotate.cpp
```


Are we done? Not quite. If you look at the produced output in a markdown previewer, you will notice that it does not render properly. Why?

That is because there are hidden unicode characters in this file which we need to replace by a space character. To show all whitespaces, you can run the following commands:


```vim
:set listchars=eol:$,tab:>-,trail:~,extends:>,precedes:<,space:␣
:set list

" to see unicode characters in the statusline
:set statusline=%b\ %B
```


This will yield the following output:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/crzmw3jczm7wfhopbse0.png)

Notice that in the statusline we can view the invisible character as 
`A0`
. We need to replace it by space, which can be easily done by:


```vim
:%s/\%u00a0/ /g
```


And voila, we have our output!

---

### Combining everything

In vim, the pipe (|) character can be used to pipe multiple find and replace commands. So everything we did here can be condensed to the following command:


```vim
:%s/│//|%s/├──/*/|%s/└──/*/|%s/\%u00a0/ /g
```


---

### What lies ahead

I have made a plugin called [treemd](https://l04db4l4nc3r.github.io/treemd.vim/) which maps some very easy keybindings for converting your tree buffer to a markdown list. There is a bonus keybinding for running the tree command with a specified depth, in the current directory and using it as a markdown list:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=L04DB4L4NC3R%2Ftreemd.vim" style="border: 0; width: 100%;"></iframe>


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-tree-to-markdown-57oc)*


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

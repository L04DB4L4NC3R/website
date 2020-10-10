---
title: 'Vim to the rescue: Repetition Made Easy'
date: '2020-04-26T09:20:41.388Z'
excerpt: >-
  The What   A month ago I was working on a script for sending bulk emails to
  the participants...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--5AnLp9lv--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/r7lfku98sagh61j9vfl5.png
comments_count: 2
positive_reactions_count: 11
tags:
  - vim
  - tutorial
  - todayilearned
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-repetition-made-easy-a8c'
layout: post
---
## The What

A month ago I was working on a script for sending bulk emails to the participants of an event. The plan was to load a JSON file with a list of emails and generate usernames for sending people a greeting email. But the file that was provided to me looked something like this (the emails have been changed of course):


```
abc@xyz.com
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
```


The format required for the script to work was JSON, with email and username as keys. The usernames were supposed to be generated from the string preceding the '@' symbol in the email. For example: the username for 
`abc@xyz`
 will be 
`abc`
.

*Expected output*: 


```json
[
  {
    "email": "abc@xyz.com",
    "username": "abc"
  },
  {
    "email": "def@uvw.com",
    "username": "def"
  },
  {
    "email": "ghi@rst.com",
    "username": "ghi"
  },
  {
    "email": "jkl@opq.com",
    "username": "jkl"
  },
  {
    "email": "mno@lmn.com",
    "username": "mno"
  }
]
```


---

## The How

Vim has a feature called 
`macros`
, which are essentially an array of subsequent functions that can be recorded and replayed at will. This task was repetitive. To do it by hand would have consumed a lot of time, since the list emails contained about 5,000 entries! Vim simplified the flow:

![Flow](https://dev-to-uploads.s3.amazonaws.com/i/g2xq9kc3fgda8mz3qmt8.png)

---

### Recording a Macro in Vim

In vim, a macro can be bound to a key, and can be recorded by pressing the **q** button. For example: **q + a** will record a macro in the key **a**. Now whatever functions you perform are being tracked. To stop recording, simply press **q** again.

This macro can now be played using 
`@a`
. To run it 5000 times just input:


```vim
5000@a
```


---

### Recording a macro for our purpose

Before recording our macro, enclose the file in square brackets (for making an array):


```
[
{CURSOR_HERE}
abc@xyz.com
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
]
```


Press 
`q + a`
 to start recording. Then input 
`{ "email": "`
:


```
[
{
"email: "{CURSOR_HERE}abc@xyz.com
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
]
```


Yank (copy) till the 
`@`
 symbol by typing: 
`y + f + @`
. Then append '",' to the end of the line using: 
`A + ",`
:


```
[
{
"email: "abc@xyz.com",
{CURSOR_HERE}
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
]
```


Now for adding our username, type 
`{"username": ""},`
 and come back between the quotes:


```
[
{
"email: "abc@xyz.com",
"username": "{CURSOR_HERE}" },
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
]
```


Remember we yanked the email (till @) earlier? Paste it by pressing **p** and remove the @ symbol using **x**. 


```
[
{
"email: "abc@xyz.com",
"username": "abc" },
{CURSOR_HERE}
def@uvw.com
ghi@rst.com
jkl@opq.com
mno@lmn.com
]
```


You can stop recording the macro now using **q**.

Now that we have made our JSON for the first email, we don't have to do anything else. Simply rerun the macro 5,000 times to format all the emails just like you formatted the first one to get this output:


```json
[
  {
    "email": "abc@xyz.com",
    "username": "abc"
  },
  {
    "email": "def@uvw.com",
    "username": "def"
  },
  {
    "email": "ghi@rst.com",
    "username": "ghi"
  },
  {
    "email": "jkl@opq.com",
    "username": "jkl"
  },
  {
    "email": "mno@lmn.com",
    "username": "mno"
  }
]
```


Don't know how many emails there are? Just enter a huge number for a macro to repeat, when it can't find the next line, it'll exit automatically. 

Here is a recording of the same:


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=FU8X60HZhSQ" style="border: 0; width: 100%;"></iframe>


---

### Fun facts about vim macros and registers

* You can create 26 macros, one for each letter of the alphabet.
* Each macro is stored in a register and can be accessed using the **"** symbol.
* To get the keystrokes of a macro 'a' in our current buffer, you can press: **" + a + p**, where '"' is the macro selector, 'a' is the register and 'p' specifies paste action.
* There are some default registers in vim:
  * Whenever you delete something, it is pasted in the '"' register (can be accessed by **""**)
  * Yanked text can be accessed using **"0** to **"9** registers, from latest to oldest.
  * **".** is a readonly register which stores the last inserted text
  * **"%** is a readonly register which stores the current file path
  * **"# ** is a readonly register which stores the name of the last edited file
  * **":** is a readonly register which stores the last executed command

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-repetition-made-easy-a8c)*


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

---
title: 'Monsterwm: 700 lines of pure beast'
date: '2020-05-21T04:07:59.806Z'
excerpt: >-
  Monsterwm is a dynamic tiling window manager forked from dminimalwm, which was
  inspired by dwm. It ha...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--WnPA-ykm--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--jVbh0DIS--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/58xuum6eiqvpto0h3bq4.png
comments_count: 2
positive_reactions_count: 28
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/monsterwm-700-lines-of-pure-beast-hl4'
layout: post
---
Monsterwm is a dynamic tiling window manager forked from **dminimalwm**, which was inspired by dwm. It has a lot of similarities with dwm and feels like home for people who have used suckless tools. Read my blog on dwm to get additional insight on this particular *WM*, but you don't *need* to do so to understand this window manager:


<iframe class="liquidTag" src="https://dev.to/embed/link?args=https%3A%2F%2Fdev.to%2Fl04db4l4nc3r%2Fdwm-the-suckless-window-manager-1ji" style="border: 0; width: 100%;"></iframe>


Monsterwm aims to keep its codebase under 700 SLOC (source lines of code), as compared to dwm's 2000 SLOC limit. It does so by removing the status bar altogether. It believes that the status bar should not be the responsibility of a window manager. 

* [Features](# features)
* [Setting up](# setting-up)
* [Layouts](# getting-started)
* [Configuration and patching](# configuration-and-patching) 
  * [The monsterwm source](# the-monsterwm-source)
  * [Changing keybindings](# changing-keybindings)
  * [Installing patches](# installing-patches)
  * [Setting up a status bar](# setting-up-a-status-bar)
* [Verdict](# verdict)
* [References](# references)

---

### Features

* Monsterwm is only a single binary, and its source code is intended to never exceed 700 SLOC.

* Customization is done by editing the source code, which is very easy to understand.

* It is extremely fast and packed with bare essentials. Additional layouts and functionalities can be added by patching, as is the suckless anti-bloat philosophy. 

* It does not ship with a status bar, but outputs information about the desktop which external panels (like conky, dzen etc) can use. 

---

### Setting Up

Execute the following commands to get started with monsterwm:


```sh
# clone the source repository
git clone https://github.com/c00kiemon5ter/monsterwm.git

# enter the directory
cd monsterwm

# run a clean installation
make clean install
```

Now simply add the following line in your 
`~/.xinitrc`
:


```sh
exec monsterwm
```


Now that you are all set, logout and log back in again. Once you do, you will see a blank screen. 



---

### Layouts

To spin up a terminal in monsterwm, just press the following: 
`<Alt> + <shift> + <Enter>`
. If it doesn't work then checkout the [changing keybindings](# changing-keybindings) section where I talk about remapping the key bindings and customizing which terminal should open up. 

If you keep on opening terminals up then you will notice that the focus shifts to the newest terminal in the stack. A stack is a LIFO (last in first out) data structure. Monsterwm makes sure that the most attention goes to the recently opened program. 

Monsterwm has the following layouts by default:

* **Common tiling mode**: It is like the master and stack layout in dwm. The master comes on the left hand side. The focus is shifted to the newest spawn by default:


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/cxmelyl9kebsh3c5i23w.png)

* **Bottom stack (bstack) tiling mode**: Here, the newly spawned windows are stacked in the bottom:


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/l448xy0fhqyh7rm1ju6c.png)

* **Grid tiling mode**: In grid mode, each window is given an equal amount of space and thus windows tile themselves like a grid:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/um5tl0p2rk90ypsz98pv.png)

* **Floating mode**: In addition to tiling modes, windows can also be made to float over each other: 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/l7dupghmt6rdpa81v5km.png)

* In addition to these modes, monsterwm also has a monocle or fullscreen mode. Additional modes  (like fibionacci mode) can be added by patching, which we will se in the upcoming section. 


---

### Configuration and Patching

Configuring and patching monsterwm might be difficult for beginners. The source code configuration file is similar to dwm, so if you have used dwm, then monsterwm will be even easier. 

---

#### The Monsterwm Source

Using your terminal, go to whichever folder you have cloned monsterwm in and type 
`ls`
.

You may notice the configuration files in the directory.


`config.h`
 and 
`config.def.h`
 are the files that you will need to edit when you are configuring monsterwm.

Open the Makefile and edit clean recipe to add the following line of code in it:


```
rm config.h
```


This will make sure that whenever you are configuring a patch, you won't have to make changes in both 
`config.h`
 as well as 
`config.def.h`
. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9tliwavtmbrcebp5x81n.png)

Now whenever you make a change in the 
`config.def.h`
, simply run 
`make clean install`
 for re-building monsterwm from scratch. Then logout and log back in again for the changes to take effect. Monsterwm requires its source to be rebuilt every time there is a configuration change, which is exactly like dwm.

---

#### Changing Keybindings

Open the 
`config.def.h`
 in vim.


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ut7p8x07amc81dks4x6t.png)

The 
`Key_key`
 array stores all of the keybindings. The modifier key (<Alt> by default) is named 
`MODKEY`
. Shift is called 
`ShiftMask`
. All other keys are prefixed by 
`XK_`
. For example, if I am talking about the "i" key then I will write 
`XK_i`
. If I am talking about <Enter> then I will write 
`XK_Return`
. 

Now let us look at line 3, where the keybinding for opening up a terminal is defined. By default, this line is the following:


```
/* modifier            key       function        argument */
MODKEY|ShiftMask     XK_Return    spawn         {.v = termcmd}
```

It means that for 
`spawning`
 a terminal, you would have to hit 
`<Alt> + <Shift> + <Enter>`
. You can already see in the screenshot above, that I have removed 
`ShiftMask`
 from this line. So for opening up the terminal I simply do 
`<Alt> + <Enter>`
. 

In this way, by changing the modifier or keys, you can define custom keybindings. You can even add lines here to define some of your own keybindings. 

Now for the changes to take effect, simply compile the code again by running the following commands, log back in, and you are good to go:


```
make clean install
```


---

#### Installing patches

Some extensions to monsterwm are supported in the form of patches. Easiest way to apply a patch, is to git merge that branch. Here is a list of patches for monsterwm:


 * [centerwindow]   : center new floating windows on the screen and  center any window with a shortcut
 * [fibonacci]      : adds fibonacci layout mode
 * [initlayouts]    : define initial layouts for every desktop
 * [monocleborders] : adds borders to the monocle layout
 * [nmaster]        : adds nmaster layout - multiple master windows for BSTACK and TILE layouts
 * [rectangle]      : draws only a rectangle when moving/resizing windows to keep resources low (ie through an ssh forwarded session)
 * [showhide]       : adds a function to show and hide all windows on all desktops
 * [uselessgaps]    : adds gaps around every window on screen
 * [warpcursor]     : cursors follows and is placed in the center of the current window
 * [windowtitles]   : along with the rest desktop info, output the title of the current window

  [centerwindow]:   https://github.com/c00kiemon5ter/monsterwm/tree/centerwindow
  [fibonacci]:      https://github.com/c00kiemon5ter/monsterwm/tree/fibonacci
  [initlayouts]:    https://github.com/c00kiemon5ter/monsterwm/tree/initlayouts
  [monocleborders]: https://github.com/c00kiemon5ter/monsterwm/tree/monocleborders
  [nmaster]:        https://github.com/c00kiemon5ter/monsterwm/tree/nmaster
  [rectangle]:      https://github.com/c00kiemon5ter/monsterwm/tree/rectangle
  [showhide]:       https://github.com/c00kiemon5ter/monsterwm/tree/showhide
  [uselessgaps]:    https://github.com/c00kiemon5ter/monsterwm/tree/uselessgaps
  [warpcursor]:     https://github.com/c00kiemon5ter/monsterwm/tree/warpcursor
  [windowtitles]:   https://github.com/c00kiemon5ter/monsterwm/tree/windowtitles

Let us install the **fibonacci** layout. For doing so, simply run the following commands in the source repository:


```sh
git merge origin/fibonacci
make clean install
```


After doing so, simply restart the window manager. Look in the config.def.h for the changes added (as well as the keybinding). Activating this patch will make your windows spawn like a spiral:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k25ofxw8wzalwqwpxyyg.png)

---

#### Setting up a status bar


Monsterwm does not support a status bar but allocates (by default) 18 pixel on the top part of the screen for a custom status bar. This allocation is of course customizable. Whenever we run **monsterwm**, it outputs the workspace information as a stream. This stream can then be piped and the output can be shown to a terminal. In the following case, I am outputting the monsterwm to a temporary file. Let us name this file **startup.monsterwm**


```sh
# !/bin/bash

monsterwm > /tmp/monsterwm.fifo
```


In my 
`.xinitrc`
, I will add the following, instead of executing monsterwm directly:


```
exec startup.monsterwm
```


Now when my monsterwm is up and running, let us switch workspaces and see the terminal output by 
`catting`
 the file in which we are piping our output:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/94gedxgloeik3gni4c0m.gif)

You can see that it outputs real time information such as which monitor is being used, as well as how many windows are open per desktop. We can use this output as an input to dzen to show a status bar like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/5p86km1unfg4m7tgp2de.png)

Check out [these gists](https://gist.github.com/c00kiemon5ter/1905427) for some ready made scripts for setting up status bars. Copy any script you like to a file, and exec that in your 
`.xinitrc`
. 


---

### Verdict

For those of you who thought dwm was minimal, monsterwm goes one step ahead to ensure a separation of concern between a window manager and its status bar, stripping down a lot of code in the process. It is one of the most lightweight and fast window managers. 

Monsterwm is difficult to configure than your traditional window manager (like awesome or i3). But its patches are stable and do not break with monsterwm versions (ahem ahem dwm). Documentation can come from multiple sources since its configuration is almost exactly like dwm.

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: |
| Learning curve (lesser is better)| :heart: :heart: :heart: :heart: |
| Productivity | :heart: :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: :heart: :heart: |

---

### References

* [Suckless Philosophy](https://dev.to/l04db4l4nc3r/what-is-suckless-all-about-4hp)
* [Official Repository](https://github.com/c00kiemon5ter/monsterwm)
* [My configuration](https://github.com/L04DB4L4NC3R/monsterwm-config)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/monsterwm-700-lines-of-pure-beast-hl4)*


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

---
title: 'Dwm: The Suckless Window Manager'
date: '2020-04-07T11:34:24.237Z'
excerpt: >-
  Dwm stands for Dynamic Window Manager. It is a minimalist tiling window
  manager designed specifically...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--GNkAtaRI--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/ojr5tt2ix60zi0r9v13m.png
comments_count: 0
positive_reactions_count: 18
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/dwm-the-suckless-window-manager-1ji'
layout: post
---
Dwm stands for *Dynamic Window Manager*. It is a minimalist tiling window manager designed specifically for X11. It is designed to be much smaller, faster and simpler than its alternatives. 

The Suckless community claims that dwm's code is never intended to exceed 2000 SLOC (source lines of code). For those of you who are not familiar with the suckless philosophy, check out my blog on the same:


<iframe class="liquidTag" src="https://dev.to/embed/link?args=https%3A%2F%2Fdev.to%2Fl04db4l4nc3r%2Fwhat-is-suckless-all-about-4hp" style="border: 0; width: 100%;"></iframe>


Dwm, like other suckless tools, is meant for the *elitist*, and suckless makes sure of that. There is no binary distribution of dwm. It is just a source file which you have to compile manually to get started. Customization requires editing the source directly and building it from scratch (which is easier than it looks, up ahead). 

* [Features](# features)
* [Setting up](# setting-up)
* [Getting started](# getting-started)
* [Tags](# tags)
* [Windows](# windows)
* [Dmenu](# dmenu)
* [Configuration and patching](# configuration-and-patching) 
  * [The dwm source](# the-dwm-source)
  * [Changing keybindings](# changing-keybindings)
  * [Installing patches](# installing-patches)
* [Verdict](# verdict)
* [References](# references)

---

### Features

* Dwm is only a single binary, and its source code is intended to never exceed 2000 SLOC.

* Customization is done by editing the source code, which is very easy to understand.

* It uses a stack based system for managing windows, where the *top* of the stack is the master and the other windows are slaves.

* It is extremely fast and packed with bare essentials. Additional layouts and functionalities can be added by patching, as is the suckless anti-bloat philosophy. 

---

### Setting Up

Execute the following commands to get started with dwm:


```sh
# clone the source repository
git clone git://git.suckless.org/dwm

# enter the directory
cd dwm

# run a clean installation
make clean install
```


And you are good to go. As of Q1 2020, dwm 6.2 is the latest version. Now simply add the following line in your 
`~/.xinitrc`
:


```sh
exec dwm
```


Now that you are all set, logout and log back in again. Once you do, you will see a blank screen with numbers on top. The screen is going to have your wallpaper on it by default. Something like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/hvrsvoibnjff21bdfw01.png)



---

### Getting Started

To spin up a terminal in dwm, just press the following: 
`<Alt> + <shift> + <Enter>`
. If it doesn't work then checkout the [changing keybindings](# changing-keybindings) section where I talk about remapping the key bindings and customizing which terminal should open up. 

If you keep on opening terminals up then you will notice that the focus shifts to the newest terminal in the stack. A stack is a LIFO (last in first out) data structure. Dwm makes sure that the most attention goes to the recently opened program. You can choose between a lot of different layouts from dwm patches. The one I like to use is [centeredmaster](https://dwm.suckless.org/patches/centeredmaster/), which keeps the master terminal in the center of the screen.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/itbd2r3wn3eugbr1fagf.png)

If you want more than one master then you can even promote and demote master panes. 
`<Alt> + i`
 is used to promote the master and 
`<Alt> + d`
 is used for demoting it. Here is as example of two windows selected as master:
 
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/n2qvz4feapaot2pnsqp4.png)


---

### Tags

Notice that the top bar has a few numbers, starting from 1 to 9. These numbers are tags (workspaces) that we can switch between. To do so, simply hit 
`<Alt> + [1-9]`
. For example 
`<Alt> + 6`
 will take me to the 6th tag. Note that whatever was running on the previous tag keeps on running there as usual. The highlighted numbers indicate that there is something running on those tags.

You can move windows from to and from one or more tags. For example, for moving a window in tag 1 to tag 9, press the following commands in tag 1: 
`<Alt> + <Shift> + 9`
. 

To view all of the windows running in all of the tags at once, press 
`<Alt> + 0`
. Tags are a very powerful way to switch between programs and view multiple programs at once. 

---

### Windows

Dwm is feature rich when it comes to managing windows, and has a lot of solutions to complex problems such as fixing a tag on all screens, promoting windows to master and demoting them to slaves.

| Default key binding | Action performed |
|:-------------------:|:----------------:|
| 
`<Alt> + [h/j/k/l]`
| Move left-right-up an down windows |
| 
`<Alt> + r`
| Terminate current window |
| 
`<Alt> + <Shift> + c`
| Terminate the process running in the current window | 
| 
`<Alt> + <Shift> + q`
| Logout |
| 
`<Alt> + <Shift> + [1-9]`
 | Re-locate the current window to another tag |
| 
`<Alt> + <Shift> + 0`
 | To fix the current tag on all tags |
| 
`<Alt> + p`
 | To spin up [dmenu](# dmenu) |
| 
`<Alt> + i`
 | Promoting current window to master |
| 
`<Alt> + d`
 | Demoting current window to slave |


The default super (called a modifier in dwm, or Mod), 
`<Alt>`
 can be changed by editing the configuration.

---

### Dmenu

Dmenu is a toolbar menu which can be used for easy access of programs. Simply press 
`<Alt> + p`
 to activate the menu, then type in the name of the program you want to execute. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bgf4oet4aqwjgudujitv.png)

Note that you do not have to have dwm to get dmenu. You can independently install it either by building it from source, or running the following command:


```
sudo apt install dmenu
```


I started off with dmenu along with herbstluftwm, but now I use dmenu in very single window manager that I use.

You can even pass in arguments to programs using dmenu. Simply press spacebar after writing the name of the program you want to execute, then subsequently write the arguments that you want to pass in to the program.

---

### Configuration and Patching

Configuring and patching dwm might be difficult for beginners. I will try to make it as simple as I can by taking two examples:

* Changing the default keybinding of the terminal.
* Installing [centeredmaster](https://dwm.suckless.org/patches/centeredmaster/) layout patch.

---

#### The Dwm Source

Using your terminal, go to whichever folder you have cloned dwm in and type 
`ls`
.

You may notice three configuration files in the directory. 
`config.mk`
 contains the build configuration. You won't have to touch it in the best case scenario. 


`config.h`
 and 
`config.def.h`
 are the files that you will need to edit when you are configuring dwm. I suggest making the configuration changes on a different branch:


```
git checkout -b patches
```


Once you are on a different branch, open the Makefile and edit clean recipe to add the following line of code in it:


```
rm config.h
```


This will make sure that whenever you are configuring a patch, you won't have to make changes in both 
`config.h`
 as well as 
`config.def.h`
. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/3447dplff0092rlco0au.png)

Now whenever you make a change in the 
`config.def.h`
, simply run 
`make clean install`
 for re-building dwm from scratch. Then logout and log back in again for the changes to take effect. Dwm requires its source to be rebuilt every time there is a configuration change, which is unlike other window managers like herbstluftwm and i3, where you can simply reload the configuration at runtime.

---

#### Changing Keybindings

Open the 
`config.def.h`
 in vim.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/16gmz9rfyx8xl6aza003.png)


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

Now by default dwm uses 
`st`
 (simple terminal) when someone hits the keybindings for opening the terminal up. That is why your terminal might not open up the first time you hit the default key binding for doing so (if st is not installed). However this can easily be changed to suit the terminal of your choice by simply editing the argument 
`termcmd`
 definition. Since I use 
`terminator`
, I have changed it like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bjjl3c5zfkun5lpjhnrt.png)

Now for the changes to take effect, simply compile the code again by running the following commands, log back in, and you are good to go:


```
make clean install
```


---

#### Installing patches

In this example, I will be installing the [centeredmaster](https://dwm.suckless.org/patches/centeredmaster/) patch. Download its source code and place it in the dwm directory. 

Patches in dwm are tagged commit diffs in the upstream repository of the version control system. Therefore, for apply patches, you have to use git:


```
git apply dwm-centeredmaster-6.1.diff
```


Once you do that, it will make changes in the dwm source code. Simply commit after doing so. Once the patch is successfully applied, build dwm again by running 
`make clean install`
, logout and log back in again to see the changes in effect.

To activate 
`centeredmaster`
, hit 
`<Alt> + u`
. This way patches and different layouts can be installed for dwm. 


---

### Verdict

Dwm is an easy to use but hard to configure window manager, especially for beginners. It has a lot of useful patches which feel like they should've been shipped dwm source itself. The main drawback is the need to compile the source and log back in again after a change in configuration. Except for that, dwm is a really fun to use window manager. It is extremely fast, feature rich, and powerful. 

Now some of the patches in dwm might not work out of the box. This is primarily due to the fact that you might have a version which is not yet supported by the patch. But the developer community is always doing changes on those patches. All in all, patching your own dwm configuration is a rewarding process.

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
* [Official Website](https://dwm.suckless.org/)
* [List of Patches](https://dwm.suckless.org/patches/)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/dwm-the-suckless-window-manager-1ji)*


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

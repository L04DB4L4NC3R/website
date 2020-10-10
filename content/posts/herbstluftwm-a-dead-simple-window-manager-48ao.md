---
title: 'Herbstluftwm: A Dead Simple Window Manager'
date: '2020-04-05T12:28:16.786Z'
excerpt: >-
  Herbs.....what? How do you even begin to pronounce this window manager? After
  some digging, it is app...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--R6O_E5JP--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/ks36wotkultqmuyt7mw9.png
comments_count: 10
positive_reactions_count: 56
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/herbstluftwm-a-dead-simple-window-manager-48ao'
layout: post
---
Herbs.....what? How do you even begin to pronounce this window manager? After some digging, it is apparently pronounced as the following: *herbs + laugh + umm*. And this is the version that makes the most sense! As to why it is named so:

> I liked the name of the e-mail client wanderlust. Unfortunately I am a happy mutt user, so I needed an other application with a similar name.
> - the creator of herbstluftwm

Nevertheless, herbstluftwm is one of the easier window managers to get started with. The following is an index to help you navigate this blog easier:

* [Features](# features)
* [Setting up](# setting-up)
* [Getting started](# getting-started)
* [Tags](# tags)
* [Windows](# windows)
* [Herbstclient](# herbstclient)
* [Configuration](# configuration)
* [Verdict](# verdict)
* [References](# references)

---

### Features

* It is made for X11.
* The layout is based on splitting frames to sub-frames.
* Each screen (workspace) is called a tag, which has a unique identifier. Switching between tags is seamless.
* It can be configured during runtime. Which means that any customization made does not require the service to be restarted.
* *herbstclient* is the frontend for herbstluftwm, which can be used to issue commands to the server during runtime.

According to the herbstluftwm wiki, it functions in the following way:



```
                 startx
                   | f/e
                   V
              ~/.xinitrc
                   | f/e or exec
    IPC-Call       V
    .- - - -> herbstluftwm           __________________
  ."            /     \             | Symbol | Meaning |
  .            /       \            |--------+---------|
  .       f/e /         \ f/e       |  A     | A forks |
  .          /           \          |  | f/e | and     |
  .         V             V         |  V     | execs   |
  .     autostart       xterm       |  B     | into B  |
  .         |             |         |________|_________|
  .     f/e |             | f/e
  .         V             V
   --  herbstclient     $SHELL

```


In the [last blog](https://dev.to/l04db4l4nc3r/the-linux-desktop-deep-dive-1jh3), we understood that 
`startx`
 loads the display manager, which in turn loads the *.xsession* and *.xinitrc* scripts to configure the X Client, which is herbstluftwm in this case. When started, it runs the 
`~/.config/herbstluftwm/autostart`
 script to load all of the configurations.


---

### Setting Up

Herbstluftwm is very easily to install, and will most likely have an installation candidate for your distribution. 


```
sudo apt install herbstluftwm
```

To run it, simple add the following line in your 
`~/.xsession`
 file:


```
exec herbstluftwm
```


Logout and log back in again, and boom! You are good to go.

---

### Getting Started

Herbstluftwm then gives us access to spawn terminals using the default 
`<Alt> + <Enter>`
 command. 

When we do that for the first time, the screen looks something like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4chlpdvnd9r5ifscdhid.png) 

---

### Tags

Notice that the top bar has a few numbers, starting from 1 to 9. These numbers are tags (workspaces) that we can switch between. To do so, simply hit 
`<Alt> + [1-9]`
. For example 
`<Alt> + 6`
 will take me to the 6th tag. Note that whatever was running on the previous tag keeps on running there as usual. The highlighted numbers indicate that there is something running on those tags.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/sa5cqrd0bwwnagu003xb.png)

---

### Windows

Herbstluftwm uses a lot of vim bindings for navigation. Here are some of the default key bindings for splitting windows and navigating:

| Default key binding | Action performed |
|:-------------------:|:----------------:|
| 
`<Alt> + o`
| Split window horizontally |
| 
`<Alt> + u`
| Split window vertically |
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
`<Alt> + <Ctrl> + [h/j/k/l]`
| Resize the window |
| 
`<Alt> + <Shift> + q`
| Logout |
| 
`<Alt> + <Shift> + r`
| Re-load configuration |
| 
`<Alt> + <Shift> + [1-9]`
 | Re-locate the current window to another tag |


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2ub3uhra4xaxlrdiqcl9.png)

Here the default super (called a modifier in herbstluftwm, or Mod) 
`<Alt>`
 can be changed by editing the configuration.

---

### Herbstclient

The only way to communicate with herbstluftwm is by using herbstclient, which is a command line utility for inter-process communication with the *WM* server. To see the list of available commands, run:


```
herbstclient --help
```


It is a very powerful tool. In fact, the 
`autostart`
 file we mentioned earlier, has a lot of key bindings mapped to herbstclient commands. A simple example of how we can use herbstclient is:


```
herbstclient spawn firefox
```


This command will talk to the herbstluftwm backend to launch an instance of firefox in the current tag. 

To learn more about how to use the client, go to the [tutorial](https://herbstluftwm.org/tutorial.html# client).

---

### Configuration

All of the herbstluftwm configuration lies in 
`~/.config/herbstluftwm/autostart`
. This file can be edited for some of the following functionalities:

* Adding keybindings.
* Configuring colours and themes.
* Changing the modifier key (<Alt> by default).
* Configuring titlebar, borders, frame width etc.

And much much more. A simple example is the following:


```
hc keybind $MOD-b spawn firefox
hc keybind $MOD-n spawn nautilus
```

Here, 
`hc`
 is an alias for herbstclient, and $Mod is <Alt>. This configuration essentially enables me to spin up firefox on hitting 
`<Alt> + b`
 and the file manager nautilus on hitting 
`<Alt> + n`
.

The best part about herbstluftwm is that after changing the configuration, you don't have to logout to re-compile the program. Simply pressing 
`<Alt> + <Shift> + r`
 will reload the configuration with the changes made!

---

### Verdict

Herbstluftwm is very easy to get started with. It has the capability to load the configuration during runtime, has a sophisticated client, and is extremely fast due to minimalism. I would recommend it to anyone who is getting started with window managers.

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: :heart: :heart: |
| Learning curve (lesser is better)| :heart: :heart: |
| Productivity | :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: :heart: |

---

### References

* [Tutorial](https://herbstluftwm.org/tutorial.html)
* [Official Website](https://herbstluftwm.org/)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/herbstluftwm-a-dead-simple-window-manager-48ao)*


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

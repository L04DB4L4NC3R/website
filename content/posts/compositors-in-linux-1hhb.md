---
title: Compositors in Linux
date: '2020-04-15T10:22:14.548Z'
excerpt: >-
  Compositors are a very important part of the aesthetics of any linux desktop
  environment. In this blo...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--9Jr59qdC--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/j7lww4t7wdnl66gzxcu4.jpg
comments_count: 3
positive_reactions_count: 16
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/compositors-in-linux-1hhb'
layout: post
---
Compositors are a very important part of the aesthetics of any linux desktop environment. In this blog, we will be looking at the following:

* [What are Compositors](# what-are-compositors)
* [How Compositors Work](# how-compositors-work)
* [When to use a Compositor](# when-to-use-a-compositor)
* [When NOT to use a Compositor](# when-not-to-use-a-compositor)
* [The Compton Compositor](# compton)
* [The Picom Compositor](# picom)
* [Configuring the Compositor](# configuring-the-compositor)
* [Useful Links](# useful-links)

---

### What are Compositors

A compositor is a software which interacts with the window system as well as graphics in linux to produce:

* Transparency in windows
* Transition animations
* Drop shadows around windows which give them a 3D effect
* V sync: Waits for the display to update before updating the display

With compositor:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2t30r5vqbamlg0zp1ltd.png)

Without compositor:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/64y2sjq4fq10id6cwu6n.png)

As you can see, using compositors in a linux desktop environment adds flavour to the aesthetics. Now let us see how they work.

---

### How Compositors Work

> The compositer causes an entire sub-tree of a window hierarchy to be rendered to an off-screen buffer. Applications can then take the contents of that buffer and do whatever they like. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7ejh54l4srsx6pxdmrlq.png)

The off-screen buffer can be automatically merged into the parent window or merged by external programs, called compositing managers. Maintaining a buffer like this makes it easy to add additional frames during a window state change, such as fade-in and fade-out animations. Each frame of each running application goes through the compositor.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/i3trco1aa9hv3cg53ehg.png)

---

### When to use a Compositor

A compositor should be used if there is a need of transparency, transition animations, v-sync and similar aesthetic features. Note that most desktop environments (like gnome) come with their own integrated compositors. Even some window managers like Compiz, Enlightenment, KWin, Marco, Metacity, Muffin, Mutter, Xfwm, do compositing on their own.

You would need to install a compositor separately if you are using a minimalistic desktop environment of window manager such as dwm, i3 or awesome. In such a case, since the environment is bare-bones (in the order of 1 to 5 megabytes), it is not shipped with a compositor off the shelf. In such cases, compositors like *compton* or *picom* can be used.

---

### When NOT to use a Compositor

The mechanism behind a compositor revolves around maintaining an off-screen buffer and passing that around different windows. While this might add a lot of effects to your window manager or desktop environment, it is NOT ideal during gaming, where it causes latency. 

While gaming, not using a compositor might lead to the lack of v-sync (unless you turn v-sync on in-game) and a lot of screen tearing, but it does away with latency between frames. I would recommend turning the compositor off while gaming. The drawbacks can be avoided if hardware V-sync is used, but it requires altering the X11 config for synchronization at a graphics driver level. Specifically, enabling the **ForceFullCompositionPipeline** option for use with nvidia graphics (and **TearFree** option in the case of Intel) . In such a case, the compositor would not have to be turned off while gaming since v-sync will be offloaded to the graphics driver instead of the compositor itself. This would of course require the v-sync in the compositor to be turned off.

--- 

### Compton

Compton is a light weight and standalone compositor for the X Window System. It is a fork of the *xcompmgr-dana* compositor, which in turn is a fork of the *xcompmgr* compositor.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ockleu4txe7ds0ugwfm.png)

In addition to xcompmgr-dana, it supports the OpenGL backend, as well as colored drop-shadows. It can be easily installed for your distribution using official repos. For debain it can be installed like this:


```sh
# install comption
sudo apt install compton

# run compton in the background
compton &
```


Compton can be added as a startup script for the window manager of your choice.

---

### Picom

Although compton is a pretty solid standalone compositor for X11 but sadly it is not regularly maintained anymore. Picom is an active fork of compton which aims to battle the code complexity of compton in order to draw more developers into contributing to the project.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/5gjftrz0u12rs9bjc5nf.png)

For getting started with picom, I recommend building it from source. For debain based systems, the following dependancies need to be installed and subsequently, the following commands can be used to build picom:


```sh
# Debian specific command. The next few commands are for all distros
sudo apt install libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev  libpcre2-dev  libevdev-dev uthash-dev libev-dev libx11-xcb-dev

# clone the project and go into it
git clone https://github.com/yshui/picom && cd picom

# Use the meson build system (written in python), to make a ninja build 
meson --buildtype=release . build

# Use the ninja build file to proceed
ninja -C build

# Copy the resultant binary into PATH
cp build/src /usr/local/bin

# Run picom in the background (this command can be added to the autostart)
picom & 
```


---

### Configuring the Compositor

Compositors like compton and picom are highly configurable. From customized colored drop shadows, to the amount of transparency can be set both globally, and for certain windows in specific.

A sample config for picom can be found in 
`/etc/xdg/picom.conf`
. [Here](https://github.com/yshui/picom/blob/next/picom.sample.conf) is a copy of the same. To get started, simply copy the configuration to 
`~/.config/picom/picom.conf`
.


```sh
cp /etc/xdg/picom.conf ~/.config/picom/
vim ~/.config/picom/picom.conf
```


All of the available options are mentioned in the comments. After making a change, simply edit the configuration and save. The compositor will reload automatically. 

To add a compositor to your window manager, simply put the following line in your 
`~/.xsession`
:


```sh
# Start compositor in the background
picom & # or compton & (in case you want to use compton)

# Execute window manager
exec awesome
```


---

### Useful Links


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Fyshui%2Fpicom" style="border: 0; width: 100%;"></iframe>



<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Fchjj%2Fcompton" style="border: 0; width: 100%;"></iframe>


[Picom Configuration](https://wiki.archlinux.org/index.php/Picom# Configuration)

[Offloading V-sync to the nvidia graphics](https://wiki.archlinux.org/index.php/NVIDIA/Troubleshooting# Avoid_screen_tearing)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/compositors-in-linux-1hhb)*


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

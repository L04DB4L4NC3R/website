---
title: 'InstantWM: Animations in a Window Manager!'
date: '2020-10-08T13:29:24.354Z'
excerpt: >-
  InstantWM is a window manager to InstantOS, which is an Arch-Linux based
  operating system that aims t...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--fc08k5ty--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/0yxz2ohhis98yv0gxc95.png
comments_count: 0
positive_reactions_count: 2
tags:
  - linux
  - tutorial
  - opensource
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/instantwm-animations-in-a-window-manager-48f4'
layout: post
---
InstantWM is a window manager to **InstantOS**, which is an Arch-Linux based operating system that aims to work right out of the box and also cater to power users. It went through a lot of scrutiny and controversy in it's development process, primarily due to faulty reviews from a particular youtuber ([distrotube](https://www.youtube.com/channel/UCVls1GmFKf6WlTraIb_IaJg)). 

The developer subsequently [released a video](https://youtu.be/XTjAO3yUqpQ) with some bugs either excavated, or altogether nullified by the faulty review. When the smoke settled, people started reviewing InstantOS, but no one has really made a standalone review of **InstantWM**, which is the window manager that the OS uses, and can be installed on any distribution. I feel like this window manager deserves its own "series" of reviews.


---

### First Impressions

I usually start my reviews with features and the installation procedure, but for this particular WM, I felt that a first impressions review is necessary due to the underlying controversy. 

> It is the best and the most versatile window manager I have used in a while

Considering I have used stable and extendible WMs such as xmonad and i3, instantWM bring a lot to the table. On first glance, it looks like a [dwm](https://dwm.suckless.org/) fork. That is because it is, but only 40% of the suckless code is remaining in the instantWM repository.

It's versatility comes in the fact that it is both a tiling and a floating window manager. It has a menu like [awesome](https://awesomewm.org/), and you can even use it with a mouse instead of a keyboard, which makes it suitable for newcomers as well. It's modernity is in the fact that it is both minimal and fashionable at the same time, with it's attractive window animations and compsiting effects without sacrificing any functionality.

---

### Features

InstantWM is no joke. It is feature rich without sacrificing on functionality and usability. Some of its main features include.

* Patchless configuration (you don't have to manually patch things into the config)
* Modern window transition animations without sacrificing on speed
* Full multimedia and multimonitor support out of the box
* **Instantutils** offers a rich set of utilities for support
* Hybrid window manager (floating + tiling)
* Tag system reminiscent of dwm, with tag pinning support as well

---

### Installation

If you are coming from a *dwm* background, you can simply skip this section. 

You need to clone the instantWM repository and build it from source. This is the same way dwm works. Even the configuration is done in the code itself, and needs to recompile after every change.


```sh
git clone --depth=1 https://github.com/instantOS/instantWM.git
cd instantWM
./build.sh
```


These commands will generate a binary. You can then logout of your current DE or WM and login to instantWW, either using a [display manager](https://dev.to/l04db4l4nc3r/the-linux-desktop-deep-dive-1jh3# display-manager), or through changing your 
`~/.xinitrc`
 to say the following:


```sh
exec instantwm
```


Before logging into instantWM, you can download the **instantutils**, which are available in the linux source repositories. We will touch on what these utilities do later on.


```sh
# instantutils is available in the AUR
yay -S instantutils
```


InstantWM uses the [st](https://st.suckless.org/) terminal by default, so make sure you either have an st build or you change the configuration (
`termcmd`
) to point to another terminal.

---

### Tiling Modes

[The official web page](https://instantos.io/youtube/layouts# rundown-of-all-layouts) has a rundown of all instantWM layouts. Some high utility ones are:

**Grid Layout**

This layout arranges windows in a grid of equally sized windows.

![Grid Layout](https://dev-to-uploads.s3.amazonaws.com/i/dj23c0z4x8qo7m1qe69c.png)

**Centered Master**

One of m favourite layouts, centered master is a layout where the window at the center is the master and all other windows pop up on the left and right hand sides.

![Centered Master](https://dev-to-uploads.s3.amazonaws.com/i/6nr5wljsibvp84fpqgfj.png)

**Horizontal Stack Layouts - 1 and 2**

These are your traditional tiling modes but tiling is done either horizontally or vertically.

![TTT](https://dev-to-uploads.s3.amazonaws.com/i/hiheo2vnmaunwtaaceas.png)

![===](https://dev-to-uploads.s3.amazonaws.com/i/dzkz9uiyn94rwcl4qwz0.png)

**Overview**

This layout stacks windows in a way that each window is visible and is unchanged from its size in the previous layout.

![Overview Layout](https://dev-to-uploads.s3.amazonaws.com/i/b30fdkh5pyfne7vcuwik.png)

**Half Stack**

The master area is tiled normally, but the stack works like the monocle layout with all windows layered on top of each other.

![Half Stack](https://dev-to-uploads.s3.amazonaws.com/i/ej43e6mmkw8pdnp0c0dh.png)

Other layouts are:

* Floating
* Monocle
* Tiling Layout (Master and Stack)

---

### Overlay Windows

Have you ever played games where you get an overlay console when you press the tilde button, where you can enter commands? You can do the same thing to your windows in instantWM. 

![Overlay](https://dev-to-uploads.s3.amazonaws.com/i/r6ej5ro40sdgfhty8mds.png)


`super`
 + 
`control`
 + 
`w`
 overlays your current window on top of the other windows and essentially locks it in place so it cannot be accidentaly removed. You can then press the same keybinding to undo the action. This gives you a lot of power when you are developing as well as looking at documentation, or a manpage. You can [checkout available overlay animations](https://youtu.be/T40cfbBVBQw).

---

### Configuration

InstantWM can be configured the same way you configure *dwm*. If you haven't read my blog on how to configure dwm, you can give it a read here:


<iframe class="liquidTag" src="https://dev.to/embed/link?args=https%3A%2F%2Fdev.to%2Fl04db4l4nc3r%2Fdwm-the-suckless-window-manager-1ji" style="border: 0; width: 100%;"></iframe>


Or you can directly go into the [configuration section](https://dev.to/l04db4l4nc3r/dwm-the-suckless-window-manager-1ji# configuration-and-patching), to checkout how to tweak instantWM to your liking. 

**NOTE**: A key difference between InstantWM and dwm configuration is that instantWM does not have a patch and diff system like dwm, and additional has a 
`build.sh`
 script that you can run everytime you change a configuration.

---


### Multiple Monitor Support

I do not write about multiple monitor support a lot when I am doing my window manager reviews since the WMs that support this feature usually require 
`xrandr`
 commands to be run in order to set the display, but instantWM comes with an amazing utility for the same.

The moment you plug your external display in, an instantmenu pops up, asking if you want to mirror or extend your display out to the secondary display. This is a great feature that I hope more window managers incorporate.


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=cH2b7rz6xNU" style="border: 0; width: 100%;"></iframe>


You can easily switch between monitors and send current windows to the secondary display without leaving your keyboard, as shown in the video above.

---

### Conclusion

InstantWM and its instantutils can be easily downloaded and configured for any system and you don't necessarily have to have instantOS for the best experience. People in the WM community are used to using minimal and lightweight WMs which often compromise on aesthetics. It is great to see a window manager with a modern user experience that is still minimal enough to be installed and used on low power machines.

As of now (when this article was written), instantWM is still in beta and actively looking for contributors. I am glad to see that the developer is also building towards ARM and 32 bit support. I can recommend this window manager to beginners as well as power users due to its outstanding versatility.



| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: |
| Learning curve (lesser is better) | :heart: :heart: |
| Productivity | :heart: :heart: :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: :heart: :heart: |

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/instantwm-animations-in-a-window-manager-48f4)*


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

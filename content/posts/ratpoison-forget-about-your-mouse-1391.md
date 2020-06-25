---
title: 'Ratpoison: Forget About Your Mouse'
date: '2020-05-09T12:26:26.445Z'
excerpt: >-
  Ratpoison is an ambitious project that puts the GNU screen command as a first
  class citizen. This win...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--WlOxsDdB--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--4vXGQ74E--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/emsirdnlps64le81bdpb.png
comments_count: 2
positive_reactions_count: 4
tags:
  - linux
  - opensource
  - techtalks
canonical_url: 'https://dev.to/l04db4l4nc3r/ratpoison-forget-about-your-mouse-1391'
layout: post
---
Ratpoison is an ambitious project that puts the GNU screen command as a first class citizen. This window manager professes minimalism and makes sure that the user does not need a mouse at all, hence the name.

If you are an emacs user then you will feel more in home with this window manager. For all other users, this *WM* is a bit complicated to get used to, yet very easy to configure. 
 
* [Features](# features)
* [Setting up](# setting-up)
* [Layouts](# layouts)
* [Ratpoison Menu](# ratpoison-menu)
* [Frame Navigation](# frame-navigation)
* [Configuration](# configuration)
* [Verdict](# verdict)

---

### Features

* Ratpoison does not support window decoration, since it does not want you to use the mouse to manage windows. 
* Even though it's design philosophy does not put aesthetics in the highest regard, it has external compositor support (ahem ahem spectrwm).
* Each window takes up a complete frame, so menu bars like polybar and conky are not compatible (and not recommended). 
* The default keybindings are more like key-chords. They are emacs centric but use 
`Ctrl + t`
 as the top level modifier rather than 
`Ctrl + x`
 in emacs due to it leading to "key-clobbering". The maintainers feel that the current keybindings are sufficient and you don't have to change them to get the most out of ratpoison. 


---

### Setting Up

Ratpoison has a candidate for most distros. On debian it can be installed using 
`apt`
: 


```sh
sudo apt install ratpoison
```


After installing it, simply add the following line in your 
`~/.xinitrc`
, logout and log back in again:


```
exec ratpoison
```


After you login, it will just show a black screen with nothing on it. But you will see an info bar on the top right corner informing you of how to open the help and application menu. 

Press 
`Ctrl + t + ?`
 to view the keybindings. The best part about this list is that when you create your own bindings, you will be able to see them getting updated in this list.

Ratpoison has excellent documentation. Distributed on [it's official website](https://www.nongnu.org/ratpoison/) as well as it's man pages. An exhaustive list of default keybindings is given [here](https://www.nongnu.org/ratpoison/doc/Default-Key-Bindings.html# Default-Key-Bindings). 



---


### Layouts

Ratpoison is a tiling window manager and only supports 2 layouts: Horizontal and Vertical split. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ftwoaun2exe5892y4qi0.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/iwr4q3xtz22zajdrul9a.png)

Whenever you close a split, the windows get readjusted automatically. You don't have any control over how the adjusted layout will look like. So you are left wishing for the best result whenever you close a split. 

---

### Ratpoison Menu

Ratpoison has its own awesome-style application menu. It can be activated using 
`Ctrl + t + .`
. It isn't nearly as comprehensive as the menu we get in awesome, but it is useful for easy navigation to X11 apps.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/lwu9c9tfmlq6g5kh19d5.png)

---

### Frame Navigation

Each window in ratpoison occupies an entire frame, with no overlapping of frames allowed. You can easily jump from one frame to the other by pressing 
`Ctrl + t + [num]`
 where num is the numeric identifier of that frame. One unique thing about ratpoison is that you can even rename your windows so that you can easily refer to them for navigation.

For viewing which frames are open, press 
`Ctrl + w`
: 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7m0bojfev7vd6krfj1cn.png)

Notice how each window frame has a number next to it. That number can be used after hitting the top command to jump to that frame. You can also jump to the previous and the next frame using the 
`Ctrl + t + n|p`
 commands.

---

### Configuration

Configuring ratpoison is very easy, primarily due to it being well documented. Ratpoison client has a set of commands that can be used to interact with the window manager. To pass in the client native commands, you can do 
`Ctrl + t + :`
. For running terminal commands, you can do 
`Ctrl + t + !`
. 

To start configuring ratpoison, create a file called 
`~/.ratpoisonrc`
. Here is what my configuration looks like:


```sh
# exec command can be used to execute shell commands
# this command starts up the compositor
exec picom &

# this command sets the wallpaper
exec nitrogen --set-scaled /usr/share/backgrounds/Manhattan_Sunset_by_Giacomo_Ferroni.jpg

# this command sets up the battery alert
exec /usr/local/bin/battery_alert 100 &

# c-t r will restart ratpoison
bind r restart 

# c-t f will execute firefox
bind f exec firefox

# vim-like nav commands
# difference between bind and definekey is that 
# definekey does not require the top command to be run first
definekey top M-l focusright
definekey top M-h focusleft
definekey top M-j focusdown
definekey top M-k focusup

# For having multiple workspaces
# Can be shifter by Alt-F1-6
exec /usr/bin/rpws init 6 -k
```


You can read more about how to configure your ratpoison from [here](https://www.nongnu.org/ratpoison/doc/). Ratpoison requires minimum configuration for the most part. That is a huge perk in its favour. 

---

### Verdict

Ratpoison aims at only one thing: Getting rid of the mouse. And it succeeds keeping user away from the mouse for the most part. I noticed that ratpoison is extremely hard to use with its default keybindings and inflexible window splits. Especially due to the fact that I come from a vim environment rather than emacs. 

I can see how ratpoison will be ideal for someone coming from emacs, but I still feel that there are more feature rich window managers out there which can be used in a minimal fashion to ensure minimal mouse usage. In lieu of this, I certainly wouldn't recommend ratpoison for a newcomer. If you are a veteran emacs user then this *WM* might be for you. I personally prefer spectrwm over ratpoison when it comes to following "no wasted screen real-estate" philosophy. 

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: :heart: |
| Learning curve (lesser is better)| :heart: :heart: :heart: :heart: |
| Productivity | :heart: :heart: |
| Fun | :heart: |

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/ratpoison-forget-about-your-mouse-1391)*


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

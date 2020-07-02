---
title: The Linux Desktop Deep Dive
date: '2020-04-04T07:06:34.352Z'
excerpt: >-
  Linux has definitely made a lot of sense even in a purely materialistic
  sense.   Linus Torvalds    I...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--UUtpMWNl--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/od5ure9kbixnt95o7do7.jpg
comments_count: 37
positive_reactions_count: 460
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/the-linux-desktop-deep-dive-1jh3'
layout: post
---
> Linux has definitely made a lot of sense even in a purely materialistic sense.
> - Linus Torvalds

In a world where existing software design practices led to monolithic mayhem, especially in the case of kernels and operating systems, the linux community came up with software designed like a castle built out of lego. 

The best part of linux I love is a conjunction of its simple complexity and the complex simplicity in the form of customizablity. Everything about linux is modular and user centric. And how the cogs work together like a well oiled machine is what amazes me. 

The linux desktop environment is one such pluggable GUI layer in a vast expanse of sedimentation. It feels like a system which truly cares about the freedom of its users. Like a hive mind with individuality. This is what has motivated me to do a series of "window manager hopping".

A typical linux desktop is composed of the following moving parts:

* [Display Manager](# display-manager)
* [Window System](# window-system)
* [Window Manager](# window-manager) 
* [Desktop Environment](# desktop-environment)

A typical hierarchy looks like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/oojld2xuel4fa4272ktj.png)

Before getting into each and every component, let us look at what a linux system looks like without any graphical user interface. 

When a linux machine is booted, it spawns 8 *ttys* by default. TTY essentially means a terminal console without any GUI. You can access these consoles by pressing 
`<Ctrl> + <Alt> + [1-8]`
. For example, pressing 
`<Ctrl> + <Alt> + 1`
 will show the following screen:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/79kyltkcuoh10e0xafjc.png)

The 7th tty actually loads the GUI with the **display manager** which we will get to in the next section. 

---

### Display Manager

A display manager (also called login manager) is loaded after the end of the boot procedure in linux. It loads up an authentication screen, much like telnet, which prompts for the username and password. Its primary function is to handle authentication, and manage user session. It also loads the window system configured for the machine and it does so by running a **.xsession** script, which is used to setup initial clients (we will get to what an X Client is in the following section).

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4y5jx2fczcxumeu5yzv7.jpg)

Some examples include **lightdm**, which comes out of the shelf for many linux systems and is easily one of the most versatile display managers out there. Some others include **gdm**, which is the display manager for gnome, and **xdm** for X11 (which we will get to shortly). 

The best part about a display manager is that you don't have to roll with the one which is pre-installed on your system. Running a new *DM* is as easy as running the following commands:


```
sudo systemctl disable gdm
sudo apt install lightdm
sudo systemctl enable lightdm
```


The second best part about a *DM* is its customizability. Anything can be customized, from the colour to the greeter screen. For example, to customize a lightdm login manager, you need to edit 
`/etc/lightdm/lightdm.conf`
. 

To see your default display manager, simply run the following command:


```
cat /etc/X11/default-display-manager
```


---

### Window System

A window system is the heart and soul of GUI in linux. It determines what needs to be drawn on the screen and how. In this particular blog, we are going to be talking about the most popular window system: **X Window System**, also called **X** or **X11**, which is the name I am going to use henceforth. 

X11 uses a network approach to GUI in linux. It consists of the following elements:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4uxt4xt8uij4v6z2hsqh.png)

* 
`X Server`
: It is a program that interacts with the hardware and controls display to draw boxes and buttons. Each X Server is made for a specific video card (it has hardware dependency). Note that X11 has a flipped view of the client-server architecture. Typically a server runs remotely in such an architecture, but in X11 the server actually runs on the host machine.

* 
`X Client`
: It is a program which uses the X Server to display itself on a specific screen, eg: xclock, xterm, xcalc. The best part about X11, which revolutionized how people think about GUI, is that the X Client and Server do not need to be on the same machine. What it essentially means is that I can send commands from my machine to display a particular program in a different machine, and vice versa. How cool is that!

* 
`Window Manager`
: We will get to *WMs* in the next section.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/m1r6frr7nw17gtpnjar4.GIF)

Both the X Client and the X Server speak a common tongue, and communicate to each other using the X protocol. The connection string looks something like this:


```
hostname:displaynumber:screennumber
```


* 
`Host Name`
: Name of the physically connected machine (display). If this part is left empty, then it defaults to the current machine. Host name can be a machine's node name, IP address, or blank.

* 
`Display Number`
: There might be a lot of displays connected to a particular device. This field specifies which display to connect to.

* 
`Screen Number`
: Every single monitor has multiple windows. This field represents which window to display to.  

This connection string is stored in 
`DISPLAY`
 environment variable in linux, and to view which display you are outputting to, simply run the following command:


```
echo $DISPLAY
```


To start the GUI on a minimalist *tty*, simply run the following command in the terminal:


```
startx
```

This command is part of the 
`xinit`
 tool which specializes in initializing X11. If you don't already have it, you can always run the following command to install it:


```
sudo apt install xinit
```
 

--- 

### Window Manager

A window manager is a special client application which controls the geometry, appearance, coordinates and graphical properties of X display. It is also responsible for re-shuffling and re-sizing windows in a stack. Some of the popular window managers are: dwm, i3, herbstluftwm, awesome, openbox etc. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/nuiy52p82wj87kjtbgac.jpg)

A window manager also provides client side decorations, such as title-bars, buttons etc. Note that a lot of *gtk* applications have inbuilt client side decorations, and thus do not need window managers (eg: firefox, gedit). 

The linux community has developed a lot of standalone *WMs* over the years. More and more are leaving full desktop environments and shifting to window managers for the following reasons:

* Less bloated, and packed with the bare essentials
* Faster and hence more productive
* Highly customizable 

Switching window managers is as easy as executing the following commands:


```
sudo apt install dwm
echo "exec dwm" > ~/.xsession
```


As mentioned earlier, the display manager runs the 
`.xsession`
 script. Adding 
`exec dwm`
 command in the aforementioned script indicated the *DM* to run the dwm window manager immediately after login. 

---

### Desktop Environment

A desktop environment can easily be called a superset of a window manager. In fact it is a bundled GUI which has a lot of features in addition to a *WM*, including wallpapers, toolbar, icons and desktop widgets. It is a full fledged graphic user interface. Some examples include gnome, XFCE, KDE etc. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/mb41j4yzw0u6xef5jdo2.png)

---

### Conclusion

This blog was a deep dive into how Window Systems and Managers work, and how you see the GUI that you have grown to love. In the subsequent parts of the series, I will be trying out various window managers and talking about the following:

* *WM* Features
* Installation and set up
* Functionality in action
* Verdict

If you want me to include some additional study metrics or want to suggest a window manager, do comment. Stay tuned for the upcoming parts :v:. 


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/the-linux-desktop-deep-dive-1jh3)*


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

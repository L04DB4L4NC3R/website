---
title: 'Spectrwm: The Compact Window Manager'
date: '2020-04-29T05:27:12.560Z'
excerpt: >-
  Spectrwm, is a small and minimalist tiling window manager. It is unlike manual
  WMs like bspwm and has...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--Ta4cyH3y--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/z0gfdfsu89dom3wjpdbg.png
comments_count: 1
positive_reactions_count: 6
tags:
  - linux
  - techtalks
  - ubuntu
  - opensource
canonical_url: 'https://dev.to/l04db4l4nc3r/spectrwm-the-compact-window-manager-3efl'
layout: post
---
Spectrwm, is a small and minimalist tiling window manager. It is unlike manual *WMs* like bspwm and has more in common with dwm and i3. It was hilariously called scrotwm earlier. 

Spectrwm is one of the more obscure window managers. I frankly didn't like it as much as some of the other WMs that I have tried so I had decided not to write an entry on it. But I realized that I gotta get my points out there since some of you guys might have different opinions about this window manager (and might be able to change mine as well).

 
* [Features](# features)
* [Setting up](# setting-up)
* [Getting started](# getting-started)
* [Tags](# tags)
* [Layouts](# layouts)
* [Configuration](# configuration)
* [Why I don't like Spectrwm](# why-i-dont-like-spectrwm)
* [Verdict](# verdict)

---

### Features

* It is a dynamic tiling window manager.
* It has a plaintext configuration file and can be reloaded during runtime. 
* It strives to be small, compact and fast.
* It uses workspaces instead of tags for managing multiple windows.
* Although spectrwm isn't well document by far (at least compared to i3), it is easy to configure due to the commented defaults. 


---

### Setting Up

Spectrwm is available on most source repositories. In addition, you can download the release and build it from source.


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Fconformal%2Fspectrwm" style="border: 0; width: 100%;"></iframe>


The easiest way to get started (on debian based systems) is this:


```sh
sudo apt install spectrwm
```

To run it, simple add the following line in your 
`~/.xsession`
 file:


```
exec spectrwm
```


Logout and log back in again, and boom! You are good to go.

When you login to spectrwm, you get a basic menu bar which contains details like:

* Which monitor you are on.
* Which workspace you are on
* Date and time

Spectrwm does not support some popular menu bars such as the beloved polybar, yabar and lemonbar. If you want to customize the menu bar, you can either write your own script or use an alternative that works with spectrwm, namely **conky**. In this blog we will be using conky to configure our menu bar.

All of the default keybindings of spectrwm can be seen in its man page (which is surprisingly comprehensive). Almost any problem while setting up spectrwm can be resolved by RTFM (Reading the Freaking Manual). 


```sh
man spectrwm
```


---


### Layouts

Spectrwm comes with 3 layouts mainly. You can switch between these layouts using the 
`Mod + Spacebar`
 keys. The default modifier in spectrwm is the windows key (Mod4).

* **Vertical Master-Stack Layout**: This is the default layout in spectrwm. Here your left window will be the master, and every window you create after that will keep on stacking on the right hand side. This is also the default layout in dwm.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/vnvd6hi2qhjr8xxd6kqw.png)

* **Horizontal Master-Stack Layout**: This is similar to the master-stack layout only. But here the master is at the top horizontal window split and each new spawn vertically splits the bottom horizontal split of the window.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k7fextejf4fwh57iucya.png)

* **Full Screen**: In this layout, all windows occupy 100% of your screen space. They can then be switched back and forth by using the 
`Mod + j|k`
 keys.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/234bw0fdf5ni47krwnxe.png)

---


### Configuration

The default configuration file of spectrwm is 
`~/.spectrwm.conf`
. There is an example configuration available at 
`/etc/spectrwm.conf`
. You can copy it to your home folder to get started. 

As soon as you go inside the file, you will notice that all of the important functionalities that you might customize in a window manager are already commented. Whenever you make a change in the configuration, just press the 
`Mod + q`
 key to restart spectrwm.

Configuration in spectrwm is pretty self explanatory so I wont be diving deeper. I will just touch on these three subjects:

* [Key Bindings](# key-bindings)
* [Quirks](# quirks)
* [Conky Bar Setup](# conky-bar-setup)

---

#### Key Bindings

The **bind** function can be used for mapping programs to keys in spectrwm. Now this might not be obvious but there is a separate configuration file with a LOT of key bindings specified beforehand. You can head over to [the official spectrwm repository](https://github.com/conformal/spectrwm) to take a look at the keybinding configurations. All of the configuration files with country ISO codes ahead of them (eg: spectrwm_fr.conf) are the files which you need to look at. 

You can paste the contents of [spectrwm_us.conf](https://raw.githubusercontent.com/conformal/spectrwm/master/spectrwm_us.conf) in your 
`~/.spectrwm.conf`
 and fiddle around with the keybindings to suit your needs. The syntax is pretty easy to understand:


```
bind[<action>] = <keybinding>
```


---

#### Quirks

You can associate a certain program to open a certain way using quirks. They can be thought of as modifiers which limit (or extend) the actions of a specific program in a window. For example: 


```
# quirk[Firefox:Dialog]			= FLOAT
# quirk[Gimp:gimp]	
```


The format of a quirk is the following: 


```
quirk[<class>:<name>] = [NONE | FLOAT | ANYWHERE | FULLSCREEN | FOCUSPREV]
```


The class name of a program is actually the class name we get after selecting a window in 
`xprop`
 mode. It is the official X11 name of a particular window:


```sh
# how to get the class name of a window
xprop | grep WM_CLASS
```


---

#### Conky Bar Setup

If you take a closer look at the bar section of a spectrwm configuration, there is an option called **bar_action**. You can map it to a custom script if you want. You can also map it to conky, if you want to use it:


```
bar_action = conky
```


Conky is a lightweight system monitor for X11 that can be used to display any kind of information on your desktop. It needs a configuration file at **~/.conkyrc**. This is how my conkyrc looks like:



```
out_to_x no
out_to_console yes
update_interval 1.0
total_run_times 0
use_spacer none
TEXT
[ ${time %R %a,%d-%# b-%y} ] [ Mail:${new_mails} ] [ Up:${uptime_short} ] [ Temp:${acpitemp}C ] [ Battery: ${battery_percent BAT1}% ${alignr}${battery_bar 3,20 BAT1} ] [ ${addr wlp0s20f3} ] [ RAM:$memperc% ] [ CPU:${cpu}% ] [ ${downspeedf wlp0s20f3} Mbps ]
```


Refresh your spectrwm and you will get a bar like this: 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/35eqsx27jyvwx8kjkk2g.png)

To learn more about conky, you can head over to its official repository:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Fbrndnmtthws%2Fconky" style="border: 0; width: 100%;"></iframe>


---

### Why I don't like spectrwm

Some of you might not agree with this section. But know that some of these points are facts and others are just my opinions. They might not be a deal breaker for you. Some of these are some issues that I faced while dealing with spectrwm, even after *RTFM*, so I felt like I needed to mention it for all of the new users who might want to try spectrwm out.

* Spectrwm does not support [external compositing](https://dev.to/l04db4l4nc3r/compositors-in-linux-1hhb). Which means compton or picom will simply not work with it. You can say goodbye to window animations, drop shadows and transparency

* As mentioned earlier, spectrwm does not support third party menu bars such as polybar, lemonbar or yabar. Which is kind of stupid due to it's similarities with i3 and dwm.

* When you install spectrwm, [there is a bug](https://github.com/conformal/spectrwm/issues/11) which forces certain programs to open up on certain workspaces only. This is annoying if you are working on workspace 1 and you want to spawn a terminal on the same workspace but it ends up on workspace 6 without any reason. Although this bug can be solved by adding a simple quirk, but due to design decisions, it can not be included with the base spectrwm build. 

* While using spectrwm, I have noticed that it remembers the exact layout of your previously opened tiles in a particular workspace. For example if I open 3 terminals and resize each and every one of them, the next time I open 3 terminals on the same workspace, they are going to be the same size. This might be an annoyance if you don't want your windows to be the same size everytime. 

* I noticed a very weird thing that started happening in my *WM*. Whenever I opened some windows on a workspace which already has a window, they spawned behind the current window. This caused a lot of annoyance since I was not able to figure out if my windows were even being spawned or not. Later on I realized that it was because fullscreen mode and I had no indication that it was configured only for that particular workspace. As I mentioned earlier, spectrwm also memorizes layout on a per-workspace basis. Which is very different from other WMs.

---

### Verdict

Spectrwm has it own array of annoyances and incompatibilities. But the more I think about its design philosophies, the more convinced I am that these incompatibilities are intentional. 

Spectrwm aims at being a very minimal and lightweight window manager, not just in terms of lines of code and bulk but in terms of usage. If you are someone who does not want any aesthetic distractions, wants to make the full use of screen real estate, then this is the WM for you. 

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: :heart: |
| Learning curve (lesser is better)| :heart: :heart: :heart: |
| Productivity | :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: |

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/spectrwm-the-compact-window-manager-3efl)*


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

---
title: 'I3: The Improved Tiling Window Manager'
date: '2020-04-09T15:34:11.775Z'
excerpt: >-
  One of the most popular tiling window managers out there, i3 is written from
  scratch. The developers...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--TWfWNWNg--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/qe42wqr0i4a0wkxb9j0k.png
comments_count: 8
positive_reactions_count: 42
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/i3-the-improved-tiling-window-manager-42k7'
layout: post
---
One of the most popular tiling window managers out there, i3 is written from scratch. The developers claim that it is targeted towards advanced users, but it is certainly easy to use and configure. More so than its suckless alternative. Primarily due to its beautiful and well maintained documentation (some of the best docs I have ever seen for window managers), as well as an advanced user community who regularly chip in to make sure things keep running smooth.

I3 is written from scratch

* [Features](# features)
* [Setting up](# setting-up)
* [Getting started](# getting-started)
* [Workspaces](# workspaces)
* [Windows](# windows)
* [Modes of operation](# modes-of-operation)
  * [Splitv mode](# splitv-mode)
  * [Splith mode](# splith-mode)
  * [Stack mode](# stack-mode)
  * [Tabbed mode](# tabbed-mode)
* [Configuration](# configuration)
  * [Changing Keybindings](# changing-keybindings)
  * [Configuring The Status Bar](# configuring-the-status-bar)
* [I3-gaps](# i3-gaps)
* [Verdict](# verdict)
* [References](# references)

---

### Features

* I3 uses the tree data structure for storing window references.
* It has different *modes* of operation. Which we will see in the upcoming sections.
* I3 assigns each workspace to a virtual monitor, thus implementing multi-monitor functionality correctly.
* It can be configured during runtime. Which means that any customization made does not require the service to be restarted.
* It uses the asynchronous XCB library instead of the old, synchronous XLIB.

Check out the I3 guidelines on their [official website](https://i3wm.org/)

One thing to note is the following statement clearly mentioned on their official website:

> The usual elitism amongst minimal window managers: Don’t be bloated, don’t be fancy (simple borders are the most decoration we want to have).
However, we do not enforce unnecessary limits such as a maximum amount of source lines of code. If it needs to be a bit bigger, it will be. 

Now I don't know about you guys but I think this is targeted at [dwm](https://dev.to/l04db4l4nc3r/dwm-the-suckless-window-manager-1ji) for enforcing a 2000 SLOC limit on their development. But it is for you guys to decide :)


---

### Setting Up

I3 is available for the following distributions. In addition, you can download the debian release, or just the tarball as well.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/46u7qn6wjjqld64p0i3r.png)

The easiest way to get started (on debian based systems) is this:


```
sudo apt install i3
```

To run it, simple add the following line in your 
`~/.xsession`
 file:


```
exec i3
```


Logout and log back in again, and boom! You are good to go.

---

### Getting Started

The first time you run i3, since you will not have a configuration template at 
`~/.config/i3/config`
, i3 will run the **i3-config-wizard**. Which will prompt you to generate a configuration automatically:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/rtj22jwqejdoavkwja2d.png)

Once you do that, you will be greeted by your wallpaper, with a thin status bat at the bottom. Yes, i3 status bar is at the bottom by default. But this can of course easily be configured.

The default modifier in i3 is 
`<Alt>`
. To spawn a terminal, press 
`<Alt> + <Enter>`
. 

When we do that for the first time, the screen looks something like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wf1wit6pnvty3l275lam.png)

---

### Workspaces

In i3, the status bar shows the number of active workspaces. I3 gives you 10 workspaces that we can switch between. To do so, simply hit 
`<Alt> + [1-9]`
 for the first 9 and additionally 
`<Alt> + 0`
 for the 10th workspace. For example 
`<Alt> + 6`
 will take you to the 6th workspace. Note that whatever was running on the previous workspace keeps on running there as usual.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8ppveu8hs4g59yh4pmkq.png)

---

### Windows

i3 uses vim bindings for movement. The only difference is that instead of using 
`h|j|k|l`
 for movement, it shifts the bindings one key to the right and instead uses 
`j|k|l|;`
. 

| Default key binding | Action performed |
|:-------------------:|:----------------:|
| 
`<Alt> + v`
 | Split window vertically on the next spawn |
| 
`<Alt> + h`
| Split window horizontally on the next spawn |
| 
`<Alt> + [j/k/l/;]`
| Move left-right-up an down windows |
| 
`<Alt> + e`
| Toggle horizontal and vertical |
| 
`<Alt> + d`
| Open dmenu |
| 
`<Alt> + <Shift> + q`
| Quit the currently running window |
| 
`<Alt> + <Shift> + r`
| Re-load configuration |
| 
`<Alt> + <Shift> + [1-9]`
 | Re-locate the current window to another wprkspace |
| 
`<Alt> + <Shift> + 0`
 | Re-locate the current window the tenth wprkspace |
| 
`<Alt> + s`
| Turn on stacking mode (explained in the next section) |
| 
`<Alt> + w`
| Turn on tabbed mode (explained in the next section) |


---

### Modes of Operation

As mentioned earlier, i3 uses the tree data structure for storing window references in workspaces. Traversing through these windows is just like tree traversal. Now you have different modes of operation, and each mode tweaks the layout, but all in all it is just a tree data structure underneath. For example, in the given window split pane, the tree will look like the following:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wjfhlkpm61land4h1pay.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/i6neluoygavqslpn483k.png)

---

#### Splitv Mode

This mode is used for spawning windows which are vertically split. To activate this mode, simple press 
`<Alt> + v`
. After this mode being activated, when you spawn programs next, either using shortcuts or dmenu, they will be vertically split.


![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/771habbjj89lkv8vu0de.png)

---

#### Splith Mode

This mode is used for spawning windows which are horizontally split. To activate this mode, simple press 
`<Alt> + h`
. After this mode being activated, when you spawn programs next, either using shortcuts or dmenu, they will be horizontally split.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/yzqnlmvglwdqkgt3wqmc.png)



`Note`
: You can switch between horizontally and vertically split panes using 
`<Alt> + e`
 toggle

---

#### Stack Mode

Stack mode will place each and every tab on top of each other like a stack. Note that it is not actually a stack internally, but only visually so. To activate stack mode press 
`<Alt> + s`
.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/s3l6g8g2csgh3whdb865.png)

---

#### Tabbed Mode

Tabbed mode is exactly like the stack mode, the only difference being that it visually places the windows as tabs (the kind you might see on a browser). To activate it, press 
`<Alt> + w`
.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/adcllk01uczfrd8woq7g.png)

---


### Configuration

The i3 configuration lies in 
`~/.config/i3/config`
 file. It uses an easy to use syntax for defining parameters. All of which are well documented on i3's official user manual. In this blog, we will be configuring our status bar as well as changing some key bindings to get started. In the [next section](# i3-gaps) we will learn how to add gaps between windows in i3. 

See the full configuration tutorial for i3 [here](https://i3wm.org/docs/4.12/userguide.html# configuring).

---

#### Changing Keybindings

In i3 configuration, keybindings are defined by the 
`bindsym`
 keyword, and the modifier (
`<Alt>`
 by default) is defined by 
`$mod`
. 

Now I am a long time vim user, so I am used to the vim's usual movement keys (h|j|k|l). In i3 everything is shifted to the left. Now let us try to change that. Find the following lines in the configuration:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/m499duiip8hdsp5212pp.png)

And change it to use h|j|k|l instead of j|k|l|;. For the configuration to take effect, save the file and hit 
`<Alt> + <Shift> +r`
 for live reload. You will now see the following prompt on top:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8huuuext2x9chndq6si0.png)

Whoa whoa! This wasn't supposed to happen right? I3 throws an error in the form of a red status line whenever there is an error in the configuration. So you will always get to know where you went wrong. How convenient is that! Just a quick show at the error log will make you realize that you cannot bind 
`<Alt> + h`
 for moving left since it is already bound (for splith mode). To get rid of this error, just change the binding for splith mode like the following, and you should be good to go! Hit 
`<Alt> + <Shift> + r`
 after making the change, and voila.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/gxpwpcs2mx88g2swcx77.png)

---

#### Configuring the Status Bar

The bar at the bottom of your screen is called the status bar, or simply **i3bar**. It supports very low as well as high level customization, including:

* Changing aesthetics (color, font, opacity). 
* Adding custom configuration
* Adding custom commands to be executed and shown on the i3bar

A full set of supported variables and customization can be viewed [here](https://i3wm.org/docs/4.12/userguide.html# _configuring_i3bar).

The following is my configuration, which I have added at the bottom of my 
`~/.config/i3/config`
 file:



```
# CSS-like element selector
bar {
        # For the default i3 status bar information
        status_command i3status

        # The nproc command will be executed and the result will be 
        # shown on the right side of the i3bar. You can add custom shell
        # scripts here (after exec)
        status_command exec /usr/bin/nproc

        # The next two lines are for the font that I am using
        font -misc-fixed-medium-r-normal--13-120-75-75-C-70-iso10646-1
        font pango:DejaVu Sans Mono 14

        # I want by i3bar to be at the top rather than the bottom
        position top
        
        # The next section is for the i3bar colors and transparency
        # i3bar uses the RGBA format for color specification where the A
        # is for the opacity (which is optional). 
        # The RGBA string will be hexadecimal; so # [__][__][__][__]
        i3bar_command i3bar --transparency
        colors {
            # RGBA format
            # The fourth option accounts for the opacity 
            background # 844685aa
            statusline # ffffffdd
            separator # ffffffdd
        }
}

```


After saving the configuration and refreshing i3, the bar looks like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/z4dowy0jj41pgzaw0wiq.png)

---

### I3 gaps

I3-gaps is a fork of I3 which adds additional functionality such as configuring gaps between windows. The best part about i3-gaps is that it is always kept up to date with the upstream, so any new update in i3 will also be reflected in i3-gaps. Check out the official repository here:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2FAirblader%2Fi3" style="border: 0; width: 100%;"></iframe>


Now i3 has PPAs for Ubuntu and AUR's for Arch. If you want to build it from source, for other distributions, [this](https://gist.github.com/boreycutts/6417980039760d9d9dac0dd2148d4783) gist will get you started on it. 

Once you install it, you are good to go. Add the following lines (in the same config file) for configuring gaps between your windows:



```
# only works if i3-gaps is installed
# a window selector should be there
for_window [class="^.*"] border pixel 2

# defining inner and outer window gaps
gaps inner 10
gaps outer 10
```


Save and reload, and you are good to go. I3-gaps also has a smart gaps feature, where gaps can be turned on and off in a particular workspace in certain scenarios. I recommend checking out the official repository for the same. 

---



### Verdict

I3 is free of bloat, and is very easy to learn. Even though it might be more complex than simpler alternatives like herbstluftwm, but learning it is easier due to the excellent documentation which makes for a fun exploration. I recommend everyone to try out i3. 

The developers at i3 took a rather radical approach, building this wm from scratch, using a tree data structure. But the more I read up about i3, the more I see how well they have utilized this idea. I3 is not the best wm by far, but it is certainly one of the better ones. 

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: :heart: :heart: |
| Learning curve (lesser is better)| :heart: |
| Productivity | :heart: :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: |

---

### References

* [I3 user guide](https://i3wm.org/docs/userguide.html)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/i3-the-improved-tiling-window-manager-42k7)*


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

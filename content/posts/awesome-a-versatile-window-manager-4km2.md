---
title: 'Awesome: A Versatile Window Manager'
date: '2020-04-11T04:26:06.964Z'
excerpt: >-
  Awesome, or awesomewm, is a window manager which comes with a lot of features,
  right out of the box....
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--ctma6Axi--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/oghr6plxpkyqrhzlsbvi.png
comments_count: 6
positive_reactions_count: 36
tags:
  - linux
  - opensource
  - techtalks
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/awesome-a-versatile-window-manager-4km2'
layout: post
---
Awesome, or *awesomewm*, is a window manager which comes with a lot of features, right out of the box. It is written in the Lua programming language (almost), but configuring it does not require a lot of knowledge about the same. It is ideal for people starting out with window managers due to the fact that it is shipped with a lot of useful functionality which you would otherwise have to configure separately.


* [Features](# features)
* [Setting up](# setting-up)
* [Getting started](# getting-started)
* [Tags](# tags)
* [Layouts](# layouts)
* [Configuration](# configuration)
   * [Changing default keybindings](# changing-default-keybindings)
   * [Adding/removing layouts](# adding-and-removing-layouts)
   * [Adding startup processes](# adding-startup-processes)
   * [Adding useless gaps between windows](# adding-useless-gaps)
* [Verdict](# verdict)
* [References](# references)

---

### Features

* Awesomewm is very stable, fast and with a small codebase and footprint.
* It uses tags instead of workspaces: windows can be placed on several tags and displayed at the same time.
* It can be configured during runtime. Which means that any customization made does not require the service to be restarted.
* It uses the asynchronous XCB library instead of the old, synchronous XLIB.
* It comes with a very comprehensive application menu as well as a run menu. 



---

### Setting Up

Awesomewm is available on most source repositories. In addition, you can download the release and build it from source.


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2FawesomeWM%2Fawesome" style="border: 0; width: 100%;"></iframe>


The easiest way to get started (on debian based systems) is this:


```sh
sudo apt install awesome
```

To run it, simple add the following line in your 
`~/.xsession`
 file:


```
exec awesome
```


Logout and log back in again, and boom! You are good to go.

---

### Getting Started

When you login, awesomewm already has a default wallpaper set. Along with 9 tags on the menubar. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/g2mpwn6qfzpgrc39zxfr.png)

The default modifier in awesomewm is 
`<Win>`
. To spawn a terminal, press 
`<Win> + <Enter>`
. To get a list of all shortcuts, awesomewm provides a comprehensive cheat-sheet. Just press 
`<Win> + s`
 to view it. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/kwmwkdi8rcnw32qqafhb.png)

To activate the application menu simply click on the top left corner of the menu bar, or right click anywhere. You will be greeted with something like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/d2ysdz6u3iokqcgvsiye.png)

This menu can be used as a quick launcher, and even be configured to hold items which you want. In addition, 
`<Win> + r`
 can be used for spawning a run menu on the menubar. But I prefer dmenu instead.

---

### Tags

In awesomewm, the status bar shows the number of active tags. Awesome gives you 9 tags that we can switch between. To do so, simply hit 
`<Win> + [1-9]`
. For example 
`<Win> + 6`
 will take you to the 6th workspace. Note that whatever was running on the previous workspace keeps on running there as usual.

To shift a currently running window to another tag, simply press 
`<Win> + <Shift> + [1-9]`
.

---

### Layouts

In awesomewm, movement between windows is done using 
`<Win> + j|k`
 and window resizing is done using 
`<Win> + h|l`
.

Awesome offers different layouts per tag, which can be viewed on the left top corner of the menu bar and can be changed by clicking on the same:

 	
Cornernew: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/cornernew.png) 	
Cornetnww: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/cornernww.png) 	
Cornerser: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/cornersew.png) 	
Cornersww: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/cornersww.png) 	
Dwindlew: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/dwindlew.png) 	
Fairhw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/fairhw.png) 	
Fairvw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/fairvw.png) 	
Floatingw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/floatingw.png) 	
Fullscreenw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/fullscreenw.png) 	
Magnifierw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/magnifierw.png) 	
Maxw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/maxw.png) 	
Spiralw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/spiralw.png) 	
Tilebottomw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/tilebottomw.png)	
Tileleftw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/tileleftw.png) 	
Tiletopw: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/tiletopw.png)
Tilww: ![Alt Text](https://github.com/awesomeWM/awesome/raw/master/themes/default/layouts/tilew.png)



---


### Configuration

The awesome configuration lies in 
`$XDG_CONFIG_HOME/awesome/rc.lua`
 file. For example: 
`/etc/xdg/awesome/rc.lua`
. By default awesomewm looks at the 
`~/.config/awesome/rc.lua`
 file if it can find it. If it can't then it defaults to the aforementioned configuration. 

To edit it, simply run the following command for getting started:


```sh
cp /etc/xdg/awesome/rc.lua ~/.config/awesome/
vim ~/.config/awesome/rc.lua
```


After making any changes in 
`rc.lua`
, awesomewm can be reloaded by pressing 
`<Win> + <Ctrl> + r`
. In addition, the awesome-client can also be used for the same: 


```sh
echo 'awesome.restart()' | awesome-client
```


In this blog, we will be configuring the following things:

* [Changing default keybindings](# changing-default-keybindings)
* [Adding/removing layouts](# adding-and-removing-layouts)
* [Adding useless gaps between windows](# adding-useless-gaps)
* [Adding startup processes](# adding-startup-processes)


---

#### Changing Default Keybindings

The configuration file, 
`rc.lua`
, contains a *globalkeys* option which is a table that stores keybindings.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/gkzcowbyex77tkb7gqug.png)

The first section stores the modifier keys, eg: 
`{modkey,}`
,  
`{modkey, "Shift"}`
 or 
`{modkey, "Control"}`
. The second part can be used to add keys to be pressed along with the modifier, and the third part is the function to be performed when the particular binding is pressed. 

Each keybinding is a part of a group and a description can be provided to go along with them. Adding a keybinding is as simple as copy-pasting the above binding and changing it with respect to what action you want to perform. For example, the following binding spawns firefox whenever I press 
`modkey + b`
: 


```lua
awful.key({modkey, }, "b", awful.spawn("firefox"))
```


---

#### Adding Startup Processes

You can spawn processes or applications easily by using the following commands in 
`rc.lua`
. To open these applications on startup, simply add the commands at the bottom of the configuration:


```lua
-- spawning a program
awful.spawn("firefox")

-- running a script inside a shell
awful.spawn.with_shell("launch.sh")

-- setting wallpaper using nitrogen
awful.spawn.with_shell("nitrogen --set-scaled /usr/share/backgrounds/crysis.jpg")
```


---

#### Adding and Removing Layouts

Lain is a library which provides a lot of useful commands for configuring widgets, adding layouts and other useful tweaks. Follow the repository to see how to use lain to its fullest:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Flcpz%2Flain" style="border: 0; width: 100%;"></iframe>


Let us get started by importing lain in our 
`rc.lua`
:


```lua
local lain = require("lain")
```


To add a layout, namely [centerwork](https://github.com/lcpz/lain/wiki/Layouts# centerwork), defined by lain, simply go to the 
`awful.layout.layouts`
 section and add 
`lain.layout.centerwork`
. Other layouts can be removed from here, if you want to. The order of the layouts matter!

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zsk8a92li9wvmco1hift.png)


---

#### Adding Useless Gaps

Useless gaps refers to the space between windows that can be added for aesthetic purposes. For example: 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/20bs2uv80znh75e4cema.png)


These gaps can be configured at runtime by adding the following keybindings to *globalkeys*:


```lua
awful.key({ modkey, "Control" }, "=", function () lain.util.useless_gaps_resize(1) end),

awful.key({ modkey, "Control" }, "-", function () lain.util.useless_gaps_resize(-1) end),
```


These commands will resize the gaps by a factor of 1 pixel every time we press 
`modkey + Control + =|-`
. 

---


### Verdict

Even though configuring awesomewm is not as easy as i3, it offers a lot of things right out of the box and is easy to get started with. Lua configuration is slightly challenging when it comes to adding additional libraries and trying to keep the code modular but there is a very supportive community and third party libraries for the same. 

Awesome is a solid window manager for both beginners and experts, and I highly recommend it for both. 

| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: :heart: |
| Learning curve (lesser is better)| :heart: :heart: :heart: |
| Productivity | :heart: :heart: :heart: :heart: |
| Fun | :heart: :heart: |

---

### References

* [Official Website](https://awesomewm.org/)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/awesome-a-versatile-window-manager-4km2)*


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

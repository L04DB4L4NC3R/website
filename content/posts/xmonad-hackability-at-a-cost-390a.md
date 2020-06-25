---
title: 'XMonad: Hackability, At a Cost'
date: '2020-06-15T14:13:12.041Z'
excerpt: >-
  I started using Xmonad a month ago. Usually I live in a Window Manager for a
  week or so before writin...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--eUd8m6iH--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--GiX1dOnC--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/4da4nr3sfkc39c4fjbxd.png
comments_count: 0
positive_reactions_count: 3
tags:
  - linux
  - techtalks
  - opensource
  - ubuntu
canonical_url: 'https://dev.to/l04db4l4nc3r/xmonad-hackability-at-a-cost-390a'
layout: post
---
I started using Xmonad a month ago. Usually I live in a Window Manager for a week or so before writing a post about it but took my sweet time with this particular *WM*, primarily because XMonad has so much to it that even a month of usage doesn't give me enough credibility to do it justice in my posts. Still I will make sure that a beginner can understand how to use it, and most importantly, **whether to use** it.

If you don't have time to read through the whole thing and want to Keep your confirmation bias at its peak check out [some of the cool things you can do with XMonad](# some-cool-things-you-can-do-with-xmonad)

---

### Key Features

* Suckless in nature and has configuration written in the haskell programming language.
* Reload and recompile on the fly.
* Dynamic tiling window manager with the ability to add additional layouts yourself.
* Custom run menu.
* Tags and multi-monitor support.
* Lightweight, no-bloat, and blazing fast

---

## Installation

XMonad has different ways to install on different linux distributions. The main thing to note is that it has a core library (called 
`xmonad`
) and a community library for additional feature support (called 
`xmonad-contrib`
).

Installation can be done from source (using haskell cabal) or through the distro repositories. For example, in Arch Linux you can run the following to install XMonad:


```sh
sudo pacman -S xmonad xmonad-contrib
```


The installation is different for ubuntu/debian based systems. I suggest you [read the documentation](https://xmonad.org/download.html) for the same.

Note that XMonad itself is minimal but it requires the whole haskell ecosystem to be downloaded on your machine, including the bloated 
`ghc`
 haskell compiler and it might install [cabal](https://www.haskell.org/cabal/) too, based on the type of installation you opt for. Generally you can build from source, use cabal, or use the distro repositories to name a few.

To start xmonad write the following in your 
`~/.xinitrc`
 and restart your system.


```sh
exec xmonad
```


Once you do so, you will be greeted with a black screen, and nothing else. You won't even know if you have logged in or not unless you press a right keybinding to spawn a window. You can press 
`mod + shift + enter`
 to spawn the terminal, where 
`mod`
 is the modifier key (windows key by default).

---

## How to approach configuration

XMonad is not like i3 or dwm where you have a pre-populated configuration file which you can edit to your heart's content. The best way to approach it is to look at other people's configuration files. The alternative would be to learn haskell from scratch, look at the step by step guide and learn how to create a configuration of your own. While it is a fun and well documented strategy, it is a long one. If you want a fast result then you can use and edit what other people have spent months configuring. And no, it does not make you a pirate, in fact it is what the XMonad developers suggest on their [official guide](https://wiki.haskell.org/Xmonad/Config_archive/John_Goerzen's_Configuration).

Let us take a look at a minimal configuration. Your config should reside in the following path: 
`~/.xmonad/xmonad.hs`
. You can recompile and reload your WM in real-time using the 
`mod + q`
 keybinding. 


```hs

import XMonad
import Data.Monoid
import System.Exit
import qualified XMonad.StackSet as W
import qualified Data.Map        as M

myTerminal      = "alacritty"
myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True
myBorderWidth   = 1
myModMask       = mod1Mask
-- The default number of workspaces (virtual screens) and their names.
myWorkspaces    = ["1","2","3","4","5","6","7","8","9"]
myNormalBorderColor  = "# dddddd"
myFocusedBorderColor = "# ff0000"
```


Even though you might not be familiar with the haskell programming language, still the configuration is quite readable. 
`mod1Mask`
 is your standard windows key. If you are like me and prefer to use Alt as a modifier then you can use the 
`mod4Mask`
 key. 
`--`
 is for comments in haskell. I have added my configuration in the references. Changing keybinding is fairly simple:



```hs
  -- launch dmenu
    , ((modm,               xK_p     ), spawn "exe=`
dmenu_path | dmenu
` && eval \"exec $exe\"")

    -- close focused window
    , ((modm .|. shiftMask, xK_c     ), kill)

     -- Rotate through the available layout algorithms
    , ((modm,               xK_space ), sendMessage NextLayout)

    -- Move focus to the next window
    , ((modm,               xK_Tab   ), windows W.focusDown)
```


The first part in the parenthesis defines the key combination, where 
`modm`
 is your modifier key. If you want more than one modifier with a minor key then you can use the 
`.|.`
 syntax like I have used to close the focused window. All of these functions are well documented in the step by step guide if you want to learn about them more.

---

**Custom Layouts**

If you take a look at the end of the xmonad.hs file, there is a configuration map:


```hs
defaults = defaultConfig {
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        logHook            = myLogHook,
        startupHook        = myStartupHook
    }
```


This config map is very powerful because you can add custom functions in it for handing some of the basic functionality of XMonad. For example, you can add your custom keymaps, logs, startup applications, mouse bindings, terminal etc. You can even add your custom layout in XMonad, which by default features with the master and stack layout variants. The 
`myLayout`
 is a layout map we have defined earlier in the file:


```hs
myLayout = tiled ||| Mirror tiled ||| Full
  where
    -- default tiling algorithm partitions the screen into two panes
    tiled   = Tall nmaster delta ratio

    -- The default number of windows in the master pane
    nmaster = 1

    -- Default proportion of screen occupied by master pane
    ratio   = 1/2

    -- Percent of screen to increment by when resizing panes
    delta   = 3/100
```


You can create custom modes of your own. Want a layout where 3/4th screen is horizontal and the rest is verticaly split? You can do that easily by following the xmonad documentation. With the help of distrotube, which I have linked in the description, I have some awesome layouts in my copy of the configuration file. Here are some of my favourites:

**Tall Layout**
This is the traditional master and stack layout that is very popular in all window managers. The new window comes on the left and all older windows are stacked onto the right hand side of the screen.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xn528z81f6hz1ztm0tr6.png)

**Grid Layout**
Each and every window is given the same amount of space on the screen. This results in a grid formation of spawnables.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ont7ecau7ppu886i41wd.png)

**One Big Layout**
This is a custom layout where 4 windows are allowed in tiling mode. After the 4th window, all subsequent windows keep stacking up on the last window. It gives more focus to the top left corner of the screen. It is perfect for a Dev + Ops operation where you might need 2 additional smaller windows for monitoring logs while you develop and deploy using the other two.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/tev7hao3051x9j9a1yir.png)

**Space Layout**
This layout is exactly lke the One Big layout, but it adds additonal spaces between windows for a more aesthetically pleasing look. Perfect for r/unixporn.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4f3fqsdvj9qbhwwsjo95.png)

---

## XMobar, the hackable status bar

Being suckless also means pluggability. Although XMonad does not impose any restrictions on using any status bars like dzen2, polybar or conky, but if you are going through the pain of learning and installng a WM that uses haskell, might as well use a status bar that goes along with it. XMobar is exactly what you want:


```sh
sudo pacman -S xmobar
```


You essentially need to write an xmobar script which you can then call from your 
`xmonad.hs`
 like the following:


```hs
import XMonad.Hooks.DynamicLog (dynamicLogWithPP, defaultPP, wrap, pad, xmobarPP, xmobarColor, shorten, PP(..))

-- the following line can be used to include xmobar in xmonad
xmproc0 <- spawnPipe "xmobar -x 0 ~/.config/xmobar/xmobarrc0"
```


The language is very straightforward but might feel intimidating at first. For example, [here](https://github.com/L04DB4L4NC3R/DEC/blob/master/config/xmobar/xmobarrc0) are the contents of my xmobarrc.

Notice that you can even define custom fonts and colours for each and every section of your status bar. I have it configured so that it shows me my CPU, memory and hard disk usage, along with my upload and download speeds, battery, date-time and my workspaces.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/mu9pb03fe98ulboph051.png)

---

## Some cool things you can do with XMonad

Here is a list of what xmonad can do (at least what all I have discovered so far).

* **Custom Layout Definition**. You can decide how windows are drawn  on the screen and come up with your own layouts, like this hilarious space layout:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4f3fqsdvj9qbhwwsjo95.png)

* **Open Applications Grid**. You can switch between all the applications you have open no matter which workspace they are on, using a grid that is spawned on screen:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wlaygc3wmwgth6n6241d.png)

* **Application Spawn Grid**. You can define a grid to spawn that can be used to open any applications that you want, using the vim-key selection:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/od0yf5slb7mq111gtp0s.png)

* **Promote Master**. In a master and stack layout, you can promote a window to be your master. You can also demote the same. It is ideal when you want to shift focus without swapping the windows entirely.

* **Move a window to every workspace**. You can copy a particular window to each and every workspace. The window will still remain in the first one but its copies will be made across every workspace. It is ideal if you are screen recording and want your front camera window to be on every workspace. You can also kill all other copies except the first one.

* **Custom window rules**. Want your Gimp to always spawn in floating mode? Or your browser to always be on the third workspace. You can do that using managed hooks.

* **Different Prompts**. You don't need to use dmenu as a run prompt. XMonad has a built in run prompt. In fact it has many other prompts, namely manpage prompt, ssh prompt among others. You can even create your own custom prompt for one liner command line outputs.

* **Key Sub-Maps**. Running out of keybindings? You can have custom key maps. For example, for opening custom prompts, you can assign 
`Mod + p`
 to prompts and subsequently press the 
`m`
 button for the manpage prompt or 
`r`
 for the run prompt. So the whole command will end up being 
`Mod + p + r`
 for the run prompt and 
`Mod + p + m`
 for the manpage prompt.


---

## At what cost?

Time! Time is the only thing you need to understand this beast and extend it to your liking. Although you can copy someone else's config, and there is nothing wrong with that, in fact it is a great way to start with XMonad, but learning the basics and being able to create your own config from scratch is an experience altogether. You don't need to be a haskell god for using it, but any functionality you want can be looked up in the awesome haskell wiki called [hackage](). It has syntactical queues and useful examples to build a config of your dreams. 


## Verdict

While XMonad is a very difficult window manager to configure in the beginning, especially if you are doing it from scratch, it is one of the most hackable, fast and reliable window managers that I have ever used. This *WM* is very old but there is a reason it is so popular even now. Some might argue that it is more suckless than dwm itself, and I agree, but it is certainly harder to setup than dwm due to the fact that you might end up writing (or copy pasting) a lot of code in a language you are likely not familiar with.

With that being said, I think I will use xmonad for another month or so before I make the next window manager hop!


| Judgement Rubric | Rating |
|:-----------------:|:------:|
| Simplicity of use | :heart: :heart: :heart: :heart: |
| Simplicity of Configuration | :heart: |
| Learning curve (lesser is better) | :heart: :heart: :heart: :heart: |
| Productivity | :heart: :heart: :heart: :heart: :heart: |
| Fun | :heart: :heart: :heart: :heart: :heart: |


---

## References

* [My XMonad Config](https://github.com/L04DB4L4NC3R/DEC/tree/master/.xmonad)
* [Derek Taylor's XMonad Config](https://gitlab.com/dwt1/dotfiles/-/tree/master/.xmonad)
* [Distrotube](https://distrotube.com/)
* [My Dotfiles](https://github.com/L04DB4L4NC3R/DEC)


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/xmonad-hackability-at-a-cost-390a)*


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

---
title: Editor Almighty
date: '2020-06-12T12:06:35.301Z'
excerpt: >-
  How my search for the perfect text editor took me to SpaceVim   What compels
  people to migrate from t...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--IUeBqACF--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/xti5km3trvkfavi5r320.png
comments_count: 2
positive_reactions_count: 6
tags:
  - vim
  - techtalks
canonical_url: 'https://dev.to/l04db4l4nc3r/editor-almighty-2de6'
layout: post
---

How my search for the perfect text editor took me to SpaceVim

> What compels people to migrate from their comfort zone? Is it boredom, monotony, or the bland impracticality of their ever so inertial state. I call it an itch, just waiting to be scratched.

This ever so inexplicable itch is what became the driving force behind my rather opinionated journey across editors.

One thing to clear right off the bat is that this blog, in no way, declares the superiority of one editor over the other, it merely explains which editor boosted _my_ productivity. Feel free to form your own opinion after reading this post. Without further ado, let us get started.

![](https://cdn-images-1.medium.com/max/1024/0*6jrTd4O_RZZrsNax)<figcaption>Photo by <a href="https://unsplash.com/@sergeytrofimov?utm_source=medium&amp;utm_medium=referral">Serghei Trofimov</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral">Unsplash</a></figcaption>

#### **What I started off with**

I started my development journey, like most people do, with a minimal and easy to use a text editor called [Atom](https://atom.io/). I soon learnt that [VSCode](https://code.visualstudio.com/) (Visual Studio Code) was all of the buzzes, and I caught that fad pretty early on. Subsequently, I was amazed at the wide array of extensions that VSCode had to offer. From VCS to advanced debugging tools, and more.

#### Why I decided to drop VSCode

- I had to depend on the mouse for navigation to an extent, even with vim bindings.
- There was no real feeling of personal satisfaction when everything was handed over in a plate (personal choice).
- I wanted something fast(er) and cheaper on my memory.
- I did a lot of development on remote servers, which didn’t have VSCode at that time (now we have [VSCodium,](https://github.com/VSCodium/vscodium) which I still don’t prefer).

#### Journey to the centre of vim

During the same time, I got interested in DevOps, and so felt a natural pull towards terminal-based editors. Emacs felt too intimidating, so the natural course took me to vim.

I was amazed at the world of opportunities that vim created for me, from granular customization to fast versatility, I couldn’t get enough of setting up my own .vimrc. Now at the same time, I had my semester finals (which obviously didn't go too well).

As my exams ended (along with a part of me), I figured out my perfect build. It included some popular plugins like:

![](https://cdn-images-1.medium.com/max/225/1*sSxN3_F2fXSxY30_0mJ-vg.png)

- [vim-go](https://github.com/fatih/vim-go.git)
- [ctrlp.vim](https://github.com/kien/ctrlp.vim.git)
- [vim-fugitive](https://github.com/tpope/vim-fugitive.git)
- [nerdtree](https://github.com/scrooloose/nerdtree.git)
- [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe.git)
- [pathogen](https://github.com/tpope/vim-pathogen.git)

And the following terminal tools (yes, I shifted to zsh):

![](https://cdn-images-1.medium.com/max/337/1*VWNcnaDGBZGas0LYqvvnKQ.png)

- [Oh my zsh](https://github.com/robbyrussell/oh-my-zsh.git)
- [terminator config](https://www.systutorials.com/docs/linux/man/5-terminator_config/)
- [zsh plugins](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins)
- [shell themes](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes)

So my environment started looking visually verbose, which is just the way I prefer:

![](https://cdn-images-1.medium.com/max/880/1*wTqHwvjDN0pc6aow5tebsQ.png)<figcaption><em>Terminator split panes with CLI tools</em></figcaption>

#### Scaling the learning curve

I had the perfect setup I wanted, especially for development and operations. It was fast, highly customizable, and intuitive. But there was still something missing. I still hadn’t memorized the vim shortcuts and had a lot of trouble staying away from the mouse while working. Trouble in paradise!

![](https://cdn-images-1.medium.com/max/1024/0*nAgkP6Cw7gxAadY4)<figcaption>Photo by <a href="https://unsplash.com/@officestock?utm_source=medium&amp;utm_medium=referral">Sebastian Herrmann</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral">Unsplash</a></figcaption>

During this time, I would occasionally switch between VSCode and vim in order to boost productivity, although it was doing more harm than good. I followed the following guidelines which helped me be 2X more productive in vim that I ever was in VSCode:

- **Restrict yourself** : Unplug your mouse, close all other editors, and no matter how slow you type, keep grinding. I was a back-end intern at [Atlan](https://atlan.com/) during this time and I didn’t even install any other editor on my work computer other than vim itself. The first week was tough, but I soon got the hang of it and subsequently became quite productive.
- **Understand rather than memorize** : In vim, all of the key bindings have a reason to be there. Understand the meaning of the commands that you are typing in. Vim will soon sound like a poem to you. For example: w means _word_ in vim and c means _change_. Doing a c + i + w over a word in vim essentially means change in word.
- **Do what works for you** : Do you want to change the key bindings? Sure, go ahead! Want to change the fonts, tab/spaces? Knock yourself out! Want to change how tiling works in vim? The world is your oyster! In the end, it is about productivity above all else. Never be afraid to seek help from others. Vim has a great community and you can learn a lot by simply watching the vim conference screen-casts on YouTube.

#### Shortcomings of vim

Fast forward a few months and I was using vim bindings everywhere, even in my [browsers](https://vimium.github.io/)! Vim showed me how typing can actually be poetic, even though you might be writing something as mundane as skeletal HTML. It had some shortcomings though:

- **Built Synchronous:** Vim (before 8.0) was built to be synchronous, which started causing a lot of problems after adding a plethora of plugins. Loading times would take seconds, even with vim v8+(might not sound like it, but actually that is very slow for an editor)!
- **Lack of out-of-the-box plugins:** There are some plugins that you got to have. For instance, [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe) is a plugin for code auto-completion and [nerdtree](https://github.com/preservim/nerdtree) is a plugin for viewing a file directory structure in vim. These are some of the extensions that should come in-built, due to the nature of their utility.
- **Requirement of explicit plugin managers:** Plugin managers like [pathogen](https://github.com/tpope/vim-pathogen), [vundle](https://github.com/VundleVim/Vundle.vim) or [plug](https://github.com/junegunn/vim-plug) are required for installing and configuring extensions in vim. This causes a lot of hassle when you are using one particular plugin but an extension only supports the other.

#### SpaceVim to the rescue!

[SpaceVim](https://spacevim.org/) is a community-driven _vim distribution._ What this essentially means is that it is a set of vim configurations which add an abstraction over vim. The following are the salient features of SpaceVim which attracted me:

- **Super easy installation:** Installing SpaceVim involves running just a single command on your terminal. You get instant gratification. Fair warning though, your existing vim configurations are going to be overwritten.
- **Asynchronous plugin manager:** SpaceVim has a [neovim](https://github.com/neovim/neovim) inspired plugin system. It only loads the most essential plugins during the initial runtime cycle and defers the loading of the rest of the plugins. This _lazy-loading_ of plugins creates a seamless typing experience for the user.

![](https://cdn-images-1.medium.com/max/961/1*kD4lZRkcUjW9tm3Q3C_NwQ.png)

- **Layer based plugin system:** SpaceVim installs plugins in layers. Each layer defines a set of plugins, grouped together to offer maximum functionality to the user, per download. Each and every plugin inside a particular layer, as well as in different layers, is downloaded asynchronously by the SpaceVim _PlugManager._
- **A plethora of off-the-shelf features:** SpaceVim comes loaded with a ton of features right of the box. From asynchronous grep on the fly, to fancy TODO managers. It brings a lot to the table in order to add value to the users’ typing experience.

![](https://cdn-images-1.medium.com/max/1024/1*US5IJBiRmZ1HaR2MbUcnCg.png)

- **Spacebar oriented:** As the name ever so discretely suggests, SpaceVim is big on using spaces as a macro for invoking a lot of in-built functionality. This is a fresh change from vim, where the spacebar has virtually no functionality in normal mode, even though it is the easiest key to hit on the keyboard, due to both its size and its stature. And no, SpaceVim has nothing to do with outer space.
- **Over 78 language packs supported:** Language packs are layers (set of plugins) which offer a lot of functionality for development in a particular language. For example, a lang# go layer will offer functionality for go development.

![](https://cdn-images-1.medium.com/max/1024/1*lwKNGzLaiRY4_rJFR0Bhrw.png)

All of these can be installed by simple adding the following lines to your **~/.SpaceVim.d/init.toml**


```
[[layers]]
name = "lang# go"
```


#### Conclusion

SpaceVim is not the endgame. Nothing is. The aim is to keep on finding, and mastering whatever boosts productivity.

> Efficiency is doing something which has already been done before, better.

> YOU are the most important resource when it comes to productivity. So choose the editor which boosts YOUR productivity. After all, no one knows better than you :)

#### References

- [Home](https://spacevim.org/)
- [vim/vim](https://github.com/vim/vim)
- [L04DB4L4NC3R/DEC](https://github.com/L04DB4L4NC3R/DEC)

* * *

This Article was originally published [on Medium](https://medium.com/gdg-vit/editor-almighty-79807100f10c) under [Developer Student Clubs VIT, Powered By Google Developers](https://dscvit.com/). [Follow us](https://medium.com/gdg-vit) on Medium.

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/editor-almighty-2de6)*


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

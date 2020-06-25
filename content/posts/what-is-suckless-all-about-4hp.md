---
title: What is suckless all about?
date: '2020-04-06T14:33:37.450Z'
excerpt: >-
  It has become appallingly obvious that our technology has exceeded our
  humanity.    — Albert Einstei...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--hCvhiRp5--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/om5fub5o8iydz6vlhgcm.jpg
comments_count: 5
positive_reactions_count: 8
tags:
  - linux
  - opensource
  - techtalks
  - discuss
canonical_url: 'https://dev.to/l04db4l4nc3r/what-is-suckless-all-about-4hp'
layout: post
---
> It has become appallingly obvious that our technology has exceeded our humanity.
>    — Albert Einstein

Ever since the culmination of the 21st century, computers are becoming more aware and humans substantially ignorant. That machine in your palm, the mobile phone, contains more computational power than an entire auditorium of machinery could fit in the early 20th century. 

Being born in the late 1990s, I have been a front-seat witness to this boom in computation. My first computer had 4 GB of RAM back in the day. Now my mobile phone alone has an 8 gig RAM chip. Humans are reduced to lazy couch sleuths living in a bubble of tools that we have taken for granted. 

The famous [Moore's law](https://en.wikipedia.org/wiki/Moore%27s_law):

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/71210fuf7p0g7vmo88ah.png)

Sadly the rise of computation has taken a perverse toll on the developer community. Do you know that an average program written in python is 2 to 10 times slower than a program written in any other compiled language (let us say C++). This is because people have simply started neglecting the time and space complexity of the algorithms they write as well as dependencies they bear in their code. No one cares about a code running 10 times slower if it yields a result in 0.04 seconds instead of 0.004 seconds. 

---

### The Suckless Philosophy

> Extreme computational capability ushers in an era of complacency in code, leading to unnecessary bloating. 

The [suckless community](https://suckless.org) is a group of like-minded people with the aim of creating software that is:

* Simple, clear and frugal.
* Minimalistic in nature to avoid bloating.
* Simple to understand and contribute to.

Suckless focuses their tools around the elites of the computer science domain, because the community believes that the aforementioned niche often gets ignored when a bloated tool tries to fit the majority. Thus working with suckless tools isn't always easy. Some of their most popular work includes the following:

* 
`dwm`
: Dynamic window manager.
* 
`st`
: A simple terminal.
* 
`surf`
: A highly minimalist web browser.

---

### Is suckless a hater community?

Let us take an example. The suckless community has the following things to say about GCC:

> GCC is the virus which has spread into nearly every Linux distribution and has added its language extensions to be not easily replacable. As of 2016 it is now written in C++ and so complete suck. Why can't a compiler just be a simple binary doing its work instead of adding path dependencies deep into the system?

A lot of people view suckless as an extremist community, who openly and rather blatantly bash other people's software in order to try and promote their own vision of how the software can *suck less*. Although a lot of their arguments can be backed up by credible evidence. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8umqcme21w0bmw91iqjb.jpg)

I was randomly browsing online when I came across this great article: [contempt culture](https://blog.aurynn.com/2015/12/16-contempt-culture) which changed my whole view about verbal extremism in the developer community, and I have since started seeing suckless as an elite community who are just trying to make better software. 

I would love to read your views about the suckless community and their tools. Also, I was contemplating whether to do a series on suckless tools. Let me know if you are interested :)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/what-is-suckless-all-about-4hp)*


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

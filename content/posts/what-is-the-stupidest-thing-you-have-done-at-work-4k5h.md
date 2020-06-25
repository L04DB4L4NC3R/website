---
title: What is the stupidest thing you have done at work?
date: '2020-05-17T17:12:52.657Z'
excerpt: >-
  This one time, I pushed some code to my branch and later on I saw that I had
  pushed the .env branch w...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--JM4CpGo7--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--oFfYpxkX--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/jfs35x8x8sm1qp5frx4j.jpg
comments_count: 7
positive_reactions_count: 3
tags:
  - discuss
  - watercooler
canonical_url: >-
  https://dev.to/l04db4l4nc3r/what-is-the-stupidest-thing-you-have-done-at-work-4k5h
layout: post
---
This one time, I pushed some code to my branch and later on I saw that I had pushed the 
`.env`
 branch with a lot of secrets on the repo. I panicked. Even more so by seeing that the 
`.env`
 file was in all of my commits for that branch. I started looking for git commands that can be used to completely erase the existence of a file from the whole commit history and found a very obsure and VERY long command which for the life of me I can't find again. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xd6yijtlwmzhst9hn0ml.jpg)

Anyways, after a copy paste later, I had created a duplicate commit for each of my commit in the tree. Each pair consisted of one commit that had the 
`.env`
 file and one that didn't. My 50 commits became 100 commits and my project lead was of course furious and curious as to why I had pushed 50 more commits at once. I explained the whole situation to him. 

Turns out they themselves had pushed the 
`.env`
 file on the master branch and all of the credentials inside it were of the development cluster. When I asked why it is so, they said that the repository is private anyway :shrug:. 

Feel free to share your stupid work story :)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/what-is-the-stupidest-thing-you-have-done-at-work-4k5h)*


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

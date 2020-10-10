---
title: 'Vim to the rescue: Human Readable Processes'
date: '2020-04-27T08:01:42.371Z'
excerpt: >-
  The What   Have you ever heard of the top command in linux. Yes, the one that
  lists out curr...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--cIiiEgLb--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/eg1skmhesxskj7dr4kqn.png
comments_count: 2
positive_reactions_count: 5
tags:
  - vim
  - tutorial
  - linux
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/vim-to-the-rescue-human-readable-processes-1fni'
layout: post
---
# The What

Have you ever heard of the **top** command in linux. Yes, the one that lists out currently running processes with a lot of other meta information about usage. A typical top command output, when piped to a file, looks like this:


```
[?1h=[?25l[H[2J(B[mtop - 16:44:50 up 1 day,  7:51,  1 user,  load average: 0.30, 0.38, 0.39(B[m[39;49m(B[m[39;49m[K
Tasks:(B[m[39;49m[1m 384 (B[m[39;49mtotal,(B[m[39;49m[1m   1 (B[m[39;49mrunning,(B[m[39;49m[1m 289 (B[m[39;49msleeping,(B[m[39;49m[1m   0 (B[m[39;49mstopped,(B[m[39;49m[1m   0 (B[m[39;49mzombie(B[m[39;49m(B[m[39;49m[K
%Cpu(s):(B[m[39;49m[1m 10.2 (B[m[39;49mus,(B[m[39;49m[1m  3.4 (B[m[39;49msy,(B[m[39;49m[1m  0.2 (B[m[39;49mni,(B[m[39;49m[1m 85.7 (B[m[39;49mid,(B[m[39;49m[1m  0.3 (B[m[39;49mwa,(B[m[39;49m[1m  0.0 (B[m[39;49mhi,(B[m[39;49m[1m  0.1 (B[m[39;49msi,(B[m[39;49m[1m  0.0 (B[m[39;49mst(B[m[39;49m(B[m[39;49m[K
KiB Mem :(B[m[39;49m[1m 16262016 (B[m[39;49mtotal,(B[m[39;49m[1m  7029368 (B[m[39;49mfree,(B[m[39;49m[1m  2042444 (B[m[39;49mused,(B[m[39;49m[1m  7190204 (B[m[39;49mbuff/cache(B[m[39;49m(B[m[39;49m[K
KiB Swap:(B[m[39;49m[1m        0 (B[m[39;49mtotal,(B[m[39;49m[1m        0 (B[m[39;49mfree,(B[m[39;49m[1m        0 (B[m[39;49mused.(B[m[39;49m[1m 13593976 (B[m[39;49mavail Mem (B[m[39;49m(B[m[39;49m[K
[K
[7m  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                  (B[m[39;49m[K
(B[m 1527 root      20   0    4552    784    724 S   6.2  0.0   0:07.06 acpid                                                                                                    (B[m[39;49m[K
(B[m 1985 redis     20   0   51444   3632   2564 S   6.2  0.0   0:33.44 redis-server                                                                                             (B[m[39;49m[K
(B[m 3336 angad     20   0  533196  95444  71856 S   6.2  0.6  14:36.86 Xorg                                                                                                     (B[m[39;49m[K
(B[m[1m 4084 angad     20   0   57972   4380   3508 R   6.2  0.0   0:00.02 top                                                                                                      (B[m[39;49m[K
(B[m 4729 angad     20   0  863236 195212 119392 S   6.2  1.2   3:44.26 chrome     
TLDR;
```


Whoa! A lot of information being thrown here, but not exactly human readable. Sometimes when I am using a tool in linux, I often spin up the *OG* top command to look at how much the tool is using my memory as compared to other processes. I want a clear readable format which I can use to view the result of the top command so that I can embed it wherever I like, be it a blog or an issue. Basically I want something like this:

---

* top - 00:26:50 up 15:33
	*  1 user
	*  load average: 0.34
	* 0.69
	* 0.84
* Tasks: 370 total
	*   1 running
	* 279 sleeping
	*   0 stopped
	*   0 zombie
* %Cpu(s):  5.2 us
	*  1.5 sy
	*  0.1 ni
	* 92.3 id
	*  0.8 wa
	*  0.0 hi
	*  0.1 si
	*  0.0 st
* KiB Mem : 16262016 total
	*  9118020 free
	*  1652820 used
	*  5491176 buff/cache
* KiB Swap:
	* 0 total
	* 0 free
	* 0 used. 14034404 avail Mem 

|PID|USER|PR|NI|VIRT|RES|SHR|S|%CPU|%MEM|TIME+|COMMAND|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|15353|angad|20|0|57824|4240|3476|R|12.5|0.0|0:00.02|top|
|15312|angad|20|0|273360|34332|12680|S|6.2|0.2|0:00.24|vim|
|1|root|20|0|225944|9512|6544|S|0.0|0.1|0:42.51|systemd|
|2|root|20|0|0|0|0|S|0.0|0.0|0:00.07|kthreadd|
|4|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|kworker/0:+|
|6|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|mm_percpu_+|
|7|root|20|0|0|0|0|S|0.0|0.0|0:00.12|ksoftirqd/0|
|8|root|20|0|0|0|0|I|0.0|0.0|0:30.62|rcu_sched|
|9|root|20|0|0|0|0|I|0.0|0.0|0:00.00|rcu_bh|

---

Aaah now this is more like it. Informative yet soothing to the eyes. Often, data visualization is limited by the perceptive short term memory load by the sheer volume of the displayed information. More times than not, we can mould the information a certain way so that it is more perceptive. Markdown comes to the rescue here!


---

# The How

In this series, I am going to tell you how I converted the garbled top command output to a human readable form using the following steps:

* [What to work with](# what-to-work-with)
* [Converting metadata to a list](# converting-metadata-to-a-list)
* [Converting process data to a table](# converting-process-data-to-a-table)
* [What lies ahead](# what-lies-ahead)

---

## What to work with

First we need to pipe the output of the top command into a file. What I like to use is the following command:


```sh
top -d 5 -n 1 -b | grep "load average" -A 15 > myfile
```


* 
`-d`
: This is the delay time interval (5 seconds here)
* 
`-n`
: This specifies the number of cycles to run. Since we only want a snapshot, we specify 1.
* 
`-b`
: Notice that when piped to a file, the top command prints out a lot of control characters. This can be avoided by using batch mode, which removes there characters for further processing.
* Whatever comes after the pipe is to make sure we only get a specified number of lines in the top output (15 here). We can specify any number here, or remove this option for the full top output
* We are using the 
`>`
 symbol to take the output and pipe it to a file called **myfile**. Use vim to open this file, and we will proceed.

---

## Converting metadata to a list

We talked about macros in the last entry of this series. We are going to create a macro for converting the first section of the top command to a bulleted list. 


```
top - 17:06:25 up 1 day,  8:13,  1 user,  load average: 0.25, 0.35, 0.39
Tasks: 380 total,   1 running, 287 sleeping,   0 stopped,   0 zombie
%Cpu(s):  8.8 us,  2.9 sy,  0.2 ni, 87.7 id,  0.3 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem : 16262016 total,  7259032 free,  1811312 used,  7191672 buff/cache
KiB Swap:        0 total,        0 free,        0 used. 13827644 avail Mem 
```
 

Press **q + a** to start recording the macro in the **a** key. The following set of functions need to be performed sequentially:

* Find all commas and add a new line instead, with a tab and a *, to specify that the item is a sub element of the list:


```vim
:%s/,/\r\t\*/g
```


Note that here we have used the 
`\r`
 symbol instead of 
`\n`
 as \n appends an extra character at the end of the newline. 
`g`
 is used to specify that this action needs to be performed on every occurrence of 
`,`
 in a line.

* Cleanup the extra space in the last point:


```
KiB Swap:        0 total
	*        0 free
	*        0 used. 13797256 avail Mem 
```


For this, search for Kib, then delete the space till the 
`0`
 reaches the 
`:`
 and press enter to go into a new line. Insert a *. Cleanup the extra space in the last two fields also. To get this:


```
KiB Swap:
	*  0 total
	*  0 free
	*  0 used. 13797256 avail Mem 
```


* Insert a bullet behind every field by searching and pre-pending the line with a *. 

Now we have something that looks like this:

* top - 00:26:50 up 15:33
	*  1 user
	*  load average: 0.34
	* 0.69
	* 0.84
* Tasks: 370 total
	*   1 running
	* 279 sleeping
	*   0 stopped
	*   0 zombie
* %Cpu(s):  5.2 us
	*  1.5 sy
	*  0.1 ni
	* 92.3 id
	*  0.8 wa
	*  0.0 hi
	*  0.1 si
	*  0.0 st
* KiB Mem : 16262016 total
	*  9118020 free
	*  1652820 used
	*  5491176 buff/cache
* KiB Swap:
	* 0 total
	* 0 free
	* 0 used. 14034404 avail Mem 

We have our first section done and recorded in macro 'a'. To paste the contents of the macro in the current file, you can do 
`" + a + p`
. You can use this output to create your custom function for performing the actions specified and adding them to a keybinding if you want.

---

## Converting process data to a table

Under a metaphorical microscope, when we highlight all of the hidden characters, the process data looks something like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2rclg3iqfe6xm4jnoum5.png)

Converting this to a table format will include the following steps:

* Search for "PID" using 
`/PID`
.
* Paste the following line below the line that contains PID:


```
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
```

* Since we will be replacing spaces with 
`|`
 to make a table, we have to make sure none of our process names have spaces. Till now I have only seen the 
`Web Content`
 process having a space. Simply replace it:


```vim
:%s/Web Content/Web-Content/g 
```


* Go to the line with PID. Now from that line till the end of the document delete the space from each line beginning:


```vim
" The + suggests that match one or more space
" .,$ means from current line till the end of the document
:.,$s/^\s\+//
```


* Convert each line ending to a 
`|`
:


```vim
" $ is the line ending character
:.,$s/$/|/
```


* Convert each line beginning with a 
`|`
:


```vim
" ^ is the line beginning character
:.,$s/^/|/
```


* Convert one or more spaces to a 
`|`
:


```vim
:.,$s/\s\+/|/g
```


And you are good to go. The process data now looks like this:


```
|PID|USER|PR|NI|VIRT|RES|SHR|S|%CPU|%MEM|TIME+|COMMAND|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|15353|angad|20|0|57824|4240|3476|R|12.5|0.0|0:00.02|top|
|15312|angad|20|0|273360|34332|12680|S|6.2|0.2|0:00.24|vim|
|1|root|20|0|225944|9512|6544|S|0.0|0.1|0:42.51|systemd|
|2|root|20|0|0|0|0|S|0.0|0.0|0:00.07|kthreadd|
|4|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|kworker/0:+|
|6|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|mm_percpu_+|
|7|root|20|0|0|0|0|S|0.0|0.0|0:00.12|ksoftirqd/0|
|8|root|20|0|0|0|0|I|0.0|0.0|0:30.62|rcu_sched|
|9|root|20|0|0|0|0|I|0.0|0.0|0:00.00|rcu_bh|
```


Which is exactly the format We wanted. The table will render in markdown like this:

|PID|USER|PR|NI|VIRT|RES|SHR|S|%CPU|%MEM|TIME+|COMMAND|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|15353|angad|20|0|57824|4240|3476|R|12.5|0.0|0:00.02|top|
|15312|angad|20|0|273360|34332|12680|S|6.2|0.2|0:00.24|vim|
|1|root|20|0|225944|9512|6544|S|0.0|0.1|0:42.51|systemd|
|2|root|20|0|0|0|0|S|0.0|0.0|0:00.07|kthreadd|
|4|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|kworker/0:+|
|6|root|0|-20|0|0|0|I|0.0|0.0|0:00.00|mm_percpu_+|
|7|root|20|0|0|0|0|S|0.0|0.0|0:00.12|ksoftirqd/0|
|8|root|20|0|0|0|0|I|0.0|0.0|0:30.62|rcu_sched|
|9|root|20|0|0|0|0|I|0.0|0.0|0:00.00|rcu_bh|

---

## What lies ahead

You can check out the plugin I made for the same purpose here: 


<iframe class="liquidTag" src="https://dev.to/embed/github?args=L04DB4L4NC3R%2Ftop.vim" style="border: 0; width: 100%;"></iframe>


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/vim-to-the-rescue-human-readable-processes-1fni)*


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

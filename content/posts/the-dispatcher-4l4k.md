---
title: The Dispatcher
date: '2019-05-05T10:24:07.618Z'
excerpt: Introduction
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--FsEbuRyl--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/8snhnbtdskfpg90wtlyi.jpg
comments_count: 1
positive_reactions_count: 6
tags:
  - os
  - computerscience
canonical_url: 'https://dev.to/l04db4l4nc3r/the-dispatcher-4l4k'
layout: post
---



**Introduction**

Lets say you are an employee looking for that A+ in your appraisal. Now the boss selects you for a super important project. Feeling special? The boss, by this metaphor, is a task scheduler. Now a dispatcher is someone who gives you suitcase full of briefing letters related to the project and opens the door for you with a pat on your back!

Lets call him pat-man for reference.

Your computer is an interesting piece of hardware, but holds an even more spectacular piece of software, nay, an array of processes working together. to make it feel like just one big software. But these processes need to communicate. Moreover, they need to coordinate their temporal cohesiveness. That’s where the schedulers and dispatchers come in.

**Process states in an operating system**

A process in an operating system has 5 states associated with it:

*   
`New`
: When a new process is created
*   
`Ready`
: When the process is ready for execution
*   
`Running`
: When the process is running
*   
`Waiting`
: When the process is waiting for another process, or an I/O task to complete
*   
`Terminated`
: When the process ends

![process states](https://thepracticaldev.s3.amazonaws.com/i/5okde6cbdpmvg00evzo5.jpeg)

Note that there is a waiting queue and a ready queue associated with all of the processes.

The waiting queue consists of a list of all of the processes that are waiting to be dispatched. When the processes are ready to execute, they are pushed into the ready queue.

The **short term scheduler** runs in the CPU and is used for selecting a single process from the ready queue for execution.

![scheduling and dispatching processes with queues](https://thepracticaldev.s3.amazonaws.com/i/qco1p2gogb0xn98ixjvg.png)

**The dispatcher**

A process dispatcher gives control of the CPU to a process selected by the short term scheduler.

Rewind back to the introduction where we said that your boss was the scheduler and the pat-man was the dispatcher. Note that the boss selected you but it was the pat-man who actually opened the door for you and gave you the resources to operate. Similarly, dispatchers can allocate threads to processes and CPU to the threads.

A dispatcher has the following responsibilities:

*   **Switching to user mode**: All of the low level operating system processes run on the kernel level security access, but all of the application code and user issued processes run in the application space or the user permission mode. Dispatcher switches the processes to the user mode.
*   **Addressing:** The program counter (PC) register points towards the next process that is to be executed. The dispatcher is responsible for addressing that address.
*   **Initiation of context switch:** A context switch is when a currently running process is halted and all of its data and its process control block (PCB) are stored in main memory, and another process is loaded in its place for execution.
*   **Managing dispatch latency:** Dispatch latency is calculated as the time it takes to stop one process and start another. The lower the dispatch latency, the more efficient the software for the same hardware configuration.

> Note that a dispatcher is NOT a thread. The dispatcher runs on each core, runs a thread for a while, saves its state, loads the state of another thread and runs it.

**Selection of processes for dispatch**

The dispatcher can select processes in the following ways:

![ready queue](https://thepracticaldev.s3.amazonaws.com/i/y0cgwhn7ugz0sgsm2xeo.png)

*   Search the table from the front and run the first ready thread.

![ready queue](https://thepracticaldev.s3.amazonaws.com/i/sro2d9xctq8da48jdbis.png)

*   Dispatch one thread from the queue and run it. If the process is not completed, insert it at the back of the queue.

![priority based ready queues](https://thepracticaldev.s3.amazonaws.com/i/i4fo5k7416mu62kw8qr6.png)

*   Give each thread a priority and organize the priority queues accordingly.

![priority based multiple queues](https://thepracticaldev.s3.amazonaws.com/i/io79i1c35n2rcm52fdqn.png)
priority based multiple queues

*   Have multiple queues for each priority class. Whenever some threads are ready for execution chose the one with the highest priority and run it.

![](https://thepracticaldev.s3.amazonaws.com/i/047fj5ubxhwgaiy5snzf.png)

**Stopping processes and managing dispatcher failure**

If a thread is executing and the dispatcher isn’t, it means that the operating system has lost control. In that case the following recovery mechanisms can be employed:

**Traps:** Traps are essentially events in the operating system which cause a state switch into the operating system. Traps allow execution of a program or task to be continued without loss of program continuity. The return address for the trap handler points to the instruction to be executed after the trapping instruction. They can be used to catch arithmetic errors.

*   
`System calls`
: System calls is an application programming interface through which processes running in user mode can communicate with the kernel mode to leverage operating system specific functionalities like signalling or killing processes.
*   
`Page Fault`
: A page fault occurs when a program attempts to access data or code that is in its address space, but is not currently located in the system.

**Interrupts:** Events occurring outside the current thread that causes a state switch in the operating system. eg: timers, completion of disk operations etc. They can be used to stop running processes.

> Interrupts are hardware interrupts like the completion of I/O events while traps are software-invoked interrupts like division by 0. Both traps and interrupts are asynchronous and are used as signalling or recovery mechanisms by the OS in case of a dispatch failure.

**Conclusion**

![](https://thepracticaldev.s3.amazonaws.com/i/4tsqffvin8walzp50yse.jpg)


A dispatcher is an integral part of an operating system. It is responsible for maintaining the ready queue and making sure each ready process gets dispatched to utilize the CPU.

Dispatcher is also being used in other systems like sophisticated small-talk messaging systems, and in object oriented programming as dynamic dispatchers. It is time someone patted the pat-man on the back!

**Further reading**

[**What is the difference between Trap and Interrupt?**](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt)

[**A Compact Task Dispatcher for Embedded Systems.pdf**](https://drive.google.com/file/d/0Bw1wxZHj3VakNnZ3eFVEbUhWZ2s/view)

[**Implementing an Asynchronous Dispatch Queue**](https://embeddedartistry.com/blog/2017/2/1/c11-implementing-a-dispatch-queue-using-stdfunction)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/the-dispatcher-4l4k)*


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

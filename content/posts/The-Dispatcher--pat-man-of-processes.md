---
title: 'The Dispatcher: pat-man of processes'
date: '2019-05-05T10:24:07.618Z'
thumb_img_path: https://miro.medium.com/max/4320/0*q4BAxzKfOSzua7L-
excerpt: Introduction
layout: post
---
![](/images/The-Dispatcher--pat-man-of-processes/0*q4BAxzKfOSzua7L-.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@chillarea?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@chillarea?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">sebastiaan stam</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

**Introduction**

Lets say you are an employee looking for that A+ in your appraisal. Now the boss selects you for a super important project. Feeling special? The boss, by this metaphor, is a task scheduler. Now a dispatcher is someone who gives you suitcase full of briefing letters related to the project and opens the door for you with a pat on your back!

Lets call him pat-man for reference.

Your computer is an interesting piece of hardware, but holds an even more spectacular piece of software, nay, an array of processes working together. to make it feel like just one big software. But these processes need to communicate. Moreover, they need to coordinate their temporal cohesiveness. That’s where the schedulers and dispatchers come in.

**Process states in an operating system**

A process in an operating system has 5 states associated with it:

*   `New`: When a new process is created
*   `Ready`: When the process is ready for execution
*   `Running`: When the process is running
*   `Waiting`: When the process is waiting for another process, or an I/O task to complete
*   `Terminated`: When the process ends

![](/images/The-Dispatcher--pat-man-of-processes/1*tovTQ0iXuLiN3kNr6_Zwyg.jpeg)

<figcaption>process states</figcaption>

Note that there is a waiting queue and a ready queue associated with all of the processes.

The waiting queue consists of a list of all of the processes that are waiting to be dispatched. When the processes are ready to execute, they are pushed into the ready queue.

The **short term scheduler** runs in the CPU and is used for selecting a single process from the ready queue for execution.

![](/images/The-Dispatcher--pat-man-of-processes/1*gCqlPlb-TRTxZ9_TKUVLZw.png)

<figcaption>scheduling and dispatching processes with&nbsp;queues</figcaption>

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

![](/images/The-Dispatcher--pat-man-of-processes/0*_50rq5dId0RbMLrI.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@kylejglenn?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@kylejglenn?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Kyle Glenn</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

The dispatcher can select processes in the following ways:

![](/images/The-Dispatcher--pat-man-of-processes/1*n5hud1t_Q5Xnc5DQ_-OcZQ.png)

<figcaption>ready queue</figcaption>

*   Search the table from the front and run the first ready thread.

![](/images/The-Dispatcher--pat-man-of-processes/1*gxcykEnF-wY5LwRBcff39A.png)

<figcaption>ready queue</figcaption>

*   Dispatch one thread from the queue and run it. If the process is not completed, insert it at the back of the queue.

![](/images/The-Dispatcher--pat-man-of-processes/1*0QNm5BSKtzNE_IUCKGRXkw.png)

<figcaption>priority based ready&nbsp;queues</figcaption>

*   Give each thread a priority and organize the priority queues accordingly.

![](/images/The-Dispatcher--pat-man-of-processes/1*szLfCGr2p4qAlJBzITVVNw.png)

<figcaption>priority based multiple&nbsp;queues</figcaption>

*   Have multiple queues for each priority class. Whenever some threads are ready for execution chose the one with the highest priority and run it.

![](/images/The-Dispatcher--pat-man-of-processes/1*JThWQubVoZ57pnOYTtsAug.png)

**Stopping processes and managing dispatcher failure**

If a thread is executing and the dispatcher isn’t, it means that the operating system has lost control. In that case the following recovery mechanisms can be employed:

**Traps:** Traps are essentially events in the operating system which cause a state switch into the operating system. Traps allow execution of a program or task to be continued without loss of program continuity. The return address for the trap handler points to the instruction to be executed after the trapping instruction. They can be used to catch arithmetic errors.

*   `System calls`: System calls is an application programming interface through which processes running in user mode can communicate with the kernel mode to leverage operating system specific functionalities like signalling or killing processes.
*   `Page Fault`: A page fault occurs when a program attempts to access data or code that is in its address space, but is not currently located in the system.

**Interrupts:** Events occurring outside the current thread that causes a state switch in the operating system. eg: timers, completion of disk operations etc. They can be used to stop running processes.

> Interrupts are hardware interrupts like the completion of I/O events while traps are software-invoked interrupts like division by 0. Both traps and interrupts are asynchronous and are used as signalling or recovery mechanisms by the OS in case of a dispatch failure.

**Conclusion**

![](/images/The-Dispatcher--pat-man-of-processes/0*cuAdFAh5S_Z3fFra.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@milkovi?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@milkovi?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">MILKOVÍ</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

A dispatcher is an integral part of an operating system. It is responsible for maintaining the ready queue and making sure each ready process gets dispatched to utilize the CPU.

Dispatcher is also being used in other systems like sophisticated small-talk messaging systems, and in object oriented programming as dynamic dispatchers. It is time someone patted the pat-man on the back!

**Further reading**

[**What is the difference between Trap and Interrupt?**  
*Thanks for contributing an answer to Stack Overflow! Please be sure to answer the question. Provide details and share…*stackoverflow.com](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt "https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt")[](https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt)

[**A Compact Task Dispatcher for Embedded Systems.pdf**  
*Edit description*drive.google.com](https://drive.google.com/file/d/0Bw1wxZHj3VakNnZ3eFVEbUhWZ2s/view "https://drive.google.com/file/d/0Bw1wxZHj3VakNnZ3eFVEbUhWZ2s/view")[](https://drive.google.com/file/d/0Bw1wxZHj3VakNnZ3eFVEbUhWZ2s/view)

[**Implementing an Asynchronous Dispatch Queue**  
*Updated: 20190201 Previously, I introduced the concept of dispatch queues. Here's a quick review of what a dispatch…*embeddedartistry.com](https://embeddedartistry.com/blog/2017/2/1/c11-implementing-a-dispatch-queue-using-stdfunction "https://embeddedartistry.com/blog/2017/2/1/c11-implementing-a-dispatch-queue-using-stdfunction")[](https://embeddedartistry.com/blog/2017/2/1/c11-implementing-a-dispatch-queue-using-stdfunction)

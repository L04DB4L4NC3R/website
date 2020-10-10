---
title: Process synchronization monitors in go
date: '2019-05-03T05:59:04.681Z'
excerpt: Introduction
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--tOXWpz4j--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://thepracticaldev.s3.amazonaws.com/i/s7x5jswmrdfkx247686o.jpeg
comments_count: 0
positive_reactions_count: 8
tags:
  - go
  - os
  - computerscience
canonical_url: 'https://dev.to/l04db4l4nc3r/process-synchronization-monitors-in-go-4g4k'
layout: post
---


**Introduction**

In the most recent times, programming has taken its fifth gear by leveraging process synchronization constructs to achieve thread level optimization. Popular languages like Java, python, support multi-threading. But control flow is often blurred in the process of achieving maximum concurrent throughput.

![single threaded v/s multi-threaded processes](https://thepracticaldev.s3.amazonaws.com/i/yqpxzuclxgrk59jnehzn.png)
single threaded v/s multi-threaded processes

**Semaphores**

Semaphores are low level constructs which mainly have two methods defined on them. 
`Wait()`
 and 
`Signal()`
 . Semaphores make sure that the critical section of your code is atomic. Which means that in essence, shared memory cohesiveness should be sequential when two threads are trying to access it at the same time.

One thread acquires the lock, performs its critical section and then releases the lock for the other threads. In the meantime, all of the other threads are waiting in queue.

![semaphores in action](https://thepracticaldev.s3.amazonaws.com/i/5wgksg7hn1rumv5o77lb.png)

**Monitors**

A Monitor is a high level process synchronization construct which abstracts away all of the timing information. It holds conditionals, shared memory, and timing information all under the same hood.

A Monitor class is an abstract data type which contains shared data variables and procedures. The variables are private and cannot be accessed from outside of the construct, only its procedures can access the variables. Only one thread can access a monitor class object at one time.

![_Monitor class_](https://thepracticaldev.s3.amazonaws.com/i/7ar0fcaqxmxkcun3blch.png)

**Monitors in go**

We are going to construct a monitor interface which has all of the necessary functions required. Subsequently we are going to be creating a construct that satisfies the monitor interface and define the methods on it.

Create a file 
`main.go`



```go
package main

import (  
 "fmt"  
 "sync"  
)

type Monitor interface {  
 Wait()  
 Signal()  
 GetData() \[\]string  
 PutData(string)  
}

type Words struct {  
 mutex         \*sync.Mutex  
 wordsArray    \[\]string  
 isInitialized bool  
}

func (m \*Words) Init() {  
 m.mutex = &sync.Mutex{}  
 m.wordsArray = \[\]string{}  
 m.isInitialized = true  
}
```


Here our Words struct satisfies the monitor interface. All of the member variables are private. Our task is to append words in an array atomically. Note that this is not an ideal use case for monitors but serves as a good example of the same.

Since we cannot access the member variables of the Words class we will be defining fetchers and getters on it.

*   **GetData() \[\]string :** GetData function simple returns the whole array of words
*   **PutData(string) :** PutData function takes in a word as an argument and then atomically appends it to the array.

Now we are going to be defining the remaining functions


```go
func (m \*Words) Wait() {  
 if m.isInitialized {  
  m.mutex.Lock()  
 }  
}

func (m \*Words) Signal() {  
 if m.isInitialized {  
  m.mutex.Unlock()  
 }  
}

func (m \*Words) GetData() \[\]string { return m.wordsArray }

func (m \*Words) PutData(word string) {  
 m.Wait()

// critical section  
 m.wordsArray = append(m.wordsArray, word)  
 // critical section done

m.Signal()  
}
```


A monitor clubs together timing and control information. Here only initialized structs will be able to acquire the lock.

*   **Wait() :** The wait function acquires the mutex (mutual exclusion) lock if the member variables are defined
*   **Signal() :** The signal function releases the acquired lock so that the other threads can acquire it.

Our main function looks like this


```go
func main() {  
 m := &Words{}  
 m.Init()

wg := &sync.WaitGroup{}  
 wg.Add(2)  
 go func() {  
  defer wg.Done()  
  m.PutData("Angad")  
 }()  
 go func() {  
  defer wg.Done()  
  m.PutData("Sharma")  
 }()  
 wg.Wait()  
 fmt.Println(m.GetData())  
}
```


Here we have initialized our Words struct and all of the member variables in it. Then we have started two goroutines to append words into the array. After the operation is done, we simply print out the whole array.

Output:

```
[Sharma Angad]
```


**Application of monitors**

*   Producer-consumer problem: One process produces data and the other process utilizes that data. Synchronization is required between the processes.
*   Dining-philosopher problem: K number of philosophers have chopsticks in front of them. They require 2 chopsticks to eat. They need to choose between thinking and eating according to their peers.
*   File read-write problem: Monitors can be used to prevent 
`read-after-write`
, 
`write-after-read`
, and 
`write-after-write`
 problems.

**Conclusion**

> Monitors are useful data structures used to encapsulate all of the control information, timing information, and shared data under one roof. They are an abstraction over semaphores where we can define control statements over mutual exclusion.

![Monitors](https://thepracticaldev.s3.amazonaws.com/i/o0ez6rin7gdct4n1uaxb.jpeg)

**Further reading**

[**Dining Philosopher Problem Using Semaphores**](https://www.geeksforgeeks.org/operating-system-dining-philosopher-problem-using-semaphores/)

[**L04DB4L4NC3R/go-monitors**](https://github.com/L04DB4L4NC3R/go-monitors.git)

[**Difference Between Semaphore and Monitor in OS**](https://techdifferences.com/difference-between-semaphore-and-monitor-in-os.html)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/process-synchronization-monitors-in-go-4g4k)*


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

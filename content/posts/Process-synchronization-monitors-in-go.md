---
title: Process synchronization monitors in go
date: '2019-05-03T05:59:04.681Z'
thumb_img_path: https://miro.medium.com/max/1400/1*TBwzZzVwY-uKttHPkWSLTA.png
excerpt: Introduction
layout: post
---
**Introduction**

In the most recent times, programming has taken its fifth gear by leveraging process synchronization constructs to achieve thread level optimization. Popular languages like Java, python, support multi-threading. But control flow is often blurred in the process of achieving maximum concurrent throughput.

![](/images/Process-synchronization-monitors-in-go/1*TBwzZzVwY-uKttHPkWSLTA.png)

<figcaption>single threaded v/s multi-threaded processes</figcaption>

**Semaphores**

Semaphores are low level constructs which mainly have two methods defined on them. `Wait()` and `Signal()` . Semaphores make sure that the critical section of your code is atomic. Which means that in essence, shared memory cohesiveness should be sequential when two threads are trying to access it at the same time.

One thread acquires the lock, performs its critical section and then releases the lock for the other threads. In the meantime, all of the other threads are waiting in queue.

![](/images/Process-synchronization-monitors-in-go/1*TWzSKQpRGP8XCERn7bbq3A.png)

<figcaption>semaphores in&nbsp;action</figcaption>

**Monitors**

A Monitor is a high level process synchronization construct which abstracts away all of the timing information. It holds conditionals, shared memory, and timing information all under the same hood.

A Monitor class is an abstract data type which contains shared data variables and procedures. The variables are private and cannot be accessed from outside of the construct, only its procedures can access the variables. Only one thread can access a monitor class object at one time.

![](/images/Process-synchronization-monitors-in-go/1*ejATMAEWA85TntZZzrkdzw.png)

<figcaption><em>Monitor class</em></figcaption>

**Monitors in go**

We are going to construct a monitor interface which has all of the necessary functions required. Subsequently we are going to be creating a construct that satisfies the monitor interface and define the methods on it.

Create a file `main.go`

    package main
    import (  
     "fmt"  
     "sync"  
    )
    type Monitor interface {  
     Wait()  
     Signal()  
     GetData() []string  
     PutData(string)  
    }
    type Words struct {  
     mutex         *sync.Mutex  
     wordsArray    []string  
     isInitialized bool  
    }
    func (m *Words) Init() {  
     m.mutex = &sync.Mutex{}  
     m.wordsArray = []string{}  
     m.isInitialized = true  
    }

Here our Words struct satisfies the monitor interface. All of the member variables are private. Our task is to append words in an array atomically. Note that this is not an ideal use case for monitors but serves as a good example of the same.

Since we cannot access the member variables of the Words class we will be defining fetchers and getters on it.

*   **GetData() \[\]string :** GetData function simple returns the whole array of words
*   **PutData(string) :** PutData function takes in a word as an argument and then atomically appends it to the array.

Now we are going to be defining the remaining functions

    func (m *Words) Wait() {  
     if m.isInitialized {  
      m.mutex.Lock()  
     }  
    }
    func (m *Words) Signal() {  
     if m.isInitialized {  
      m.mutex.Unlock()  
     }  
    }
    func (m *Words) GetData() []string { return m.wordsArray }
    func (m *Words) PutData(word string) {  
     m.Wait()
    // critical section  
     m.wordsArray = append(m.wordsArray, word)  
     // critical section done
    m.Signal()  
    }

A monitor clubs together timing and control information. Here only initialized structs will be able to acquire the lock.

*   **Wait() :** The wait function acquires the mutex (mutual exclusion) lock if the member variables are defined
*   **Signal() :** The signal function releases the acquired lock so that the other threads can acquire it.

Our main function looks like this

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

Here we have initialized our Words struct and all of the member variables in it. Then we have started two goroutines to append words into the array. After the operation is done, we simply print out the whole array.

Output:

    [Sharma Angad]

**Application of monitors**

*   Producer-consumer problem: One process produces data and the other process utilizes that data. Synchronization is required between the processes.
*   Dining-philosopher problem: K number of philosophers have chopsticks in front of them. They require 2 chopsticks to eat. They need to choose between thinking and eating according to their peers.
*   File read-write problem: Monitors can be used to prevent `read-after-write`, `write-after-read`, and `write-after-write` problems.

**Conclusion**

> Monitors are useful data structures used to encapsulate all of the control information, timing information, and shared data under one roof. They are an abstraction over semaphores where we can define control statements over mutual exclusion.

![](/images/Process-synchronization-monitors-in-go/1*f9Az-JtUUhn_BrAQYag6VA.jpeg)

**Further reading**

[**Operating System | Dining Philosopher Problem Using Semaphores - GeeksforGeeks**  
*Prerequisite - Process Synchronization, Semaphores, Dining-Philosophers Solution Using Monitors The Dining Philosopher…*www.geeksforgeeks.org](https://www.geeksforgeeks.org/operating-system-dining-philosopher-problem-using-semaphores/ "https://www.geeksforgeeks.org/operating-system-dining-philosopher-problem-using-semaphores/")[](https://www.geeksforgeeks.org/operating-system-dining-philosopher-problem-using-semaphores/)

[**L04DB4L4NC3R/go-monitors**  
*Contribute to L04DB4L4NC3R/go-monitors development by creating an account on GitHub.*github.com](https://github.com/L04DB4L4NC3R/go-monitors.git "https://github.com/L04DB4L4NC3R/go-monitors.git")[](https://github.com/L04DB4L4NC3R/go-monitors.git)

[**Difference Between Semaphore and Monitor in OS (with Comparison Chart) - Tech Differences**  
*Semaphore and Monitor both allow processes to access the shared resources in mutual exclusion. Both are the process…*techdifferences.com](https://techdifferences.com/difference-between-semaphore-and-monitor-in-os.html "https://techdifferences.com/difference-between-semaphore-and-monitor-in-os.html")[](https://techdifferences.com/difference-between-semaphore-and-monitor-in-os.html)

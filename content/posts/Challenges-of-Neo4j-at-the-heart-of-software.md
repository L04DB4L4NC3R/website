---
title: Challenges of Neo4j at the heart of software
date: '2019-08-30T20:32:31.864Z'
thumb_img_path: https://miro.medium.com/max/4320/0*GgqQ5x90-Br5JnMC
excerpt: Introduction
layout: post
---
![](/images/Challenges-of-Neo4j-at-the-heart-of-software/0*GgqQ5x90-Br5JnMC.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@maxvdo?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@maxvdo?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Max van den Oetelaar</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

**Introduction**

Neo4j is a noSQL database which stores and represents data in the form of graphs. Each node of the graph has a specific tag which is used to identify the type of node. Edges between two nodes specify the relationship between the two nodes. The best use case of neo4j is in the case of highly embedded relational queries.

Note, you can read my article on [setting up a go-neo4j ecosystem](https://medium.com/@angadsharma1016/optimizing-go-neo4j-concurrency-patterns-810dff25f88f) as a primer.

**Hurdles to adoption**

I started working on one of my biggest projects around last year. Since my learning mechanism solely revolves around using new technologies in real life projects, I was pretty keen on giving graph databases a go. It was then that I came across what came to be the backbone of my project, neo4j. But getting to this point wasn’t easy, mainly because of the following hurdles:

*   Lack of comprehensive documentation around neo4j drivers in golang (which my project was being written in).
*   Overall write-performance issues relative to SQL databases.
*   Lack of sophisticated indexing mechanisms.
*   Garbage collection pauses.

![](/images/Challenges-of-Neo4j-at-the-heart-of-software/0*BWGjrqubK7uIDc06.png)

**Understanding the WHY**

Neo4j is a read friendly database. Which means that it is extremely fast when it comes to reading data. So much so that it paves a path to real time graph use cases.

While being read friendly, writes still come at a cost. Mainly because of the following reasons:

*   Neo4j follows a master-slave architecture and writes are always done on the master. Even if you try to write on a slave, it will internally be cascaded to the master. When the master dies, a new one is elected automatically.

![](/images/Challenges-of-Neo4j-at-the-heart-of-software/0*GWHICvIuO5qKOQzM.jpg)

*   All data resides on each machine. This is to protect referential integrity. Once data set search queries become larger than the available RAM, the system will slow down dramatically.
*   Neo4j is also not optimized for searching. Very much so when compared with technologies such as elasticsearch.
*   See the point about garbage collector pauses [here](https://qr.ae/TWrgCn)

**Solving some of the problems at the application level**

To solve the problem of write latency, I made sure that all of the functions I wrote executed concurrently. But this didn’t stop the fact that there was still a bottleneck because writes are always done on one node. This raised the issue of mutual exclusion.

While neo4j does not offer read locks on data, it does so for writes. But the locks are explicit in a lot of driver implementations. So I spent a lot of time debugging my code and fishing for errors which caused my bulk writes to crash. I then implemented `mutex locks` in the application layer itself. It was as simple as doing the following:

    `// create a new node with given label and participant data struct (FOR COORDINATORS)  
    func CreateParticipant(e Event, label string, c chan error, mutex *sync.Mutex) {`
     `mutex.Lock()`
     `// Critical section begins`
     ``_, err := con.ExecNeo(`MATCH(a:EVENT) WHERE a.name=$EventName  
        CREATE (n:INCHARGE {name:$name, registrationNumber:$registrationNumber,  
            email:$email, phoneNumber:$phoneNumber, gender: $gender})<-[:`+label+`]-(a) `, map[string]interface{}{  
            "EventName":          e.Name,  
            "name":               e.GetField(label, "Name"),  
            "registrationNumber": e.GetField(label, "RegistrationNumber"),  
            "email":              e.GetField(label, "Email"),  
            "phoneNumber":        e.GetField(label, "PhoneNumber"),  
            "gender":             e.GetField(label, "Gender"),  
        })  
        if err != nil {  
            c <- err  
            return  
        }``
     `// Critical section ends`
     `mutex.Unlock()`
     `log.Printf("Created %s node", label)  
        c <- nil  
        return  
    }`

This gave me the power to execute hundereds of goroutines at once without worrying about mutual exclusion. Granted that this could be achieved at the database level itself, it wasn’t obvious at the time. The project timeline required that I followed the *Just make it work* ideology, but got to learn a lot about neo4j in the process.

**Conclusion**

Neo4j, being a relatively newer concept in a world of SQLites and Mongooses, has the potential to be one of the most expressive databases, especially in the budding world of data visualization. While it has its caveats, a lot of them can be handled at the application level itself. While the documentation for some of the driver implementations leave a lot to be desired, in the end, there is nothing that a targetted google search can’t solve.

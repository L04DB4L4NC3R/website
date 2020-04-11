---
title: 'Clean Architecture, the right way'
date: '2020-01-12T07:31:35.937Z'
thumb_img_path: images/Clean-Architecture--the-right-way/0*ou5WuCuRbI-bcYA0.jpg
excerpt: 'A practical guide to Clean Architecture, with a personal touch.'
layout: post
---
A practical guide to *Clean Architecture*, with a personal touch.

![](/images/Clean-Architecture--the-right-way/0*ou5WuCuRbI-bcYA0.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@max_duz?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@max_duz?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Max Duzij</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

Just last Sunday, I was randomly browsing GitHub, (like most of my Sundays usually go) and I stumbled upon a very popular repository, with over 10K commits. Now I am not going to name which project it was but it should suffice to say that even though I knew the stack of the project, the code itself was completely alien to me. Some features were randomly thrown adrift a sea of loosely cohesive functions inside directories called “*utils”* or worse, “*helpers”.*

The catch with big projects is that overtime, they become so complex that it is actually cheaper to re-write them rather than training new talent to actually understand the code and then contribute.

This brings me to the ulterior motive of the rather practical anecdote, which is to talk about Clean Architecture, at an implementation level. Now this blog is going to contain some Go code, but fret not, even if you are not familiar with the beautiful language, the concepts are fairly easy to grok.

* * *

### What is so *Clean* about Clean Architecture?

![](/images/Clean-Architecture--the-right-way/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

In short, you get the following benefits from using Clean Architecture:

*   **Database Agnostic**: Your core business logic does not care if you are using Postgres, MongoDB, or Neo4J for that matter.
*   **Client Interface Agnostic:** The core business logic does not care if you are using a CLI, a REST API, or even gRPC.
*   **Framework Agnostic:** Using vanilla nodeJS, express, fastify? Your core business logic does not care about that either.

Now if you want to read more about how clean architecture works, you can read the fantastic blog, [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), by *Uncle Bob*. For now, lets jump to the implementation. To follow along, view the repository [here](https://github.com/L04DB4L4NC3R/clean-architecture-sample.git).

    Clean-Architecture-Sample  
    ├── api  
    │   ├── handler  
    │   │   ├── admin.go  
    │   │   └── user.go  
    │   ├── main.go  
    │   ├── middleware  
    │   │   ├── auth.go  
    │   │   └── cors.go  
    │   └── views  
    │       └── errors.go  
    ├── bin  
    │   └── main  
    ├── config.json  
    ├── docker-compose.yml  
    ├── go.mod  
    ├── go.sum  
    ├── Makefile  
    ├── pkg  
    │   ├── admin  
    │   │   ├── entity.go  
    │   │   ├── postgres.go  
    │   │   ├── repository.go  
    │   │   └── service.go  
    │   ├── errors.go  
    │   └── user  
    │       ├── entity.go  
    │       ├── postgres.go  
    │       ├── repository.go  
    │       └── service.go  
    ├── README.md

**Entities**

Entities are the core business objects that can be realized by functions. In MVC terms, they are the model layer of the clean architecture. All entities and services are enclosed in a directory called `pkg`. This is actually what we want to abstract away from the rest of the application.

If you take a look at *entity.go* for user, it looks like this:

<figcaption><em>pkg/user/entity.go</em></figcaption>

Entities are used in the **Repository** *i*nterface, which can be implemented for any database. In this case we have implemented it for Postgre, in *postgres.go.*  Since repositories can be realized for any database, therefore they are independent of all of their implementation details.

<figcaption><em>pkg/user/repository.go</em></figcaption>

**Services**

Services include interfaces for higher level business logic oriented functions. For example, *FindByID,* might be a repository function, but *login* or *signup* are service functions. Services are a layer of abstraction over repositories by the fact that they do not interact with the database, rather they interact with the repository interface.

<figcaption><em>pkg/user/service.go</em></figcaption>

Services are implemented at the user interface level.

**Interface Adapters**

Each user interface has it’s separate directory. In our case, since we have an API as an interface, we have a directory called *api*.

Now since each user-interface listens to requests differently, interface adapters have their own *main.go* files, which are tasked with the following:

*   Creating Repositories
*   Wrapping Repositories inside Services
*   Wrap Services inside Handlers

Here, Handlers are simply user-interface level implementation of the Request-Response model. Each service has its own Handler. See *user.go*

* * *

### **Error Handling**

![](/images/Clean-Architecture--the-right-way/1*Ps25a0vjZLWu_Tam4pklew.png)

<figcaption>Error flow in Clean Architecture</figcaption>

The basic principle behind error handling in Clean Architecture is the following:

> Repository errors should be uniform and should be wrapped and implemented differently for each interface adapter.

What this essentially means is that all of the database level errors should be handled by the user interfaces differently. For example, if the user interface in question is a REST API then errors should be manifested in the form of HTTP status codes, in this case, code 500. Whereas if it is a CLI then it should exit with status code 1.

In Clean Architecture, Repository errors can be at the root of *pkg* so that Repository functions is able to call them in case of a control flow miscarriage, as seen below:

<figcaption><em>pkg/errors.go</em></figcaption>

The same errors can then be implemented according to the specific user interface, and can most often be wrapped in views, at the Handler level, as seen below:

Each Repository level error, or otherwise, is wrapped inside a map, which returns an HTTP status code corresponding to the appropriate error.

* * *

### **Conclusion**

Clean Architecture is a great way to structure your code and then forget about all of the complexities that might arise due to agile iterations or rapid prototyping. Being database, user interface, as well as framework independent, Clean Architecture clearly takes the cake for living up to its name.

### References

[**L04DB4L4NC3R/clean-architecture-sample**  
*You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…*github.com](https://github.com/L04DB4L4NC3R/clean-architecture-sample "https://github.com/L04DB4L4NC3R/clean-architecture-sample")[](https://github.com/L04DB4L4NC3R/clean-architecture-sample)

[**Clean Coder Blog**  
*Over the last several years we've seen a whole range of ideas regarding the architecture of systems. These include…*blog.cleancoder.com](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html "https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html")[](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

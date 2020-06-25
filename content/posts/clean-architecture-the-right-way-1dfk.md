---
title: 'Clean Architecture, the right way'
date: '2020-01-12T07:31:35.000Z'
excerpt: >-
  A practical guide to Clean Architecture, with a personal touch.  Just last
  Sunday, I was randomly bro...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--K8y-87Er--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--Asc-PTnU--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/2ffsp4xeks4jxhbb0elk.png
comments_count: 1
positive_reactions_count: 19
tags:
  - go
  - productivity
canonical_url: 'https://dev.to/l04db4l4nc3r/clean-architecture-the-right-way-1dfk'
layout: post
---
A practical guide to _Clean Architecture_, with a personal touch.

Just last Sunday, I was randomly browsing GitHub, (like most of my Sundays usually go) and I stumbled upon a very popular repository, with over 10K commits. Now I am not going to name which project it was but it should suffice to say that even though I knew the stack of the project, the code itself was completely alien to me. Some features were randomly thrown adrift a sea of loosely cohesive functions inside directories called “_utils”_ or worse, “_helpers”._

The catch with big projects is that overtime, they become so complex that it is actually cheaper to re-write them rather than training new talent to actually understand the code and then contribute.

This brings me to the ulterior motive of the rather practical anecdote, which is to talk about Clean Architecture, at an implementation level. Now this blog is going to contain some Go code, but fret not, even if you are not familiar with the beautiful language, the concepts are fairly easy to grok.

### What is so _Clean_ about Clean Architecture?

![](https://cdn-images-1.medium.com/max/772/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

In short, you get the following benefits from using Clean Architecture:

- **Database Agnostic** : Your core business logic does not care if you are using Postgres, MongoDB, or Neo4J for that matter.
- **Client Interface Agnostic:** The core business logic does not care if you are using a CLI, a REST API, or even gRPC.
- **Framework Agnostic:** Using vanilla nodeJS, express, fastify? Your core business logic does not care about that either.

Now if you want to read more about how clean architecture works, you can read the fantastic blog, [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), by _Uncle Bob_. For now, lets jump to the implementation. To follow along, view the repository [here](https://github.com/L04DB4L4NC3R/clean-architecture-sample.git).


```
Clean-Architecture-Sample
├── api
│ ├── handler
│ │ ├── admin.go
│ │ └── user.go
│ ├── main.go
│ ├── middleware
│ │ ├── auth.go
│ │ └── cors.go
│ └── views
│ └── errors.go
├── bin
│ └── main
├── config.json
├── docker-compose.yml
├── go.mod
├── go.sum
├── Makefile
├── pkg
│ ├── admin
│ │ ├── entity.go
│ │ ├── postgres.go
│ │ ├── repository.go
│ │ └── service.go
│ ├── errors.go
│ └── user
│ ├── entity.go
│ ├── postgres.go
│ ├── repository.go
│ └── service.go
├── README.md
```


**Entities**

Entities are the core business objects that can be realized by functions. In MVC terms, they are the model layer of the clean architecture. All entities and services are enclosed in a directory called pkg. This is actually what we want to abstract away from the rest of the application.

If you take a look at _entity.go_ for user, it looks like this:


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2F04efd6e4659f7aab367523e52b0aa839" style="border: 0; width: 100%;"></iframe>


Entities are used in the **Repository** _i_nterface, which can be implemented for any database. In this case we have implemented it for Postgre, in _postgres.go._ Since repositories can be realized for any database, therefore they are independent of all of their implementation details.


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2F0f6862642ff871b1a754af9829c2ac18" style="border: 0; width: 100%;"></iframe>


**Services**

Services include interfaces for higher level business logic oriented functions. For example, _FindByID,_ might be a repository function, but _login_ or _signup_ are service functions. Services are a layer of abstraction over repositories by the fact that they do not interact with the database, rather they interact with the repository interface.


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2F9a457875a046e438fd0a76115db272f7" style="border: 0; width: 100%;"></iframe>


Services are implemented at the user interface level.

**Interface Adapters**

Each user interface has it’s separate directory. In our case, since we have an API as an interface, we have a directory called _api_.

Now since each user-interface listens to requests differently, interface adapters have their own _main.go_ files, which are tasked with the following:

- Creating Repositories
- Wrapping Repositories inside Services
- Wrap Services inside Handlers

Here, Handlers are simply user-interface level implementation of the Request-Response model. Each service has its own Handler. See _user.go_


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2F1b85ee1ac967163139465dda80a0f3b5" style="border: 0; width: 100%;"></iframe>


### **Error Handling**

![](https://cdn-images-1.medium.com/max/481/1*Ps25a0vjZLWu_Tam4pklew.png)<figcaption>Error flow in Clean Architecture</figcaption>

The basic principle behind error handling in Clean Architecture is the following:

> Repository errors should be uniform and should be wrapped and implemented differently for each interface adapter.

What this essentially means is that all of the database level errors should be handled by the user interfaces differently. For example, if the user interface in question is a REST API then errors should be manifested in the form of HTTP status codes, in this case, code 500. Whereas if it is a CLI then it should exit with status code 1.

In Clean Architecture, Repository errors can be at the root of _pkg_ so that Repository functions is able to call them in case of a control flow miscarriage, as seen below:


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2F42c6d8fdc9885666707e1cc680b213f0" style="border: 0; width: 100%;"></iframe>


The same errors can then be implemented according to the specific user interface, and can most often be wrapped in views, at the Handler level, as seen below:


<iframe class="liquidTag" src="https://dev.to/embed/gist?args=https%3A%2F%2Fgist.github.com%2FL04DB4L4NC3R%2Fc407b1530a0ca915372cd0ba4652dec8" style="border: 0; width: 100%;"></iframe>


Each Repository level error, or otherwise, is wrapped inside a map, which returns an HTTP status code corresponding to the appropriate error.

### **Conclusion**

Clean Architecture is a great way to structure your code and then forget about all of the complexities that might arise due to agile iterations or rapid prototyping. Being database, user interface, as well as framework independent, Clean Architecture clearly takes the cake for living up to its name.

### References

- [L04DB4L4NC3R/clean-architecture-sample](https://github.com/L04DB4L4NC3R/clean-architecture-sample)
- [Clean Coder Blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

This Article was originally published [on Medium](https://medium.com/gdg-vit/clean-architecture-the-right-way-d83b81ecac6) under [Developer Student Clubs VIT, Powered By Google Developers](https://dscvit.com/). [Follow us](https://medium.com/gdg-vit) on Medium.

* * *

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/clean-architecture-the-right-way-1dfk)*


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

---
title: Mutually exclusive terminal sessions on the web
date: '2019-04-30T11:15:58.382Z'
thumb_img_path: images/Mutually-exclusive-terminal-sessions-on-the-web/0*RD_245UoYjcLm1P3.png
excerpt: Introduction
layout: post
---
**Introduction**

In the age of online learning, knowledge can be grasped at a click of a button while enjoying your favourite blend of coffee sitting on your favourite couch. In this era of online distribution of education, mutually exclusive exam rooms are a necessity. We will learn how to make an online shared command line exam room for the same.

Note that the [project](https://github.com/L04DB4L4NC3R/examinaar) which is going to be referred has the following deliverables:

*   Terminal sessions on the web
*   The ability to create/delete shell instances of any OS at will
*   Filesystem sharing, yet session based exclusivity
*   The ability to join/leave multiple sessions at will
*   Real time video chatting while in session

Without further ado lets get started on a journey which will take you to the horizons of your browser as well as the zenith of your terminal.

*   golang standard net/http library
*   docker community edition
*   gotty, go web terminal library

The basic draft of our application will have 2 way shared terminals like this-

![](/images/Mutually-exclusive-terminal-sessions-on-the-web/0*RD_245UoYjcLm1P3.png)

*   Make sure to install the latest version of golang
*   Install the latest version of docker CE
*   Install [goTTY](https://www.tecmint.com/gotty-share-linux-terminal-in-web-browser/)

**Installing go dependencies**

    `$ sudo apt-get update && sudo apt-get upgrade -y  
    $ go get github.com/yudai/gotty  
    $ tree .`
    `├── bin    
    │   ├── get_dependancies    
    │   └── main    
    ├── _config.yml    
    ├── controller    
    │   ├── auth.go    
    │   ├── helpers.go    
    │   ├── host.go    
    │   ├── routers.go    
    │   └── user.go    
    ├── database.db    
    ├── main.go    
    ├── model    
    │   └── dbfuncs.go    
    ├── README.md    
    └── views    
        ├── _card.html    
        ├── host.html    
        ├── index.html    
        ├── login.html    
        ├── _navbar.html    
        ├── _scripts.html    
        ├── session.html    
        ├── signup.html    
        └── view\_sessions.html`

**Writing the main.go server file**

Quick recap. We installed all of the required software. Then we moved on to set up our server and handlers for serving static files. Then we wrote a function for populating templates to make sure our frontend work is fine and dandy.

Phew! that was a lot! But we have a lot of configuration and setting up done. Now we just have to convert coffee to code and we are good to go. Moving forward, now we are ready to set up the endpoints of our application. We will first start at exposing the API and then we will work on creating a frontend for the same.

Navigate to **/controller** and create 2 files called **host.go** and **routers.go**. The former will have all of our major code and the latter will have some configuration to make sure it runs fine, thusly obeying the unspoken law of modularity.

**Writing modular structures for linkage**

For making things easy for us to understand and implement we will be creating a structure called **Host**, which holds a template object which we can play with. Then we a **RegisterRoutes** method to Host for handling our desired end points

**router.go** is solely dedicated to joining all of the modular code that we write in package controller and include them in a function which runs when the server runs.

Will will also include the Startup function in **main.go** to start handling the routes we specify

**Making a frontend**

Every project starts with an index.html. Now it is finally time to create our own. Navigate to **/views** directory and create **index.html** and **\_scripts.html** The main aim is creating a form which can give us the following information-

*   image1: Name of the first image/OS the host wants to run
*   image2: Name of the second image/OS the host wants to run
*   port1: Port number of the first image
*   port2: port number of the second image

Our Index file now looks like this

![](/images/Mutually-exclusive-terminal-sessions-on-the-web/0*TooEIMmtwBJS5MsH.png)

**Creating a session**

Now that we have made the form, it is time to make a handler which does the following-

*   Take inputs- image1, image2, port1, port2
*   start docker container image1 on port1 and image2 on port2
*   exec into the docker container and expose it using goTTY

**Post handler for creating session**

We will also write our goroutines to make sessions. Each goroutine runs a container with the specified (posted) image and along the specified (posted) port in interactive mode. Then we pipe that exclusive terminal session onto the web through our trusted goTTY

And thus we end our post handler for creating an exclusive session. Now we create a get route to show us the form.

    `func (h Host) servepage(w http.ResponseWriter, r \*http.Request) {    
    if r.Method == http.MethodGet {`
     `// look for our index page and serve it    
            t := h.temp.Lookup("index.html")    
            if t != nil {    
                err = t.Execute(w, val)    
            } else {    
                w.WriteHeader(http.StatusNotFound)    
            }    
        } else if r.Method == http.MethodPost { // Continue with the post handler`
    `}`

Quick recap of what we just did. We created a form in index.html, then we started writing the servepage route that we had defined before. First we handled the POST request, and serialized all of the posted input to a data structure. Then we used that information to write asynchronous goroutines and make then run a docker container of our choice and port in interactive mode. And lastly run a goTTY session on that running docker container. The last thing left on our menu is actually showing the terminals online. So we need to create our **host.html**. See the source code.

**How to run the project**

    `# Pull all of the essential docker images you want to run     
    docker pull alpine ubuntu fedora`
    `# Run the project     
    go run main.go`

*   Navigate to localhost:3000/host
*   Enter the details and you are good to go

**Conclusion**

We have reached a stage where we can make and deploy shared terminals on the clouds. The advantage of these sessions are-

*   They are light weight
*   They follow mutual exclusion
*   There are no memory leaks into the host system
*   They is fast and effective
*   They provides shared address space and at the same time abstraction from the host

**Moving forward**

This project was just the beginning. We can do so much more! Creating a seperate user space for viewing and joining sessions. Even including Agora.io video streaming SDK for online monitoring and video calling. The possibilities are endless. A sample project is given below

[Sample project demonstration](https://youtu.be/YAKG4s9OGUA)

[Project source code](https://github.com/angadsharma1016/examinaar.git)

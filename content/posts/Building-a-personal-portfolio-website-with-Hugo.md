---
title: Building a personal portfolio website with Hugo
date: '2019-07-26T16:25:51.363Z'
thumb_img_path: images/Building-a-personal-portfolio-website-with-Hugo/0*yZCwvYCNdJQKmRUd.jpg
excerpt: Introduction
layout: post
---
![](/images/Building-a-personal-portfolio-website-with-Hugo/0*yZCwvYCNdJQKmRUd.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@laurenmancke?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@laurenmancke?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Lauren Mancke</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

**Introduction**

A personal portfolio is always fun. Whether it be flaunting it amongst your peers or standing out from the crowd in hiring. Everyone wants to have one but no one wants to write boring HTML for it. Well guess what, now you can make your own portfolio the way you write your `README`s on GitHub, in [markdown](https://www.markdownguide.org/).

[Hugo](https://github.com/gohugoio/hugo.git), the world’s fastest framework for building websites, offers the following features for building your own website with both blazing fast speed and smooth ease. Hugo provides the following features:

*   Fast reloading with real time changes on the web
*   Loads of themes and templates
*   Multi-language support
*   Static site generator
*   Millisecond build time

**Installation**

To get started, make sure you have the [Go](https://golang.org/dl/) installed. To install Hugo refer [this](https://gohugo.io/getting-started/installing).. Hugo offers a very easy-to-use multi Operating System command line interface to interact with its underlying features.

**Getting started**

To create a new website using Hugo, simply run the following commands on the command line.

    $ hugo new site mysite  
    $ cd mysite  
    $ git clone https://github.com/vaga/hugo-theme-m10c.git themes/m10c
    # Directory structure of the project
    mysite  
    ├── archetypes  
    │   └── default.md  
    ├── config.toml  
    ├── content  
    ├── data  
    ├── layouts  
    ├── static  
    └── themes  
        └── m10c
    7 directories, 2 files

You can look at some great themes for Hugo over [here](https://themes.gohugo.io/). In this tutorial we are going to use the [m10c](https://github.com/vaga/hugo-theme-m10c) theme.

Add `theme = "m10c"`, at the end of **config.toml**. You can start the hugo server by typing:

    $ hugo server -D

Go to `localhost:1313` and you will be able to see the following:

![](/images/Building-a-personal-portfolio-website-with-Hugo/1*Socm62bErSlwH6Z7HMT_wA.png)

<figcaption><em>Empty m10c&nbsp;theme</em></figcaption>

Now to add social links to your portfolio you can take a look at **mysite/themes/m10c/exampleSite/config.toml.** This serves as an example of adding different components to your own *config.toml.* You can add the social login links to your own config. Copying the params to our own *config.toml*, it now looks like this:

    baseURL = "[http://example.org/](http://example.org/)"  
    languageCode = "en-us"  
    title = "About me"  
    theme = "m10c"
    [params]  
      author = "Angad Sharma"  
      description = "Noob is just a state of mind"  
      [[params.social]]  
        name = "github"  
        url = "[https://github.com/L04DB4L4NCER](https://github.com/L04DB4L4NCER)"  
      [[params.social]]  
        name = "twitter"  
        url = ""  
     [[params.social]]  
      name = "linkedIn"  
      url = "[https://linkedin.com/in/angad-sharma-07bb38122/](https://linkedin.com/in/angad-sharma-07bb38122/)"

To add an avatar, simple add an image of yourself, name it `avatar.jpg` and place it in **static/** folder. Our website now looks like this:

![](/images/Building-a-personal-portfolio-website-with-Hugo/1*8IYZA9r1HUy0xn66wRzyYA.png)

<figcaption><em>The website, with social links and&nbsp;avatar</em></figcaption>

Now that we have our image and social links on the website, it is time to add some more of our information.

In Hugo, we can create different web pages. Each webpage goes into the **content/posts/** directory as a markdown file. It is there that we can write markdown and define how we want it all to lay out.

Webpages are created in the form of posts in Hugo. Lets get started with creating a new post.

    $ hugo new posts/Blogs.md

This creates a new file called `Blogs.md` in the **content/posts/** folder. Open *Blogs.md* and you can start writing markdown.

    ---  
    title: "Blogs"  
    date: 2019-07-23T20:14:38+05:30  
    draft: true  
    ---
    ### This is a new blog page  
    I can write in markdown over here
    <br>
    #### Index
    [Links to blogs](#a)  
    [Links to blogs](#b)  
    [Links to blogs](#c)  
    [Links to blogs](#d)  
    [Links to blogs](#e)  
    [Links to blogs](#f)
    <br>
    - [X] Markdown  
    - [X] Is  
    - [X] Fun

And it will automatically be reloaded on your website in the form of a hyperlink. You can paginate over these hyperlinks and also set which hyperlinks to show first in the order of the time they were created. On clicking the hyperlink, you will be able to see contents of the markdown file that we defined above.

![](/images/Building-a-personal-portfolio-website-with-Hugo/1*ypiaH3qzp5N0ONRBwE0CMQ.png)

<figcaption><em>First post</em></figcaption>

![](/images/Building-a-personal-portfolio-website-with-Hugo/1*CGLe-C8Sb8lIgkDznCy7tg.png)

<figcaption><em>Blogs.md</em></figcaption>

With the right number of posts and enough content, you can make your own portfolio. Take a look at one of my post pages.

![](/images/Building-a-personal-portfolio-website-with-Hugo/1*mD4spE_b_D_ldNDqG081Vw.png)

An industry with an increasing number of competition is the best motivation for someone to start designing their portfolio in a way that it stands out from the rest of the competition. But who says it has to be hard?

With a handful of simple steps, and some markdown magic, anyone can make their own beautiful website without coding one bit. Hugo is indeed a very fast tool, with advanced features like instant reloading and real time refresh, loads of templates, easy configuration, multi-language support and of course, markdown!

**References**

[**L04DB4L4NC3R/hugo-demo**  
*Contribute to L04DB4L4NC3R/hugo-demo development by creating an account on GitHub.*github.com](https://github.com/L04DB4L4NC3R/hugo-demo "https://github.com/L04DB4L4NC3R/hugo-demo")[](https://github.com/L04DB4L4NC3R/hugo-demo)

[**Hosting & Deployment**  
*Site builds, automated deployments, and popular hosting solutions.*gohugo.io](https://gohugo.io/hosting-and-deployment/ "https://gohugo.io/hosting-and-deployment/")[](https://gohugo.io/hosting-and-deployment/)

[**gohugoio/hugo**  
*The world's fastest framework for building websites. - gohugoio/hugo*github.com](https://github.com/gohugoio/hugo "https://github.com/gohugoio/hugo")[](https://github.com/gohugoio/hugo)

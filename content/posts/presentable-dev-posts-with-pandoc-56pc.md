---
title: Presentable DEV posts with Pandoc
date: '2020-04-21T06:10:36.270Z'
excerpt: >-
  I was preparing my resume due to the upcoming placement season (boy did that
  get ruined by the pandem...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--EfCczvE1--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/drs28swxy41cwx34nn8g.png
comments_count: 0
positive_reactions_count: 4
tags:
  - tutorial
  - showdev
  - todayilearned
  - todayisearched
canonical_url: 'https://dev.to/l04db4l4nc3r/presentable-dev-posts-with-pandoc-56pc'
layout: post
---
I was preparing my resume due to the upcoming placement season (boy did that get ruined by the pandemic). Like a noobie that I was, I was using a paid service to generate cool templates for me to work with. A friend of mine introduced me to [LaTeX](https://www.latex-project.org/) and i got very interested. It turns out that using latex, you can quickly create beautiful documents with a straight forward syntax. 

During my hours of roaming the often-uncharted recesses of the internet, I came to know about **pandoc**, which is a tool that can be used to convert documents from one markup format to the other. Quite interestingly, it can be used to convert markdown to LaTeX. Moreover, [beamer](https://www.overleaf.com/learn/latex/beamer) is used to create beautiful and simplistic LaTeX flavored presentations.


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2Fjgm%2Fpandoc" style="border: 0; width: 100%;"></iframe>


All the posts on the DEV community are written in markdown (even the comments), and it even has an API to fetch all of your posts. One thing led to the other and I ended up making a script for converting all of my published DEV posts to a presentation. Let us see how.

---

### Installing Dependencies

If you are on a debian based system, run the following commands:


```sh
# markup conversion tool
sudo apt install pandoc

# installing latex tools
sudo apt install texlive-latex-extra

# installing xelatex engine for handling unicode
sudo apt install texlive-xetex

# installing JSON parser for bash
sudo apt install jq

# installing curl for sending requests
sudo apt install curl
```


The following is a copy-friendly debian-based dependency installation command:


```sh
sudo apt install pandoc texlive-latex-extra texlive-xetex jq curl
```


---

### Generating the DEV API Key

DEV offers a [well-documented application programming interface](https://docs.dev.to/api/) for common actions such as fetching posts and comments. You can create an API key by going into your account settings:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/c5npwwq439ju55wyziqy.png)

This key will be used for fetching user-specific posts. 

---

### Using Pandoc

Pandoc is a really powerful markup conversion tool. I suggest you read its man page to know the full extent of its power. For the purpose of this blog, we will learn how to convert markdown to PDF presentation format (beamer LaTeX). 

Let us create a markdown file called 
`test.md`
: 


```md
---
title:
  - My Presentation
author:
  - Angad Sharma
theme:
  - AnnArbor
---

# This is a new slide

## This is a heading

* This is some text
* **This is some bold text**
* *This is some emphatic text*

# This is another slide

| This | Is | A | Table |
|:----:|:--:|:-:|:-----:|
| A | B | C | D | 
| E | F | G | H |

# This is yet another slide

![This is a photo](https://dev-to-uploads.s3.amazonaws.com/i/q8twfrlpiboszsy4d5d6.jpg)
```


The data enclosed in the 3 dashes is the metadata of the document. It can be used to define details like the author and heading of the presentation, as well as the theme for the same. Take a look at the [list of beamer themes to look for the one you like](http://deic.uab.es/~iblanes/beamer_gallery/index_by_theme.html). Now let us convert the markdown to a presentation: 


```sh
pandoc test.md -t beamer -o out.pdf --latex-engine=xelatex
```


The 
`-t`
 flag helps decide the format of the output. In this case we want a LaTeX-style presentation (beamer). The next flag, 
`-o`
 specifies the output file. 
`--latex-engine`
 flag decides which engine to use while parsing the document. In this case we are using xelatex because it handles unicode really well. Note that version 2.9.* uses 
`--pdf-engine`
 instead of 
`--latex-engine`
.

Now our out.pdf will look like this:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/fbsztnfjqmv0vn1o2vpe.png)

---

### Converting DEV posts into presentations

The following lines of code fetch your articles from DEV and convert them into a beautiful LaTeX themed presentation:


```sh
curl -H "api-key: <YOUR_API_KEY>" https://dev.to/api/articles/me/published | jq -r ".[].body_markdown"

pandoc posts.md -t beamer -o presentation.pdf --latex-engine=xelatex
```


Now what did we do? We used the DEV API to fetch a JSON of all your published posts, which is an array. Each post in that array contains a property called 
`body_markdown`
, which contains the markdown of that particular post. We simply used the 
`jq`
 parser to go through each element in the array and fetch the body_markdown of the same. Then we piped the output to a file for the subsequent step.

We used pandoc on the generated file, directing it to use the beamer format to output a PDF using the xelatex engine. Now the latter is necessary for rendering unicode characters in your markdown (so that all of your emojis show up). 
 
Quick tip: To get your latest post, simply use the 
`per_page`
 attribute of the DEV API:


```sh
# Note that an index can also be passed on the [] parameter
# of "jq" to get a specific post
curl -H "api-key: <YOUR_API_KEY>" https://dev.to/api/articles/me/published?per_page=1 | jq -r ".[].body_markdown" > latest.md

# verbose flag can be used to view additional info such as image fetch log
pandoc latest.md -t beamer -o latest.pdf --latex-engine=xelatex --verbose
```


As a sample, I have taken my blog on [bspwm](https://dev.to/l04db4l4nc3r/bspwm-a-bare-bones-window-manager-44di) and converted to a presentation: 

[Click here to view the presentation](https://drive.google.com/file/d/108wsEElpa9yqQCPNrWyomWGM7pMLO38b/view?usp=sharing)

---

### Limitations

* Liquid links do not get converted in the presentation, including embedded gists, repositories and other posts. This is due to the fact that these are not markdown features, but DEV features instead. 

* Pandoc collects all the photos in the markdown during runtime. In the case of a slow internet connection, it may timeout and completely ignore some photos. But this is in the case of a VERY slow internet connection.


---

### Conclusion

Need to take a seminar or a webinar on a topic you have already written about? Generate a presentation from your markdown in minutes, with pandoc!


*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/presentable-dev-posts-with-pandoc-56pc)*


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

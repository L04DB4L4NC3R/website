---
title: CovidComm | A Twilio DEV Hack Project
date: '2020-04-29T17:55:36.479Z'
excerpt: >-
  Introduction   COVID-19 is a stressful time for people, who tend to panic. In
  such a case, I...
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--JNaGbj9U--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--hZPwwEkC--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://dev-to-uploads.s3.amazonaws.com/i/xw0rkizoz8cbb8gur92w.png
comments_count: 0
positive_reactions_count: 6
tags:
  - twiliohackathon
  - showdev
canonical_url: 'https://dev.to/l04db4l4nc3r/twilio-dev-hackathon-project-2c9o'
layout: post
---
[Comment]: # (All of this is placeholder text. Use this format or any other format of your choosing to best describe your project.)

[Reminder]: # (Make sure you've submitted the Twilio CodeExchange agreement: https://ahoy.twilio.com/code-exchange-community)

[Important]: # (By making a submission, you agree to the competition's terms: https://www.twilio.com/legal/twilio-dev-hackathon-terms)

## Introduction

COVID-19 is a stressful time for people, who tend to panic. In such a case, I decided to build an application which solves the following two issues:

The first issue in a time of international crisis due to the pandemic is that a lot of fake news is spreading over social media. People need a reliable, and moreover, regular source of news and information related to the COVID-19 pandemic. 

The second issue that plagues people is the uneven distribution of resources. I have this friend of mine, who need not be named. Her family panicked after the announcement of a nationwide lockdown. They immediately rushed into the nearest super-store and bought loads and loads of resources. This hoarding caused a lot of potential wastage in the household. Fortunately they were kind enough to distribute their resources to the neighbors, who were in dire need of the same. 

---

## What I built

**CovidComm** is a project that ensures that people stay up to date with the latest news about coronavirus. It has the following features:

* World COVID-19 status per country
  * Total and Daily Cases
  * Total Deaths and Daily Deaths
  * Total Infected and Daily Infected
  * Total Cured and Daily Cured
  * Filter by Everything
* Trending news related to coronavirus
  * Fetched from multiple media platforms
  * Bite sized news TLDR;
* Resource redistrubution system
  * Request for resources
  * Respond to other people's requests
  * Contact respondees
* CovidBot
  * An opt-in information service
  * Calls you up daily and reads you bite sized news
  * Save time and effort trying to procure news
* Multi Platform
  * Release for MAC OS
  * Release for Linux
  * Release for Windows

---

## Demo Link

This video contains the practical demo of the project as well as a voice recording of the CovidBot, which calls subscribers and informs them of the latest COVID-19 related news on a daily basis. Note that I am using a trail TWILIO account so the bot does say some garbage stuff in the beginning, but that can easily be done away with by shifting to a paid account.

**Stick around till the end** to see the CovidBot in action!


<iframe class="liquidTag" src="https://dev.to/embed/youtube?args=QAZf4J9LSnY" style="border: 0; width: 100%;"></iframe>

 
---

## Link to Code

This project is distributed between two repositories: One for the backend of the project and one for the desktop application: 


<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2FL04DB4L4NC3R%2Fcovidcomm" style="border: 0; width: 100%;"></iframe>



<iframe class="liquidTag" src="https://dev.to/embed/github?args=https%3A%2F%2Fgithub.com%2FL04DB4L4NC3R%2Fcovidcomm-ui" style="border: 0; width: 100%;"></iframe>


---

## How I built it (what's the stack? did I run into issues or discover something new along the way?)

When I started off with this project, I had one goal in mind. To learn from the crisis around me and build something useful for which there is a need. I also had an ulterior motive: my self learning (which I believe every developer should have). I was well versed in NodeJS but had never tried TypeScript out. I used this time to learn TS from scratch and build a backend using the same.

I had initially planned to make a website for the project, but I am not exactly fond of frontend web development so I decided to make a desktop application instead. Now I had worked with electronJS earlier so I knew that it has its own plethora of issues. I did a lot of research on which framework I can use (even considered making an X11 application using libxcb but decided to make it cross-platform). I landed on Xojo, which immediately caught my attention.

Now I had never heard of Xojo before, let alone use it. I quickly learnt how to program sweet XojoScripts for API fetch but ran into yet another problem: Xojo is proprietary. Which meant that I needed a paid license for building and exporting the project to various platforms. This dissuaded me since I had already spent hours on Xojo to build a desktop app. As a last resort I decided to search the ever growing list of GitHub student pack integrations. And low and behold, I found a free Xojo license in the student pack. I was overjoyed, set it up the very same day and built my first binary for linux!

One last issue I faced was time management. Since I try to be a perfectionist, at least when it comes to code quality, I decided to adopt the Clean Architecture for my TypeScript backend, which consumed a lot of time but made the code very readable. On the top of that I had to build and maintain the desktop application also, including the user interface, integrations and IPCs. It took a lot of time but I eventually got a build which is worth showing off :). Granted it is not the best UI out there (not even close), but I was more focused towards the functionality.

#### Stack

| Technology | Where it is being used in the project | 
|:----------:|:-------------------------------------:|
| TypeScript | Used with NodeJS for building the backend |
| Express | Backend framework for NodeJS |  
| MongoDB | Used as a database to store essential user and request details |
| Xojo | Used for building the Desktop Application for MacOS, Windows and Linux | 
| Twilio programmable voice API | For calling and reading out the news |
| Twilio verification service | For verifying phone numbers on the fly |


---

## Future Scope

The main future scope of this project is to include geolocation so that the people closest to you are the ones who can help you out. 

---

## Additional Resources/Info

* [coronavirus-tracker-cli](https://github.com/sagarkarira/coronavirus-tracker-cli)

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/twilio-dev-hackathon-project-2c9o)*


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

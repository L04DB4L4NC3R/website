---
title: 8 things I learnt from a script for repository creation
date: '2020-01-23T16:00:45.766Z'
excerpt: ''
thumb_img_path: >-
  https://res.cloudinary.com/practicaldev/image/fetch/s--TfZi7Xc1--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://res.cloudinary.com/practicaldev/image/fetch/s--MazfXGjF--/c_imagga_scale%2Cf_auto%2Cfl_progressive%2Ch_420%2Cq_auto%2Cw_1000/https://thepracticaldev.s3.amazonaws.com/i/sjpxueje7lwxngdcy1fm.png
comments_count: 4
positive_reactions_count: 69
tags:
  - git
  - linux
  - bash
  - docker
canonical_url: >-
  https://dev.to/l04db4l4nc3r/7-things-i-learnt-from-a-script-for-repository-creation-4cbk
layout: post
---
As a young boy I was always reluctant to do chores around the house. I just felt that doing the same thing again and again everyday was boring. As I grew up, this mentality changed for the better (thank god), and was hilariously replaced by the following quote in my professional life:

> If it takes longer than 30 seconds, automate it.

Recently, I was tasked with creating about 18 repositories for an organization that I maintain for [DSC-VIT](https://github.com/GDGVIT), powered by Google Developers. All of the repositories needed to be created for the projects that we have planned for the first two quarters of 2020. I decided to make a shell script for it and the following are some of the things I learnt in the process.


#### Index

* [Modular code in shell :ok_hand:](# importing-functions)
* [Echo is bad at JSON :poop:](# echo-is-bad-at-json)
* [Easy arrays in shell :star2:](# arrays-in-shell)
* [Did my curl succeed? :cyclone:](# checking-if-a-curl-request-succeeded)
* [GitHub API rate limitation :snail:](# github-api-rate-limitation)
* [Switch-Case structure in shell :first_quarter_moon:](# switch-case-in-shell)
* [Cross platform execution :whale:](# cross-platform-execution)
* [Unofficial bash strict mode :cop:](# unofficial-bash-strict-mode)

<br>

Look up the code over here:


<iframe class="liquidTag" src="https://dev.to/embed/github?args=L04DB4L4NC3R%2Fgitcr" style="border: 0; width: 100%;"></iframe>



<br>

### Importing functions

I wanted modularity in my code right off the bat. This meant breaking down my code into smaller files with smaller functions and then creating one entrypoint (CLI) for their execution. I had functions to 
`create`
 repositories in bulk, 
`delete`
 and 
`revert`
 creation in bulk as well. I also added a function to give out a neat little manual if someone hit 
`help`
.



```
├── functions
│   ├── config.sh
│   ├── create.sh
│   ├── manual.sh
│   └── revert.sh
├── gitcr
├── .env
├── README.md
└── repos.txt
```
 

I had to do 2 kinds of imports:

* Importing environment variables
* Importing functions

Both of them can be achieved via a simple syntax:


```bash
# in gitcr

. ./functions/config.sh
. ./functions/create.sh
. ./functions/manual.sh
. ./functions/revert.sh
```


All of the functions and exported variables in the included files can then be used directly in the main file. Note that I have used a 
`.`
 to import the aforementioned since it is recognized by 
`sh`
 shell. You can also use the 
`source`
 keyword to include them in *bash* but it is not recognized by *sh*.


<br>


### Echo is bad at JSON

I wanted to write the output from every iteration to the console, or a *JSON* file, as specified by the user. The first thought that hit my mind was to use the 
`echo`
 command and pipe it out to a file, or console. *echo* is quite bad at that since it is not build for formatting JSON. Instead, I used 
`jq`
 for the same. So it looked like this:


![jq demo](https://thepracticaldev.s3.amazonaws.com/i/enblxyi42su7k9hf3kjs.png)



`jq`
 took garbage formatting and parsed a completely formatted JSON out of it. This can then be piped to a file at will.

![echo + jq](https://thepracticaldev.s3.amazonaws.com/i/jauard7euyelu68loj0h.png)

<br>
<br>

### Arrays in shell

For storing the JSON output in each iteration, I used an array. Arrays in shell can be declared and used in the following way:


```bash
result = () # an empty array

result=("abcd") # an array with 0-th index = "abcd"

echo ${result[0]} # printing out the index

result[1] = "defg" # assigning value to an index

echo ${result[@]} # the '@' can be used for returning the whole array

result[$iterator] = 2 # variables can be used as indices.
```


Note that memory for arrays can not be pre-allocated in shell.


<br>
<br>

### Checking if a curl request succeeded


`curl`
 command has a 
`-i`
 flag which prints out the request details such as the status code returned as well as the message. This can be extracted from the request and be used to check if the request actually succeeded or not. 

The following code returns the first line of information about the curl request. 



```bash
$ res=`
curl -i -s -XDELETE https://api.github.com/repos/$owner_name/$line -H "Authorization: token $token" | head -1 
`

$ echo $res
HTTP/1.1 401 Unauthorized
```


The 
`res`
 variable can be broken down to get both the HTTP status code of the response, as well as its message, in the following way:



```bash
# To get the status code
$ code=`
echo $res | cut -d" " -f2
`

$ echo $code
401

# To get the status code response
$ status_of_res=`
echo $res | cut -d" " -f3-5
`

$ echo $status_of_res
Unauthorized
```


![curl success](https://thepracticaldev.s3.amazonaws.com/i/3tkfr3io5uha0b7gi4fn.png)

Now what happened here? 

Notice that the 
`head -1`
 command returns the first line of text from any input. We took that first line and we did a split with *space* as a delimiter, using the 
`cut -d" " -f2`
 command.


`-f2`
 flag means that we want the second token from the splitted string. Note that this numbering starts from 1 rather than 0. 
`f3-5`
 means that we want tokens from 3 to 5, since HTTP status code messages can be more than a word long and the sentence does not have any more words after that. 

Now we can use the status code we got to check if the request succeeded. GitHub API gives a *status 204* after a 
`DELETE`
 request succeeds, so a simple check would look something like this:


```bash
if [[ $code -eq 204 ]]
then
    echo "Request Succeeded"
else 
    echo "Request Failed"
fi
```



<br>
<br>

### GitHub API rate limitation

GitHub API v3 has a rate limitation of about 
`5000 requests`
 per authenticated user and 60 requests per hour for unauthenticated users. Whenever a request is sent to the API, it returns the total rate limitation and the amount remaining for the user, in the form of response headers:



```
X-RateLimit-Limit: 5000
X-RateLimit-Remaining: 4998
```


So if you are thinking about a bulk transaction application which uses the GitHub API, read more about rate limitation [here](https://developer.github.com/v3/# rate-limiting).

For me, adding the validation in the script was easy:

* Read the number of repositories the user wants to create
* If the number is greater than 5000, then fail

Which is easily programmable in the following way:


```bash
# Read number of words in repos.txt
repo_count=`
wc -w < repos.txt
`
if [ $repo_count -gt $GITHUB_MAX_REQUESTS ]
then
    echo "You are only allowed 5000 repos"
    exit 1
fi
```

A more pragmatic way would be to check the 
`X-RateLimit-Remaining`
 header by pinging the GitHub API and then deciding how many repositories can user create, which is also easily doable by text processing curl response headers.


```bash
remaining=`
curl -i -s -XDELETE https://api.github.com/repos/L04DB4L4NC3R/BOGUS_REPO -H "Authorization: token $token" | grep X-RateLimit-Remaining | head -1 | cut -d":" -f2
`
```


Here, 
`grep`
 searches for the *X-RateLimit-Remaining* header, 
`head -1`
 takes only the first sentence and 
`cut -d":" -f2`
 uses a colon delimiter to extract only the number out of the header key-value pair, which is then stored in a variable called 
`remaining`
.


<br>
<br>

### Switch Case in shell

Switch-case statements in shell have a very unique syntax:


```bash
cli(){
	case $1 in 
		create)
			create $@
			;;
		revert)
			revert $@
			;;

		*)
		helpFunc
 		;;
	esac
}
```


Notice the terminating word 
`esac`
 is actually the opposite of 
`case`
. This syntax was designed in a way to make programming of CLI applications easy. The 
`)`
 lexeme is used as a case statement and the 
`case`
 keyword is used as a *switch* statement if you compare it to other programming languages. Wildcard 
`*`
 has been used to match the 
`default`
 case in scenarios where the user enters something that is not handled by the CLI. 

The 
`create`
, 
`revert`
 and 
`helpFunc`
 are functions. In shell, functions are called without any parenthesis. Arguments can be passed to them by writing them in a space separated format after the function call. Interestingly, the 
`$@`
 is used to pass all of the arguments (that we got when we executed the CLI) to the functions that are being called.



```bash
./gitcr create --out=json
# $@ in the gitcr function = "./gitcr" "create" "--out=json"
# When passed to the create function, it retains all of the 
# original parameters
```



<br>
<br>


### Cross platform execution

One of the challenges I faced while making this script was to make it 
cross-platform. Docker came to the rescue! You can use a 
`bash`
 container, which occupies only *15 MB*.

![docker](https://thepracticaldev.s3.amazonaws.com/i/5res2x6lzc4evxpmp602.png)

The following steps can be used for a cross-platform CLI job:

* Use a [bash container](https://hub.docker.com/_/bash)
* Copy all files that are not user defined
* Build an image and push to [DockerHub](https://hub.docker.com/)
* During runtime, mount a volume which has user defined files
* Delete the container after it has completed execution


The Dockerfile looked like this:

```Dockerfile
FROM bash

RUN apk update && apk add curl && apk add jq

RUN mkdir -p /usr/app/cli

WORKDIR /usr/app/cli

COPY . . 

RUN chmod +x gitcr
```


During runtime, the following command can be executed:


```bash
docker run --rm --mount type=bind,source="{PATH}",target=/usr/app/cli/ angadsharma1016/gitcr -c "bash /usr/app/cli/gitcr create"
```


What happened here?

This command runs a container based off of a particular image, which has all of the code. During runtime, it takes in user defined files like 
`.env`
 and 
`repos.txt`
 as a volume mount inside the container and simply runs the CLI. Your system does not need to have bash and other tools installed. 


<br>
<br>

### Unofficial bash strict mode

Always start your bash scripts with the following lines:


```bash
set -euo pipefail
IFS=$'\n\t'
```


It means the following things:

* 
`set -e`
: Exit script if any of the commands throw a return code 1
* 
`set u`
: Any undeclared variable referenced will result in an error
* 
`set -o pipefail`
: Commands in pipes won't fail silently
* 
`IFS`
: *Internal Field Separator* controls what bash calls a word

If followed, the unofficial bash strict mode can save hours of debugging time. Read more it [here](http://redsymbol.net/articles/unofficial-bash-strict-mode/)

<br>
<br>

## Conclusion

One night of hacking away at my *zsh* and trying to act like I know what I am doing taught me a lot about how to actually write useful scripts that automate a lot of work that you either have to do stat, or will have to do in the near future. It's always better to take some time off the task at hand to actually figure out a better solution to do the said task sustainably in the future. 

Don't mind writing code or working on tools that other people have worked on before, as long as it is for your own personal learning (or rolling out a product better than market alternatives). Stay hungry and stay foolish!

*[This post is also available on DEV.](https://dev.to/l04db4l4nc3r/7-things-i-learnt-from-a-script-for-repository-creation-4cbk)*


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

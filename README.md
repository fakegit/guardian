# Guardian

> Guardian is a light weighted and clean enough tool for daily event organize. You can using guardian do all the work you want to do on computer in a day, and all just **automatically done!**

# Supported Events

Guardian using multiprocess to manage all the events, for now, he can do those things:

* scrap wallpapers from [pexels](www.pexel.com) in everyday 12:20 noon, this can be change to your hobbies of course.
* changing wallpapers automatically for you, but this is not something like changing wallpapers on Windows, guardian will automatically download new pictures from internet!! and all are high resolution images!!
* more..

![Picture](http://opbocoyb4.bkt.clouddn.com/VbLMFeNgPU0mWZi5.png)
![Picture](http://opbocoyb4.bkt.clouddn.com/lYZyWx7nS4hGmPOq.png)

# Usage

For using guardian is very simple, we can using supervisor or setsid to ensure it run automatically.
I prefer using setsid, add this into `~/.bashrc`:

```
alias guardian='setsid python3 /media/work/CodeSpace/PythonProjects/guardian/main.py'
```
the path is main.py path, using this, you can call it anytime in terminal guardian, and it will still keep runing even you close your terminal!!

# Future Work
Guardian is just a start, I will add more events into guardian and make it more modulable. 
Later on, guardian maybe intergrate with **Jarvis**, which is my personal artifical intellegent assistant.

# Contribute

if you want to contribute to make guardian become more powerful, fell free to send me PR.

# Copyright
this work was done by Jin Fagang. God-like Man in the world - just kidding. You can find me on wechat: `jintianiloveu`, more interesting things need you to explore...

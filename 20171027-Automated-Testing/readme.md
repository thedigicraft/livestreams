# Oct 27 2017 - Automated Website Testing with Selenium

<a href="https://www.youtube.com/watch?v=yZvELzHlukc">
  <img src="https://i.ytimg.com/vi/Es8JDy0dInw/maxresdefault_live.jpg">
  </a>

## The Tools You Need

### Python 2.7.x

You can download python here: https://www.python.org/downloads/

### Java

You can download Java here: https://java.com/en/download/

### Selenium

You need the Selenium jar file and you can download it here: http://www.seleniumhq.org/download/

### Selenium Python Package

Run this command in your terminal

```bash
pip install -U selenium
```

### Chrome WebDriver

You need to get a copy of the Chrome WebDriver from here:  https://sites.google.com/a/chromium.org/chromedriver/downloads


## Starting the Selenium Server

Open a windows command prompt in Administrator mode.   Navigate to the directory that you downloaded the Selenium jar file and run:

```bash
java -jar selenium-server-standalone-3.6.0.jar
```

Now your Selenium server should be running.   You can minimize the command prompt window but DO NOT close it.

## Running the test

In the video, we created a file called `test.py`.  Open your terminal (we used Git Bash in the video).  Navigate to the directory where you have `test.py` and run:

```bash
./test.py
```

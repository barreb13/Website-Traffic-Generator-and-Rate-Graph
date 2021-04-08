# Project Title
Assignment 4: Website Monitoring from CSS 390 Scripting Languages

Author: Brent Barrese

# Description
These are a combination of 3 Python scripts that will generate traffic to a web server, scrape the website for statistics in the html code, and use the data collected to generate a rate graph.

# How To Use
To use these scripts, place everything in the same directory. There should be an instance of a website server running locally or you can point externally.

These scripts use command line arguments or command line flags.

There will need to be 3 seperate instances of trafficgen running with 3 different urls to generate the required errors(200, 404, 500).

trafficgen.py - Python 3

**NOTE: There will need to be 3 terminals running this script with different url arguments to fulfill assignment**

This is the script that generates traffic to the site. It uses 3 command line arguments:
*   The requested url
*   An rps rate which is the requested rate per second - should be integer form
*   A jitter rate which is used to create a random variation - should be a floating point number

ex: $ python3 trafficgen<nolink>.py http<nolink>://localhost:8080/fail 300 0.65

collector.py - Python 3

This script 'scrapes' the website html code stats page and collects data at specific intervals. There are 2 command line arguments and 1 command line flag. 
*   command line argument of the url to scrape
*   command line argument of the name of desired output text file
*   --interval which needs to be typed '--interval' and followed by an integer 

This script will run continuously, and at the requested interval pull data and output to a tab-seperated file that the user specifies.

ex: $ python3 collector<nolink>.py http<nolink>://localhost:8080/stats output.txt --interval 10

plot.py - Python 3

This script will take a properly formatted text file and parse the data. It will convert all data to integers and plot a rate graph. It will generate a 1-minute rate graph of the errors scraped from the web server. It will format the graph accordingly. 

It takes 1 command line argument:

*   The text file that holds the properly formatted data that the user wishes to generate a rate graph from.

ex: $ python3 plot<nolink>.py collectOutput.txt

# Expectations
It is expected that all files will be in the same directory. The script is written in Python3 and not in executable format. It must be executed by typing python3 'scriptname' followed by any necessary arguments or flags. See 'How To Use' if questions in specific script.

# Reflection
This program used Python in a unique way to learn more about the language, learn a little HTML, and understand some of the modules and libraries that are available through Python.

One of the things I took away from this assignment is the large amount of modules or libraries available for this language. There seems to be something available for anything. There are multiple modules available for HTML. There are also modules for plotting scientific graphs and charts. I went through a lot of documentation to understand the abilities.

I got stuck in Part 2: Stats Collector with something that I should have known (text processing!). The ability to move text around to get it into the format I needed made sense once Professor Bernstein showed me how. I got stuck down the wrong path by looking at Beautifulsoup, which I believe is an available module / library for the Python language when dealing with HTML.

# References Used 
Professor Bernstein's Office Hours!

https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

https://stackoverflow.com/questions/49076404/from-string-to-float-with-argv-in-python 

https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request

https://pynative.com/python-random-randrange/ - random numbers in a range

https://www.tutorialspoint.com/python3/python_if_else.htm - if else syntax

https://stackoverflow.com/questions/474528/
what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds - how to run every n seconds

https://www.dataquest.io/blog/web-scraping-tutorial-python/ - web scraping and BeautifulSoup

https://stackoverflow.com/questions/29643544/python-a-bytes-like-object-is-required-not-str

https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

https://stackoverflow.com/questions/4048964/printing-tab-separated-values-of-a-list

https://stackoverflow.com/questions/11604653/add-command-line-arguments-with-flags-in-python3/11604777 - argParser for command line flag --interval

https://www.youtube.com/watch?v=UO98lJQ3QGI - matplotlib

https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/ - string to int list

https://matplotlib.org/3.3.3/tutorials/intermediate/legend_guide.html

https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-6.php - unix time conversion

https://stackoverflow.com/questions/28943887/how-to-append-elements-to-a-numpy-array

https://stackoverflow.com/questions/36592802/numpy-array-of-lists

https://stackoverflow.com/questions/6682784/reducing-number-of-plot-ticks - hiding tick labels

https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib

https://docs.python.org/3/library/argparse.html 
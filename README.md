# BMP_Network_Logs_Automation
Browser mob proxy Network_Logs Automation


##What is Browsermob Proxyy?
BrowserMob Proxy allows you to manipulate HTTP requests and responses, capture HTTP content, and export performance data as a HAR file. BMP works well as a standalone proxy server, but it is especially useful when embedded in Selenium tests.

##What is Selenium Webdriver?
Selenium WebDriver is a tool for automating web application testing, and in particular to verify that they work as expected

 What we are going to do?
By integrating BrowserMob with Webdriver we can record the network calls being made by a browser while webdriver tests are run in a HAR file for futher consumption.

###Benefits:
User can verify all the network request and post parameter to a server making sure that application is passing right values across.
User can verify the response from a server and confirm server is responding as expected.
User can validate all the request/response time lines in order to see the sequence of actions.
 

BMP allows you to validate all the parameters in an automated fashion which user generally performs using chrome’s debug tools in developer mode -> Network Tab as below:

 
##Prerequisites
Python 3.7 and above
Selenium Webdriver
Pip
Download the browsermob proxy from here extract the files

##How to install browsermob proxy?
Run the below command in your command prompt
pip install browsermob-proxy

##Execute the script
Once the execution completed the output har file automatically download and stored into your project folder

###Upload
Upload the har file from chrome’s developer mode -> Network Tab to debug

###View Network Logs
View the response results from Network tab



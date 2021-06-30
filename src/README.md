### URL lookup service

We have an HTTP proxy that is scanning traffic looking for malware URLs. Before
allowing HTTP connections to be made, this proxy asks a service that maintains several
databases of malware URLs if the resource being requested is known to contain
malware.
Write a small web service, in the language/framework your choice, that responds to
GET requests where the caller passes in a URL and the service responds with some
information about that URL. The GET requests look like this:

##### GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

The caller wants to know if it is safe to access that URL or not. As the implementer you
get to choose the response format and structure. These lookups are blocking users
from accessing the URL until the caller receives a response from your service.
The service must be containerized.
Give some thought to the following:

#####1) The size of the URL list could grow infinitely, how might you scale this beyond the memory capacity of this VM? 
Bonus if you implement this.

#####2) The number of requests may exceed the capacity of this VM, how might you solve that? 
Bonus if you implement this.

#####3) What are some strategies you might use to update the service with new URLs
Updates may be as much as 5 thousand URLs a day with updates arriving every
10 minutes

=================================================

##Solution 
###Tech, Tools
To build the URL Detector I did use below 

Flask framework for REST Microservice
MySQl, Python3.9
Apache, CGI

###Environment Setup
Development Environment used: macOS M1
Go to following GitHub Repository for the source code/configuration and download

https://github.com/Femalodedra/Url_Detector.git

###Database
https://dev.mysql.com/downloads/workbench/
macOS (x86, 64-bit), DMG Archive	8.0.25	112.7M	
Download
(mysql-workbench-community-8.0.25-macos-x86_64.dmg)
download, install and set up the connection

###Package install

Package                Version
--------------------- ---------
certifi               2021.5.30
chardet                4.0.0
click                  8.0.1
dnspython              2.0.0
Flask                  2.0.1
gunicorn               20.1.0
idna                   2.10
ipwhois                1.2.0
itsdangerous           2.0.1
Jinja2                 3.0.1
MarkupSafe             2.0.1
mysql                  0.0.3
mysql-connector-python 8.0.25
mysqlclient            2.0.3
pip                    21.1.3
protobuf               3.17.3
requests               2.25.1
setuptools             57.0.0
six                    1.16.0
urllib3                1.26.6
Werkzeug               2.0.1
wheel                  0.36.2


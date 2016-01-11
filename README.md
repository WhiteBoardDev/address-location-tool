
# Address Location Tool (ALT)

ALT is an alternative to dynamic DNS services like no-ip and dyndns. Its goal is to be able to track IPs of systems located on internet service providers which assign IPs dynamically. As the IP addresses rotate, be assured that you will be able to find your server!

## Installation

### 1. Database Setup

ALT uses [firebase](https://www.firebase.com) to store the list of nodes and IPs.
This means that the first step to get up and running is to head over there and create a free account.
Once you have a database created, remember the URL to it for the configuration step

### 2. Installing Bits


**Check prerequisites**

  * easy_install
  * curl
  * make
  * gcc
  * python-dev

**Then run this one liner install**

    curl https://raw.githubusercontent.com/WhiteBoardDev/address-location-tool/master/installation/install.sh | sudo bash

### 3. Configuration

When you install the software there are templates for the configuration files located at `/etc/alt/conf/`. These files
end with .tpl. Copy these files and rename the extension to `.conf` for ALT to pick them up.

#### a. Database Setup

Adding your first node to the database will require modifying two configuration files.
The first configuration file is for your database configuration (/etc/alt/conf/db.json) file.

Add your firebase url and secret:

     {
         "db": "firebase",
         "config": {
            "url": "firebase address location",
            "secret": "firebase secret"
         }
    }
#### b. Host Name Setup

Next edit the alt configuration (/etc/alt/conf/alt.json) file.
Adding port numbers for webservices is optional.

    {
        "node": {
            "name": "node name",
            "ports": [ 8080, 8090 ]  //<-- array of port numbers. Can be left blank
        }
    }

As far as node naming convention goes, try to make it lowercase and URL compliant, or else it can be
a pain to use in curl calls.

### 4. Run!


Command line arguments

    python app.py [module (alt, proxy)] [environment=optional (dev)]


The most common run arguments will be

    python app.py alt


When you are developing locally and want to run the code directly from the source without installing
execute with the environment variable `dev`.

    python app.py alt dev


## Next steps

### Using the Node list in Firebase

Now that we have a a bunch of node IPs tracked in firebase its time to do something with them.
To see if the updater worked we can curl the database.

        curl https://my-firebase-url.firebaseio.com/hosts.json

        {
             "node1":{
                  "name":"node name"
                  "external_address":"<ip>",
                  "local_address":"<ip>",
                  "ports": [ 8080, 8090 ]
             }
        }

Cool right?

Don't worry, there is more on the way. Like having your hosts file auto sync with all of your tracked nodes!


### Other uses for ALT

After the nodes are populated in the database, we could use this to create host files, nginx proxies, etc.

### Creating an nginx proxy

An nginx proxy file can be created for all nodes that has the same external ip address of the nginx server. It also must nodes with ports that match the internal port numbers. The internal port number will be proxied to the external port number. Edit the proxy configuration (conf/proxy.json). Start by editing the proxy.tpl file:

	{
	   "domain": "some.domain.com"
	   "proxy": [
	      	{
	        	"internal": [ 8080, 8090 ],
	        	"external": 8080
    	  	},
    	  	{
    	    	"internal": [ 9000 ],
    	    	"external": 9000
			}
		]
	}


## Developing

Run the `build-depoy.sh` script to create a build and deploy the checked out version of ALT into your system.

## License

MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Address Location Tool (ALT)

ALT is an alternative to dynamic DNS services like no-ip and dyndns. Its goal is to be able to track IPs of systems located on internet service providers which assign IPs dynamically. As the IP addresses rotate, be assured that you will be able to find your server!

## Initial Setup

### Database Support

ALT uses [firebase](https://www.firebase.com) to store the list of nodes and IPs. This means that the first step to get up and running is to head over there and create a free account.

### Installing Alt

    curl https://raw.githubusercontent.com/WhiteBoardDev/address-location-tool/master/installation/install.sh | sudo bash

### Adding a node via ALT

Adding your first node to the database will require modifying two configuration files. The first configuration file is for your database configuration (`conf/db.json`). Start by editing the `conf/db.tpl` file and add your firebase url and secret:

     {
         "db": "firebase",
         "config": {
            "url": "firebase address location",
            "secret": "firebase secret"
         }
    }

Next edit the alt configuration (`conf/alt.json`). Start by editing the `conf/alt.tpl` file. Adding port numbers for webservices is optional.

    {
        "node": {
            "name": "node name",
            "ports": [ 8080, 8090 ]  <-- array of port numbers
        }
    }

Now run the following:

    python app.py alt dev

The 'alt' is the run module and 'dev' is the environment variable. Eventually the 'dev' variable will only be used for debugging and can be omitted.


### Using the Node list in Firebase

Now that we have a a bunch of node ips tracked in firebase its time to do something with them.
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


## Other uses for ALT

After the nodes are populated in the database, we could use this to create host files, nginx proxies, etc.

### Creating an nginx proxy

An nginx proxy file can be created for all nodes that has the same external ip address of the nginx server. It also must nodes with ports that match the internal port numbers. The internal port number will be proxied to the external port number. Edit the proxy configuration (`conf/proxy.json`). Start by editing the `conf/proxy.tpl` file:

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
	
Run with:

	python app.py proxy dev

### Updating hosts file

Hosts file can be updated with ALT nodes that match the external ip address. The file in dev mode will create an `alt-hosts` file.

Run with:

	python app.py hosts dev

## Dev Environment Setup


### Install via pip

Modules used for this project are installed via [pip](https://pip.pypa.io/en/stable/installing/)


    pip install requests
    pip install netifaces



## License

MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

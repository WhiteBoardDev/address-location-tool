# Address Location Tool (ALT)

ALT is an alternative to dynamic DNS services like no-ip and dyndns. Its goal is to be able to track IPs of
systems located on internet service providers which assign IPs dynamically. As the IP addresses rotate, be assured
that you will be able to find your server!

## Initial Setup

ALT uses [firebase](https://www.firebase.com) to store the list of nodes and IPs. This means that the first step to get up
and running is to head over there and create a free account.

If you want to track a computer's address, you want to run the `alt_updater.py` script.  
This script does require the requests python module so make sure to install this first. I can be done with `pip`


    pip install requests



## Adding your first nodes

Now we need to make a configuration file to feed into the updater so it knows how to behave. Here is an example:

        {
          "node":{
            "name":"node1"
          },
          "firebase":{
            "url": "https://my-firebase-url.firebaseio.com",
            "secret": "my-secret-key"
          }
        }


Now run the `alt_updater.py` and pass in the path to the `config.json` file

        python alt/alt_updater.py config.json 



#License

MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
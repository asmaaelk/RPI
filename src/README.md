# Networks LED Project README
## Asmaa Elkeurti, Kiel Martyn, Ramya Puliadi

### Abstract
Our program hosts a single page web server that allows visitors to change the brightness of LEDs connected to the host Rasberry Pi 2. Any number of LEDs can be attached to the Pi, as long as they are connected to GPIO pins. The webpage is very simple, containing only some text, two drop down forms (one for pin number, one for brightness level), and a submit button. To keep the state of the brightness level of the LEDs, our program has second thread as is required by the GPIO library we're using.

### Environmental Reproduction
**Dependences:**

* *Python 2.7*
* [*Flask*](http://flask.pocoo.org/docs/0.10/)
* [*virtualenv*](https://virtualenv.pypa.io/en/latest/)
* [*RPi.GPIO*](https://pypi.python.org/pypi/RPi.GPIO)

We're using *Flask*, a *Python* microframework, to host our web server.  *virtualenv* is required to setup and run *Python* programs using *Flask*.  Installation instructions can be found [here](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart).

We're controlling the LEDs with a *RPi.GPIO*.  We used a Rasbperry Pi 2 during development, so LEDs can be connected only to the GPIO pins of the Pi 2. A list of valid pin numbers can be found in **Usage Guidelines**.  There is no limit in our program on the number of LEDs attached to the bread board.

### Compilation Instructions (Project Setup)
Once *virtualenv* and *Flask* have been installed, a *virtualenv* project needs to be created with:

```
$ mkdir myproject
$ cd myproject
$ virtualenv venv
```

### Execution Instructions
Once the project is setup, extract our files into ```/myproject```

Then activate *virtualenv* on Linux/OS X with:

```$ . venv/bin/activate```

or on Windows with:

```$ venv\scripts\activate```

Finally the script can be executed with *Python*.


### Usage Guidelines
To access our webpage from the host Rasbperry Pi's browser, simply go to the URL: 

```http://127.0.0.1:5000```

or on another computer by typing in the Pi's address and specifying the port:

```http://<IP Address>:5000```

To change the LEDs' state with *cURL* commands, follow the below format (replacing ```<LEVEL>```, ```<PIN>```, and ```<IP>```):

```$ curl --data “Brightness<LEVEL>=&Index=<PIN>an n” <IP>:5000```

* Level signifies the brightness percentage. It should be replaced with either `0`, `25`, `50`, `75`, or `100`.
* Pin corresponds to where the LED is connected to the Pi. The server will only accept the numbers of the Raspberry Pi 2's GPIO pins: `3`, `5`, `7`, `8`, `10`, `11`, `13`, `15`, `16`, `18`, `19`, `21`, `22`, `23`, `24`, or `26`.
* Replace ```<IP>``` with the target Pi's IP address.
* The port number is hard coded in our *Python* script to ```5000```.

Example:

```$ curl --data “Brightness=100&Index=13” 192.168.3.2:5000```
# huecli
---
huecli is a cli application that can be used to control simple functions of philips hue lights

### Usage:
```
usage: hue [-h] ...

positional arguments:
  {list,switch,color}

optional arguments:
  -h, --help           show this help message and exit

```
```
$ hue color --help
usage: hue color [-h] [-d] [-g] ID COLOR

Change color of lights

positional arguments:
  ID           ID of the light or group to manipulate
  COLOR        Hex color to change light to.

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Add extended output.
  -g, --group  Use group instead of light.
```
```
$ hue switch --help
usage: hue switch [-h] [-d] [-g] SUBCOMMAND ID

Switch lights on and off. Supported subcommands are: off, on

positional arguments:
  SUBCOMMAND   Subcommand for switch command.
  ID           ID of the light or group to manipulate

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Add extended output.
  -g, --group  Switch group instead of light.
```
```
$ hue list --help
usage: hue list [-h] [-d]

List available lights

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Add extended output.
```
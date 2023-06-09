# GravitationalGUI

GravitationalGUI is a simple Python script useful for the numerical simulation of N-body gravitational systems, with a graphical window to see the real time evolution of the bodies. In order to run the script just type the following command from the `GravitationalGUI` directory:

`./gravGUI.py` <br/>

This is the main window:

![app screenshot](imgs/main.png?raw=true)

If you click on one drawn point, this will open a new window containing all its features; this is an example for the point showed in the previous picture: 

![app screenshot](imgs/point.png?raw=true)

# How to set up

Clone the repository:

`git clone https://github.com/cintuluca/atmi` <br/>

Move to the `GravitationalGUI` directory:

`cd GravitationalGUI` <br/>

To control and install the dependencies:

`pip install -r requirements.txt` <br/>

## GravitationalGUI requirements:

`numpy (>=1.22.4)` <br/>
`tk (>=0.1.0)` <br/>

# AUTHOR

Luca Cintura <luca.cintura@gmail.com> <br />

# License

Atmospheric Impact Simulation (ATMI)

Copyright (c) 2023, Luca Cintura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

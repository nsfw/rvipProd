The PixLite is configured as such:

    +------------------------------------------------+
    | Outputs 9-16                     Power for 9-16|
    | Ethernet Port                                  |
    | Outputs 1-8                      Power for 1-8 |
    +------------------------------------------------+

The TOP Panels plug in to the TOP of the board, starting at the left - 9-12
The BOTTOM Panels plug in to the BOTTOM of the board, "   "    "     - 1-4

Use the WINDOWS PROGRAM "Advatek Assistant" to setup the board.

On the Control Tab:

    IP Address: 192.168.1.22
    Type of IP: Static
    Ethernet Protocol: sACN (E1.31)

On the Control Tab, set "Advanced", and then by clicking on the Advanced button, configure:

              Univ  Chan  Num Pixels  Intensity Limit%
     Output  1: 5     1     100       80
     Output  2: 6     1     100       80
     Output  3: 7     1     100       80
     Output  4: 8     1     100       80

     Output 13: 4     1     100       80
     Output 14: 3     1     100       80
     Output 15: 2     1     100       80
     Output 16: 1     1     100       80

Under LEDS:

    Pixel ID: WS2811/12
    Speed: FAST
    color sequence:           GRB
    Set Gamma:                1.0 (default is 2.0)

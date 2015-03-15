The PixLite is configured as such:


    +------------------------------------------------+
    | Outputs 9-16                     Power for 9-16|
    | Ethernet Port                                  |
    | Outputs 1-8                      Power for 1-8 |
    +------------------------------------------------+

The TOP Panels plug in to the TOP of the board, starting at the left - 9-12
The BOTTOM Panels plug in to the BOTTOM of the board, "   "    "     - 1-4

Using the WINDOWS PROGRAM :( "Advatek Assistant", on the "Control" tab, Advanced button, configure:

              Univ  Chan  Num Pixels
     Output  1: 4     1     100
     Output  2: 5     1     100
     Output  3: 6     1     100
     Output  4: 7     1     100

     Output 13: 1     1     100
     Output 14: 2     1     100
     Output 15: 3     1     100
     Output 16: 4     1     100

Under LEDS:

    color sequence:           GRB
    Maximum output intensity: 80%
    GAMMA:                    1.0 (default is 2.0)

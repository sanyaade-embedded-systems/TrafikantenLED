#!/usr/bin/env python
# -*- coding: utf-8 -*-

def widthOfLetter(gfx):
    width = 8
    for col in [1, 0]:
        for shifter in range(0, 8, 2):
            occupied = False
            for row in range(0, len(gfx)):
                if gfx[row][col] & (0b11 << shifter) != 0:
                    return width
                else:
                    occupied = True
            width -= 1
    return width

class LedFont:
    def __init__(self):
        self.font = {}
        self.font[' '] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['-'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]

        self.font['/'] = [ [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['.'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]

        self.font[u','] = [[ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ] ]

        self.font[u':'] = [[ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['!'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['0'] = [ [ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['1'] = [ [ 0b00001100, 0b00000000 ],
                           [ 0b00111100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['2'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['3'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['4'] = [ [ 0b00000011, 0b00000000 ],
                           [ 0b00001111, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['5'] = [ [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['6'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['7'] = [ [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['8'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['9'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['a'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['b'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['c'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['d'] = [ [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['e'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['f'] = [ [ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['g'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ] ]
        
        self.font['h'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['i'] = [ [ 0b00110000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['j'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ] ]
        
        self.font['k'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11001100, 0b00000000 ],
                           [ 0b11110011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['l'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['m'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11110011, 0b00000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['n'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11001111, 0b00000000 ],
                           [ 0b11110000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['o'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['p'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ] ]
        
        self.font['q'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ] ]
        
        self.font['r'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11001111, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['s'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['t'] = [ [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['u'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['v'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['w'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b00110011, 0b00110000 ],
                           [ 0b00001100, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['x'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['y'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ] ]
        
        self.font['z'] = [ [ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b11111111, 0b01100000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'æ'] = [[ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111100, 0b11110000 ],
                           [ 0b00000011, 0b00001100 ],
                           [ 0b00111111, 0b11111100 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b00111100, 0b11111100 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'ø'] = [[ 0b00000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b11000011, 0b11000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11110000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'å'] = [[ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['A'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['B'] = [ [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['C'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['D'] = [ [ 0b11111100, 0b00000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['E'] = [ [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['F'] = [ [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['G'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000011, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['H'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['I'] = [ [ 0b11111100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11111100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['J'] = [ [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['K'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11001100, 0b00000000 ],
                           [ 0b11110000, 0b00000000 ],
                           [ 0b11001100, 0b00000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['L'] = [ [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['M'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11110011, 0b11000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['N'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11110000, 0b11000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11000011, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['O'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['P'] = [ [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['Q'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11001100, 0b11000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b00111100, 0b11110000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['R'] = [ [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['S'] = [ [ 0b00111111, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['T'] = [ [ 0b11111111, 0b11000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['U'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00111111, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['V'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['W'] = [ [ 0b11000000, 0b00001100 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b11000000, 0b00001100 ],
                           [ 0b11000011, 0b00001100 ],
                           [ 0b11001100, 0b11001100 ],
                           [ 0b00110000, 0b00110000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['X'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['Y'] = [ [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font['Z'] = [ [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b11000000 ],
                           [ 0b00000011, 0b00000000 ],
                           [ 0b00001100, 0b00000000 ],
                           [ 0b00110000, 0b00000000 ],
                           [ 0b11000000, 0b00000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'Æ'] = [[ 0b00111111, 0b11110000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11111111, 0b11110000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11000011, 0b00000000 ],
                           [ 0b11000011, 0b11110000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'Ø'] = [[ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11110000 ],
                           [ 0b11000000, 0b00110000 ],
                           [ 0b11000011, 0b00110000 ],
                           [ 0b11001100, 0b00110000 ],
                           [ 0b11110000, 0b00110000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]
        
        self.font[u'Å'] = [[ 0b00001100, 0b00000000 ],
                           [ 0b00110011, 0b00000000 ],
                           [ 0b00111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11111111, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b11000000, 0b11000000 ],
                           [ 0b00000000, 0b00000000 ] ]

        self.font[u'#'] = [[ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ],
                           [ 0xff, 0xff ] ]

        self.widths = {}
        for letter in self.font.keys():
            self.widths[letter] = widthOfLetter(self.font[letter])
            #print "Letter=%s width=%s" % (letter, widths[letter])
        self.widths[' '] = 5
        self.widths[u','] = 4
        for i in range(0, 10):
            self.widths[str(i)] = 5

    def __getitem__(self, key):
        return self.font[key]

    def width(self, key):
        return self.widths[key]

    def widthOfString(self, string):
        width = 0
        for letter in string:
            width += self.widths[letter]
        return width

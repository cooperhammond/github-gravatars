import random
from sys import stdout
import Image

def generate(r, size):
    # r must be an odd number
    scale = size / r
    s = size + scale
    colors = [(170, 126, 223), (137, 225, 138), (210, 107, 74)]
    color = colors[random.randrange(0, len(colors))]
    bg = (240, 240, 240)
        
    lines = []
    for i in range(0, r):
        line = []
        for n in range(0, r / 2 + 1):
            if random.randrange(0, 2) == 0:
                line.append("#")
            else:
                line.append(" ")
        for i in reversed(line[:(r / 2)]):
            line.append(i)
        lines.append(line)
        
    pixels = []
    
    for n_ in range(0, scale / 2):
        row = []
        for n_ in range(0, s):
           row.append(bg)
        pixels.append(row)
    
    for i in lines:
        for n_ in range(0, scale):
            row = []
            for n_ in range(0, scale / 2):
                row.append(bg)
            for n in i:
               if n == "#":
                   for n_ in range(0, scale):
                       row.append(color)
               else:
                   for n_ in range(0, scale):
                       row.append(bg)
            for n_ in range(0, scale / 2):
                row.append(bg)
            pixels.append(row)
    
    for n_ in range(0, scale / 2):
        row = []
        for n_ in range(0, s):
           row.append(bg)
        pixels.append(row)
    
    pixels = sum(pixels, [])

    im = Image.new("RGB", (s, s))
    im.putdata(pixels)
    im.save('gravatar.png')
    
if __name__ == "__main__":
    generate(5, 420)
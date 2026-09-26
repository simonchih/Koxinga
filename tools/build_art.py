"""Pack generated art into the original game's exact asset sizes and formats.

Run from any directory: python tools/build_art.py
The illustrated masters are generated with imagegen; this only slices the atlas,
typesets game symbols, and assembles resolution-compatible UI components.
"""
from pathlib import Path
import json
import re
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
NAVY = '#072338'
GOLD = '#d8ad58'
CREAM = '#ffedbe'
COLORS = ['#50b9ef', '#70c69a', '#ecd36c', '#ed7969', '#e7a763', '#ba9cde']
SCALE = 4
atlas = Image.open(ROOT / 'art/icons-master.png').convert('RGB')
names = ['food', 'gold', 'cannon', 'treasure', 'move', 'compass', 'die', 'fire', 'scroll', 'anchor', 'admiral', 'win']
icons = {}
for i, name in enumerate(names):
    x, y = i % 4, i // 4
    icons[name] = atlas.crop((x*atlas.width//4, y*atlas.height//3, (x+1)*atlas.width//4, (y+1)*atlas.height//3))

def font(size):
    return ImageFont.truetype(str(ROOT / 'wqy-zenhei.ttf'), size*SCALE)

def panel(size, color=NAVY):
    im = Image.new('RGB', (size[0]*SCALE, size[1]*SCALE), color)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, im.width-3, im.height-3), radius=6*SCALE, outline=GOLD, width=2*SCALE)
    d.rounded_rectangle((4*SCALE, 4*SCALE, im.width-4*SCALE, im.height-4*SCALE), radius=3*SCALE, outline='#6e643e', width=1)
    return im

def label(im, text, xy, size=12, fill=CREAM):
    ImageDraw.Draw(im).text((xy[0]*SCALE, xy[1]*SCALE), text, font=font(size), fill=fill, anchor='mm', stroke_width=0)

def icon(im, name, box):
    box = tuple(int(v*SCALE) for v in box)
    im.paste(ImageOps.fit(icons[name], (box[2]-box[0], box[3]-box[1])), box[:2])

def build(name, size):
    w,h = size
    im = panel(size)
    if name.startswith('Formosa'):
        return ImageOps.fit(Image.open(ROOT/'art/ocean-master.png'), size)
    if name.startswith('die-'):
        a,b = map(int, re.findall(r'\d', name))
        d=ImageDraw.Draw(im)
        d.polygon([(25*SCALE,5*SCALE),(44*SCALE,16*SCALE),(41*SCALE,44*SCALE),(25*SCALE,53*SCALE),(7*SCALE,43*SCALE),(6*SCALE,16*SCALE)], fill='#174c73', outline=GOLD, width=2*SCALE)
        label(im,str(a),(24,28),23)
        label(im,str(b),(38,44),9, '#98c9df')
    elif name.startswith('back') and re.match(r'back\d', name):
        pid=int(name[4]); icon(im,'compass',(31,5,70,44))
        label(im,str(pid+1),(14,25),15,COLORS[pid])
        ImageDraw.Draw(im).line((7*SCALE,44*SCALE,93*SCALE,44*SCALE), fill=COLORS[pid], width=2*SCALE)
    elif '_100x50' in name and not name.startswith('button'):
        first,second = name.split('_')[:2]
        for i,token in enumerate((first,second)):
            key = 'move' if token in ('-1','-2','back') else token
            icon(im,key,(i*50+5,9,i*50+45,43))
            label(im,'日' if i==0 else '夜',(i*50+11,7),7)
            if token.startswith('-') or token=='back':
                label(im,token if token!='back' else '←',(i*50+35,36),13)
        ImageDraw.Draw(im).line((50*SCALE,5*SCALE,50*SCALE,45*SCALE),fill=GOLD,width=SCALE)
    elif name.startswith('pawn'):
        pid=['2','3','4','5','6','8'].index(name[4])
        im=panel(size,COLORS[pid]); icon(im,'move',(3,3,17,17))
        label(im,str(pid+1),(5,6),7)
    elif name.startswith('turn'):
        pid=int(name[4]); icon(im,'anchor',(6,5,44,44)); label(im,str(pid+1),(25,27),20,COLORS[pid])
    elif name.startswith('wood'):
        im=panel(size, '#225675' if 'selected' in name else '#162f3d')
        d=ImageDraw.Draw(im)
        for x,y in [(5,5),(w-5,5),(5,h-5),(w-5,h-5)]:
            d.ellipse(((x-1)*SCALE,(y-1)*SCALE,(x+1)*SCALE,(y+1)*SCALE),fill=GOLD)
    elif name.startswith('button'):
        im=panel(size,'#26465a')
    elif name.startswith('arrow') or name.startswith(('clockwise','counter_clockw')):
        label(im,'↑' if name.startswith('arrow') else ('↻' if name.startswith('clockwise') else '↺'),(w/2,h/2),int(h*.7))
    else:
        key = name.split('_')[0]
        key = {'12f':'die','start':'compass'}.get(key,key)
        icon(im,key,(2,2,w-2,h-2))
        ImageDraw.Draw(im).rounded_rectangle((1,1,im.width-2,im.height-2),radius=4*SCALE,outline=GOLD,width=SCALE)
    return im.resize(size,Image.Resampling.LANCZOS)

if __name__ == '__main__':
    manifest=json.loads((ROOT/'art/legacy-assets.json').read_text())
    for name,size in manifest.items():
        im=build(name,tuple(size))
        target=ROOT/'Image'/name
        if target.suffix=='.jpg': im.save(target,quality=95,subsampling=0)
        else: im.save(target)
    # Larger source sprites are available for the new HUD and title screen.
    for name,im in icons.items():
        im.resize((256,256),Image.Resampling.LANCZOS).save(ROOT/'Image'/f'ui_{name}.png')
    Image.open(ROOT/'art/cover-reference.png').resize((256,256)).save(ROOT/'koxinga_default.ico')
    print(f'Rebuilt all {len(manifest)} legacy assets and {len(icons)} HUD assets.')

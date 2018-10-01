import glob
import pathlib

GITHUB_REPO = "https://github.com/ChoccyHobNob/EightBit-Atari-Fonts/raw/master/"

with open('index.html', 'w') as f:
    print('<html>\n<head><title>Atari Fonts</title></head><body>\n', file=f)
    fonts = [pathlib.Path(fn) for fn in glob.glob('*/*.png') if 'original' not in fn.lower()]

    for fontimg in fonts:
        fontname = str(fontimg).rstrip('-sample.png')
        fontttf = (fontname + '.ttf').replace(' ', r'%20')
        line = ('<div class="font">\n'
                '\t<a href="{REPO}{fontttf}">{fontname}</a><BR/>\n'
                '\t<a href="{REPO}{fontttf}"><img src="{fontimg}"/></a><BR/>\n'
                '</div>\n').format(REPO=GITHUB_REPO, fontttf=fontttf, fontimg=str(fontimg).replace(' ', r'%20'), fontname=fontname)
        print(line, file=f)

    print('</body></html>', file=f)

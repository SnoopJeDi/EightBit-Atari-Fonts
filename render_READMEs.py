"""
  Render a README.md with font sample images for each directory
"""
import glob
import pathlib

GITHUB_PREFIX = "https://github.com/ChoccyHobNob/EightBit-Atari-Fonts/raw/master/"

cwd = pathlib.Path('.')

for groupdir in [d for d in cwd.iterdir() if d.is_dir() and 'original' not in d.name.lower()]:
    with open(str(groupdir.joinpath('README.md')), 'w') as f:
        print('# Fonts in this directory\n', file=f)
        for img in [i for i in groupdir.iterdir() if i.name.endswith('.png')]:
            fontname = str(img.name).rstrip('-sample.png')
            print('## {fontname}\n![{fontname}]({img})\n'.format(fontname=fontname, img=GITHUB_PREFIX+str(img).replace(' ', r'%20')), file=f)

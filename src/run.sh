#!/bin/bash
sed -i "s/        'HOST':'172.17.0.1',/        'HOST':'$1',/"g HelloCovid/settings.py
echo $0 > whatrun
apache2ctl -D FOREGROUND



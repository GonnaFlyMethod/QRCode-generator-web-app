source $HOME/.poetry/env
cd $HOME/QRCode-generator-web-app/app
poetry run gunicorn -w 3 app:app

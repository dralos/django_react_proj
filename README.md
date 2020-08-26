# django_react_proj


#requisiti minimi 
python3 pip, nodejs e npm 

# step 1 install python-env dove vai a mettere tutte le tue dependency
sudo apt install -y python3-venv

# step 2 crea enviorement 
python3 -m venv env_name

# step 3 activa la il tuo env
source logrocket_env/bin/activate

# step 4 prendi la solution al interno del tuo env
git clone https://github.com/dralos/django_react_proj.git

# step 5 installa i requisiti  - qui usiamo pip e non pip3 perche l'enviorement lo abbiamo creato con python3 quindi tutto al suo interno fara' rifferimento a python3
pip install django djangorestframework django-cors-headers

# step 6 crea il db per questa solution in specifico ( se non hai bisogno di db puoi scartare questa parte) 
python manage.py migrate 

# step7 fai partire il server BE
python manage.py runserver

per il FrontEnd 
# step 1 entrare nella cartella students-fe

# step 2 prendere i paccheti da npm
npm install

# step 3 far partire il server FE 
npm start 

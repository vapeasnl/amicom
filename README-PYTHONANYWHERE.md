Déploiement sur PythonAnywhere

1) Créez un compte sur https://www.pythonanywhere.com et connectez-vous.

2) Forkez/clônez ce dépôt ou utilisez l'URL du repo: https://github.com/vapeasnl/amicom.git

3) Dans PythonAnywhere, créez un new web app (Choose Manual configuration -> Flask -> Python 3.11 or compatible).

4) Déployez le code dans un virtualenv; installez les dépendances:

```bash
python -m venv ~/venv/amicom
source ~/venv/amicom/bin/activate
pip install -r requirements.txt
```

5) Configurez le WSGI file (PythonAnywhere) pour pointer vers `app.py`:

- Remplacez le contenu du WSGI file par:

```python
import sys
import os
path = '/home/yourusername/amicom'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

6) Placez les fichiers statiques à la racine du projet (index.html, css/, js/, images/). Le `app.py` fourni sert ces fichiers directement.

7) Reload the web app on PythonAnywhere. Ouvrez l'URL fournie et vérifiez le site.

Notes:
- Si vous utilisez un domaine personnalisé, configurez les paramètres DNS selon PythonAnywhere.
- Pour un usage en production, désactivez `debug=True` dans `app.py` et utilisez un virtualenv Python récent.


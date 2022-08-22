import sys
import os
basedir = os.path.abspath(os.path.dirname(".."))
sys.path.insert(0, basedir)

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
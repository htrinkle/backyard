python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=application.py
flask run

echo "# backyard" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/htrinkle/backyard.git
git push -u origin master

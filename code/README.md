# Working with our code

Many of these chapters and their code are meant to stand alone. You probably don't want to run all chapters at once, especially with the various pytest.ini configurations.

However, we have included a `requirements.txt` file so you can get all the dependencies and plugins set up in a single statement.

Just create a virtual environment (`python3 -m venv venv --prompt .`) and activate it (`. venv/bin/activate` on macOS and Linux or `venv\scripts\activate.bat` on Windows). Then install the requirements (`pip install -r requirements.txt`).

You also need to install the **cards** project. With the virtual environment active and in this folder containing this readme.md, run:

```bash
pip install ./cards_proj
```
Welcome to the Juicy Project results!

Installation:

1. Download all files and folders to a single directory.  You'll run all python files from this directory.

2. item_one.py, item_two.py, and item_three.py can all be run in a simple command line interface using Python 3.
	a. Run item_one.py, it will generate a JSON file called item_one.json, containing the results of the item
	b. Before you run item_two.py or item_three.py, you must run text_file_juices.py, which uses the Nutritionix API to create a JSON file called juices.json.  I included this interim step so that you wouldn't have to make repeated requests to Nutritionix!
	c. You can now run item_two.py and item_three.py.  They will generate files item_two.json and item_three.txt, respectively

3. item_four.py requires Flask to run.  If you don't have Flask, use pip to install it:
	$ pip install Flask
	pip is included in Python 3.7, but if you don't have it, install it:
	a. Download https://bootstrap.pypa.io/get-pip.py
	b. Run the installer:
		$ python get-pip.py

4. To run item_four.py from Windows, you have to use Flask.
	a. Note:  like items two and three, item_four.py requires that you run text_file_juices.py first.
	b. Use the following commands:
		$ set FLASK_APP=item_four.py
		$ flask run
	c. Then use Firefox or Chrome to navigate to the link given in the command line.  Voila!  A Juicy webpage.
	d. Don't forget to CTRL-c from the command line when you're finished!

Please see project_notes.txt for additional notes, code compromises, and other information.

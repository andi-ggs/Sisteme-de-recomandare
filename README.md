# Sisteme-de-recomandare
Sisteme de recomandare, master eGov, anul 1.

This Python script uploads country data from a CSV file generated through data.world website into a Recombee database. It connects to the Recombee account using database ID, private token, and region, then clears existing items before adding new ones from the provided CSV file.

To run it, the recombee-api-client library needs to be locally installed using the command pip install recombee-api-client. The CSV file, named tari.csv, should include the columns country, capital, area, and continent.

Before running the script, update the Recombee credentials in the code with your own database ID and private token. Once set, run the script using python lab1.py. The program will delete all current items in your Recombee database, read each line from the CSV, and add a new item for each country with its name, capital, area, and continent. When the process is complete, it will print a confirmation message: “Data is added to Recombee!”

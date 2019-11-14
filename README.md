<h1>IMDB_Analysis</h1>
<h2>Python scripts for parsing IMDB data into a graph representing relationships between movies and the actors who act in them, and for analyzing the resulting graphs.</h2>

This code uses data downloaded from IMDB.

For usage,  use <a href="https://datasets.imdbws.com/">this link</a> to download title.basics.tsv.gz, name.basics.tsv.gz, title.ratings.tsv.gz, and title.principals.tsv.gz Extract, and rename resulting data.tsv files to the name of it's respective zip file (minus the .gz) and put in the working directory.

Note: Depending on your computer, calling generate_adj_list from IMDBparse.py may take up to 30 minutes as it has almost 3GB of data to process, and Python is not known for it's speed.

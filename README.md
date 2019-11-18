<h1>IMDB_Analysis</h1>
<h2>Python scripts for parsing IMDB data into a graph representing relationships between movies and the actors who act in them, and for analyzing the resulting graphs.</h2>

This code uses data downloaded from IMDB.

For usage,  use <a href="https://datasets.imdbws.com/">this link</a> to download title.basics.tsv.gz, name.basics.tsv.gz, title.ratings.tsv.gz, and title.principals.tsv.gz Extract to yield the .gz files (on windows it may extract to folder containing data.tsv, rename to the previous name (minus .gz) and put in script directory.

To perform network analysis:

![Example image]
(demo/example.png)

par.generate_adj_list("folder", 50000) parses the .tsv files, and creates a new directory (in this case called folder) containing an encoding of the graph where only movie titles with 50k ratings or above are contained (actors who do not appear in any of these movies are purged).

ana.analyze("folder") reads the graph encodings from the directory "folder", performs calculations, and displays results. Currently, to tweak calculations you must edit IMDBanalyze.py manually. I will simplify this later.


Python-vs-Java-forks
====================

Visualising usage of Python and Java throughout the world using [WebGL Globe](http://www.chromeexperiments.com/globe).

**I cannot vouch for the data as this was a primitive test that I did to get used to BigQuery and WebGL Globe.**

Data taken from [GitHub Archive](http://www.githubarchive.org/) dataset up on [Google BigQuery](https://developers.google.com/bigquery/).

Initially I wanted to compare Python, Ruby and Java, but the data was not at all good (yes, I made mistakes but that's the good thing about learning, you are free to make mistakes).

Query used to filter the data:

    SELECT repository_name, actor_attributes_location, repository_forks
    FROM [githubarchive:github.timeline]
    WHERE type="PushEvent"
        AND repository_language="Python"
        AND NOT actor_attributes_location CONTAINS "http"
    GROUP BY repository_name, actor_attributes_location, repository_forks
    ORDER BY repository_forks DESC
    
Run Locally
============

`cd` to the directory `globe`. If you're using python (like me), run
    python -m SimpleHTTPServer
    
Open `http://localhost:8000` in your browser.

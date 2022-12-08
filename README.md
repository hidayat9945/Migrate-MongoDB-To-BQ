# Migrate-MongoDB-To-BQ
## What is this for?
This includes one function to retrieve data from a collection in MongoDB. It helps changing `_id` from object to string.

## What is in it?
There are 2 python files in the repository.
- `logger.py`: contains a logger object to display what process is happening.
- `mongo_helpers.py`: contains functions that relates to MongoDB.

## What is required to setup?
Create a `.env` that contains a connection string URI. Following is the template for `.env` file.
```
MONGO_URI=your-connection-string-URI
```

## How to run the program?
I suggest to create a virtual environment in your local to separate current project with the other projects. It can be done by following [this documentation](https://docs.python.org/3/library/venv.html).
1. Clone this repo to your local.
2. Install all dependencies as dropped in `requirements.txt` file.
3. Import the function to your main program.
    ```python
    from mongo_helpers import retrieve_docs_from_mongo

    data = retrieve_docs_from_mongo(
        database=database_name,
        collection=collection_name,
        query={your-mongo-query}
    )
    ```
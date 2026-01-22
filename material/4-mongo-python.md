# MongoDB with Python

In the fourth part of the course, we learn how to use MongoDB with the Python programming language. During this part, you will learn how to build a database application using Python and the PyMongo package.

## PyMongo

[PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/) is a Python package containing tools for working with MongoDB and is the recommended way to work with MongoDB from Python. With PyMongo, we can execute similar database operations as we did with the MongoDB Shell, but using Python. This is handy when we want to implement database applications instead of just executing queries.

```mermaid
flowchart LR
    app(Python application)-- Database query --> db[(MongoDB Database)]
    db-- Query response --> app
```

First things first, we need to install the PyMongo package. To install external packages, like PyMongo, we need to use a package installer tool, such as [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/). On a Windows computer, execute (type in the command and press the <kbd>Enter</kbd> key) the following command in the [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.4) application, and on a macOS computer in the [Terminal](https://support.apple.com/en-gb/guide/terminal/welcome/mac) application:

```bash
python -m pip install pymongo
```

> [!TIP]  
> If the command doesn't work, try the `python3` command instead of the `python` command. The correct command depends on the Python installation.

> [!TIP] 
> In more complicated Python projects, packages are installed within project-specific [virtual environments](https://www.w3schools.com/python/python_virtualenv.asp).

Next, let's do some simple MongoDB operations with PyMongo in _small steps_:

1️⃣ Create a Python program that imports the `pymongo` library:

```python
from pymongo import MongoClient
```

2️⃣ In that program, initialize a `MongoClient` object and see that the database connection works:

```python
from pymongo import MongoClient

# "mongodb://localhost:27017/" is a connection string. It specifies which database server we are connecting to
# In this case, we connect to the MongoDB server on our own computer (localhost) on port 27017 (the default port for MongoDB)
client = MongoClient("mongodb://localhost:27017/")
# Change "library" to match the name of your database
db = client["library"]
```

> [!TIP]  
> If you want to connect to your cluster in the MongoDB Atlas instead, go through the [Connect to MongoDB](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/#atlas) guide. We want to keep the MongoDB Atlas connection string secret to prevent unauthorized access to our database. To achieve this, we shouldn't store the connection string in the code; instead, we should use an [environment variable](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/) for the connection string.

3️⃣ Print all the documents in one of the collections you inserted documents for in the previous part using the [find](https://www.w3schools.com/python/python_mongodb_find.asp) method. You can iterate the return value of the method using a `for` loop. The iterated items are [dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) in which the keys match the document's fields:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# Change "library" to match the name of your database
db = client["library"]
# Change the collection name to match the name of your collection
books = db.books.find()

for book in books:
  # Documents are generally turned into dictionaries in which there's a key for each field
  # The following code prints the value of the "title" field
  print(book["title"])
  # Try printing all the fields of a document
```

4️⃣ Try out other operations, e.g., by [inserting a document](https://www.w3schools.com/python/python_mongodb_insert.asp) into a collection.

Execute the program after each step and see that there are no errors.

> [!IMPORTANT]  
> Exercise 1 👨‍💻: Try out the database connection and the basic MongoDB operations using the `pymongo` library with your project's database by following the steps above. There's no need to include this prototyping code in the submission. Instead, use this code as a starting point for your database application.  

## Database application

Now that we know the basics of PyMongo, the last part of the course is to implement a database application for our project. At this point, you should have already designed the database schema and inserted some test data into the database. Use Python and PyMongo to implement a database application that uses the database. These are the requirements for the application:

- _Some kind of user interface_. The easiest way is to implement a command-line user interface that reads user input from the command line with the [input](https://www.w3schools.com/python/ref_func_input.asp) function and prints information with the [print](https://www.w3schools.com/python/ref_func_print.asp) function. You can use [this](./application.py) Python application as a starting point. If you want, you can also do something fancier, like a web application using [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/).
- Usage of _all CRUD (create, read, update, delete) operations_ for at least two collections. For the read operation, listing all documents in the collection is enough.

Implement the application _one simple feature at a time_ and confirm that it works before moving on to the next feature. Starting with a create feature of one of the collections is a good place to start. Use the MongoDB Compass to verify that different features work, for example, by checking that a document is added to a collection while using the create feature.

These PyMongo guides will be useful while implementing the CRUD features:

- [Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)
- [Find Documents](https://www.w3schools.com/python/python_mongodb_find.asp)
- [Update Documents](https://www.w3schools.com/python/python_mongodb_update.asp)
- [Delete Documents](https://www.w3schools.com/python/python_mongodb_delete.asp)
- [Sort Documents](https://www.w3schools.com/python/python_mongodb_sort.asp)

### Working with the `_id` primary key

The `_id` primary key is useful for referencing a specific document e.g. when finding, deleting or updating it. We just need to remember that the value of the `_id` field should be an `ObjectId` object:

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

# ...

book_id_to_find = "6780b2d277f48b749b940ee4"

# ❌ Using a string won't work, and the following code won't find the correct document
db.books.find_one({ "_id": book_id_to_find })

# ✔️ Using an ObjectId object will work
db.books.find_one({ "_id": ObjectId(book_id_to_find) })
```

### Relationships between documents

Consider how you establish relationships between documents, e.g. author of a book. For example, creating a `books` collection document with an author could be implemented in the following way:

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

# ...

def add_book():
  # Request other fields from the user...
  author_id = input("Author ID:")

  # 💡 Before inserting, we can also check that the author document exists to enforce referential integrity

  book = {
    # Other keys matching the document's fields...
    # We need to use an ObjectId object as the author field value
    "author": ObjectId(author_id)
  }

  db.books.insert_one(book)
```

In this case, the author could also be provided in a more user-friendly way by providing the author's full name and using it to find the corresponding author's `_id` field value.

### ⭐ Bonus: ideas for additional features

If you want to expand your application, here are some ideas for optional features:

- Filtering information (e.g, searching books based on name, author, category, or other properties).
- Statistics (e.g., number of books of each author). The [Aggregation Pipelines](https://www.w3schools.com/mongodb/mongodb_aggregations_intro.php) guide has examples of aggregation operations with PyMongo.
- To allow multiple users to use the same database, instead of a local MongoDB database, create a cluster in the [MongoDB Atlas](https://www.mongodb.com/products/platform/cloud) and [connect to it in your application](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/#atlas). We want to keep the connection string a secret to avoid unwanted people accessing our database. To achieve this, _we shouldn't store the connection string in the code_, instead, we should use an [environment variable](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/) for the connection string.

```python
# ❌ Bad, we don't want to expose the connection string or other secrets in the code
client = MongoClient("mongodb+srv://john:supersecret@cluster0.abcd123.mongodb.net...")

# ✔️ Good, connection string is stored in an environment variable and not visible in the code
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
```

> [!IMPORTANT]  
> Exercise 2 👨‍💻: Implement a Python database application based on the requirements.

## Submitting the project

You are done, good job! 🎉 The last thing to do is to submit the project. There are two ways to do it:

1. Create a _public_ [GitHub](https://github.com/) repository for the exercises and the project. This is the recommended way because it adds another cool project to your portfolio. But if you don't know anything about Git or GitHub, you don't have to learn it for this course. Add the link to the GitHub repository to the "MongoDB with Python" Moodle submission.
2. Add the project code to a folder and turn it into a compressed zip folder. Add the zip folder to the "MongoDB with Python" Moodle submission.

> [!IMPORTANT]  
> Exercise 3 👨‍💻: Submit your project work to the "MongoDB with Python" Moodle submission by following the instructions above. After the final submission, remember to give feedback for the course via the link in the Moodle's "Welcome" page.

Once you have done all the submissions in Moodle (from this part and the previous parts), your work will be reviewed after the final deadline. After the review, if there are no problems with your work, you'll get the credits. Otherwise, you'll be asked to make changes and resubmit your work.

<!-- TODO -->
> [!WARNING]  
> The final deadline for the coursework is on Sunday 17.5. at 23:59. _Final deadline is strict_ and submissions made after it won't be reviewed and no credits will be granted.

## ⭐ Bonus: Data validation with JSON Schema

Even if the structure of the collection's document in MongoDB is flexible, we usually still want to enforce some rules for the documents. For example, in the `books` collection, the `copies` attribute should only contain integer values greater than `0` and `genres` attribute an array of non-empty strings.

MongoDB supports document validation with the widely adopted [JSON Schema](https://json-schema.org/) validation standard. JSON Schema is a standard for describing the structure, rules, and constraints of JSON data, e.g. a document. For example, the following JSON Schema could be used to validate a `book` document:

```json
{
  "bsonType": "object",
  "required": ["title", "author", "year", "genres", "copies", "ebook"],
  "properties": {
    "title": {
      "bsonType": "string",
      "minLength": 1
    },
    "author": {
      "bsonType": "string",
      "minLength": 1
    },
    "year": {
      "bsonType": "int",
      "minimum": 0
    },
    "genres": {
      "bsonType": "array",
      "items": {
        "bsonType": "string",
        "minLength": 1
      }
    },
    "copies": {
      "bsonType": "int",
      "minimum": 0
    },
    "ebook": {
      "bsonType": "boolean"
    }
  }
}
```

Every time a document is inserted or updated in the collection with JSON Schema validation enabled, the document's structure must match the structure defined by the schema.

You can read more about how to enable JSON Schema validation for a collection by following the [MongoDB Schema Validation: A Practical Guide with Examples](https://www.datacamp.com/tutorial/mongodb-schema-validation) guide.

## ⭐ Bonus: Further reading

Here's some further reading to continue your NoSQL journey.

### MERN Stack

> _"MERN is a pre-built technology stack based on JavaScript technologies. MERN stands for MongoDB, Express, React, and Node, after the four key technologies that make up the stack."_ 
> — [MERN Stack Explained](https://www.mongodb.com/resources/languages/mern-stack)

- [Programming a server with NodeJS and Express (Fullstack Open)](https://fullstackopen.com/en/part3): Hands-on introduction to the MERN stack. 

### Redis

> _"Redis is an in-memory data store used by millions of developers as a cache, vector database, document database, streaming engine, and message broker. Redis has built-in replication and different levels of on-disk persistence. It supports complex data types (for example, strings, hashes, lists, sets, sorted sets, and JSON), with atomic operations defined on those data types."_
> — [Get started with Redis](https://redis.io/docs/latest/get-started/)

- [Get started with Redis](https://redis.io/docs/latest/get-started/): Install Redis and learn the basics.
- [redis-py](https://github.com/redis/redis-py): the Python interface to the Redis key-value store.

### DynamoDB

> _"Amazon DynamoDB is a serverless, fully managed, distributed NoSQL database with single-digit millisecond performance at any scale. DynamoDB addresses your needs to overcome scaling and operational complexities of relational databases. DynamoDB is purpose-built and optimized for operational workloads that require consistent performance at any scale"_
> — [What is Amazon DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

- [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html): Install DynamoDB and learn the basics.
- [Programming Amazon DynamoDB with Python and Boto3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html)

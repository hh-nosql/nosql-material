# Introduction to NoSQL database management systems

> _"When people use the term "NoSQL database", they typically use it to refer to any non-relational database. Some say the term "NoSQL" stands for "non-SQL" while others say it stands for "not only SQL". Either way, most agree that NoSQL databases store data in a more natural and flexible way. NoSQL, as opposed to SQL, is a database management approach, whereas SQL is just a query language, similar to the query languages of NoSQL databases."_
> — [What is NoSQL?](https://www.mongodb.com/resources/basics/databases/nosql-explained)

In the first part of the course, we will learn the principles of the NoSQL database management systems. During this part you will learn about the the main characteristics of NoSQL databases, the main differences between NoSQL and relational databases, and the main application areas of NoSQL databases.

NoSQL databases are a family of databases that differ from the relational databases. [MongoDB](https://www.mongodb.com/) document database, [Redis](https://redis.io/) key-value database and [neo4j](https://neo4j.com/) graph database are examples of such databases. NoSQL databases are widely adopted. Based on the [State of Database Survey](https://stateofdb.com/) in 2023, almost 75% of respondeds have used a NoSQL database and two NoSQL databases were among the top five most used databases. 

Here's a few examples how NoSQL databases are used within major companies:

- _Netflix_ powers several mission-critical applications with [Apache Cassandra](https://cassandra.apache.org/_/index.html), including member data, billing, recommendations, and subscriptions. Its distributed architecture allows Netflix to handle large amounts of data across multiple locations while maintaining high availability (source: [The Evolution of Cassandra Data Movement at Netflix](https://netflixtechblog.com/the-evolution-of-cassandra-data-movement-at-netflix-6e13329c80a1)).
- _Amazon Prime Video_ uses [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for playback, content ownership, downloads, offers, order fulfillment, libraries, subscriptions, rentals, and content discovery. Amazon migrated billions of rows from Oracle to DynamoDB to improve scalability and resilience (source: [Prime Video Boosts Scale and Resilience Using Amazon DynamoDB](https://aws.amazon.com/solutions/case-studies/prime_video_dynamodb/)).
- _Spotify_ uses [Google Cloud Bigtable](https://cloud.google.com/bigtable) for real-time personalization and music recommendations. Bigtable provides fast access to large volumes of user and behavioral data, supporting recommendation systems for millions of users (source: [Improving Bigtable single-row read throughput by 70%: How we did it](https://cloud.google.com/blog/products/databases/exploring-bigtable-read-throughput-performance-gains/)).

Familiarize yourself with the NoSQL database management systems by reading the [introduction slides](../slides/introduction.pdf) slides and the article [What is NoSQL?](https://www.mongodb.com/resources/basics/databases/nosql-explained). Once you have read through the materials, test your knowledge by completing the "Introduction to NoSQL database management systems" Moodle exam. After passing the exam, you can move on to the next part.

<!-- TODO -->

> [!WARNING]  
> To confirm the course participation, pass the "Introduction to NoSQL database management systems" Moodle exam before Thursday 29.10. at 23:59.

> [!IMPORTANT]  
> Exercise 1 👨‍💻: Read the materials mentioned above. Then, take and pass the "Introduction to NoSQL database management systems" multiple-choice Moodle exam related to the principles of the NoSQL database management systems. You have 45 minutes to complete the exam, and passing grade requires at least 69% of exam points. You can retake the exam two times in case you fail.

---

⏭️ [Move on to the next part](./2-mongo-introduction.md)

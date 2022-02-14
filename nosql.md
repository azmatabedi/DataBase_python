MongoDB is a NoSQL database that stores the data in form of key-value pairs. It is an Open Source, Document Database which provides high performance and scalability along with data modeling and data management of huge sets of data in an enterprise application.

MongoDB also provides the feature of Auto-Scaling. Since, MongoDB is a cross-platform database and can be installed across different platforms like Windows, Linux, etc.

A Document is nothing but a data structure with name-value pairs like in JSON. It is very easy to map any custom Object of any programming language with a MongoDB Document. For example, a Student object has attributes name, roll no, and subjects, where subjects are a List.

Document for Student in MongoDB will be like:

{
    name : "Stduytonight",
    rollno : 1,
    subjects : ["C Language", "C++", "Core Java"]
}

Apart from most of the NoSQL default features, MongoDB does bring in some more, very important and useful features :

MongoDB provides high performance. Input/Output operations are lesser than relational databases due to the support of embedded documents(data models) and Select queries are also faster as Indexes in MongoDB supports faster queries

MongoDB has a rich Query Language, supporting all the major CRUD operations. The Query Language also provides good Text Search and Aggregation features.
Auto Replication feature of MongoDB leads to High Availability. It provides an automatic failover mechanism, as data is restored through backup(replica) copy if a server fails.
Sharding is a major feature of MongoDB. Horizontal Scalability is possible due to sharding.
MongoDB supports multiple Storage Engines. When we save data in form of documents(NoSQL) or tables(RDBMS) who saves the data? It's the Storage Engine. Storage Engines manages how data is saved in memory and on disk.

MongoDB consists of a set of databases. Each database again consists of Collections. Data in MongoDB is stored in collections. The below figure depicts the typical database structure in MongoDB.

Database in MongoDB is nothing but a container for collections. We will learn how to create a new Database, drop a Database and how to use an existing Database in the coming lessons.
The collection is nothing but a set of MongoDB documents. These documents are equivalent to the row of data in tables in RDBMS. But, collections in MongoDB do not relate to any set schema as compared to RDBMS. Collections are a way of storing related data. Being schemaless, any type of Document can be saved in a collection, although the similarity is recommended for index efficiency.

SQL Database                            NoSQL Database (MongoDB)
Relational database                     Non-relational database
Supports SQL query language             Supports JSON query language
Table based                             Collection based and key-value pair
Row-based                               Document-based
Column based                            Field based
Support foreign key                     No support for foreign key
Support for triggers                    No Support for triggers
Contains schema which is predefined     Contains dynamic schema
Not fit for hierarchical data storage   Best fit for hierarchical data storage
Vertically scalable - increasing RAM    Horizontally scalable - add more servers
Emphasizes on ACID properties           Emphasizes on CAP 


Having seen the good features of MongoDB, now every developer should be able to understand why it is better to use NoSQL based database for big data transactions and for implementing a scalable model.


Data Model Design
MongoDB provides two types of data models: The embedded data model and the Normalized data model. Based on the requirement, you can use either of the models while preparing your document.
The example is giving below are separated for a different model
Embedded Data Model
In this model, you can have (embed) all the related data in a single document, it is also known as a de-normalized data model.


{
    _id: ,
    Emp_ID: "10025AE336"
    Personal_details:{
        First_Name: "Radhika",
        Last_Name: "Sharma",
        Date_Of_Birth: "1995-09-26"
    },
    Contact: {
        e-mail: "radhika_sharma.123@gmail.com",
        phone: "9848022338"
    },
    Address: {
        city: "Hyderabad",
        Area: "Madapur",
        State: "Telangana"
    }
}

I model the data for the specific station ID that is 201, this example belongs to the embedded model method.
Monitor station

{
   SiteID:"201"
}

Normalized Data Model
In this model, you can refer to the subdocuments in the original document, using references. For example, you can re-write the above document in the normalized model as

Personal_details:

{
    _id: <ObjectId102>,
    empDocID: " ObjectId101",
    First_Name: "Radhika",
    Last_Name: "Sharma",
    Date_Of_Birth: "1995-09-26"
}



Contact:
{
    _id: <ObjectId103>,
    empDocID: " ObjectId101",
    e-mail: "radhika_sharma.123@gmail.com",
    phone: "9848022338"
}



I model the data for the specific station ID that is 201, this example belongs to normalize model method.
Location:
{
    _id:<23423423>,
    SiteID:"201"
}

Considerations while designing Schema in MongoDB
Design your schema according to user requirements.

Combine objects into one document if you will use them together. Otherwise, separate them (but make sure there should not be a need for joins).

Duplicate the data (but limited) because disk space is cheap as compared to compute time.

Do joins while writing, not on reading.

Optimize your schema for the most frequent use cases.

Do complex aggregation in the schema.







coding implementation for the MongoDB

db.movie.insert({"SiteID":"213"})   in this way records are inserted in the database


In MongoDB default database is tested. If you didn't create any database, then collections will be stored in the test database.

db.dropDatabase()
this will drop the database 


 db.createCollection("mycol", { capped : true, autoIndexID : true, size : 6142800, max : 10000 } ){
"ok" : 0,
"errmsg" : "BSON field 'create.autoIndexID' is an unknown field.",
"code" : 40415,
"codeName" : "Location40415"
}
In nonrelational database table known as collection 
In MongoDB, you don't need to create a collection. MongoDB creates collection automatically when you insert some document.

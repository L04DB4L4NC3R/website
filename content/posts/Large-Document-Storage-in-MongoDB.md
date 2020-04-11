---
title: Large Document Storage in MongoDB
date: '2019-09-06T17:39:49.221Z'
thumb_img_path: https://miro.medium.com/max/4320/0*tBDOH0Bi9lRi1MUP
excerpt: A brief intro to GridFS
layout: post
---
A brief intro to GridFS

![](/images/Large-Document-Storage-in-MongoDB/0*tBDOH0Bi9lRi1MUP.jpg)

<figcaption>Photo by <a href="https://unsplash.com/@kmuza?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@kmuza?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener" target="_blank">Carlos Muza</a> on&nbsp;<a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener" target="_blank">Unsplash</a></figcaption>

**Introduction**

MongoDB has become the *go-to* database for no-SQL storage, and is running in thousands of production servers to date. Yet a majority of businesses use cloud native bucket storage technologies like *Amazon S3* for their day-to-day file storage needs.

Ever tried saving files directly in our own MongoDB instance? Or even a managed instance over the cloud? In any case, you’ll find answers here.

**Pros of saving files directly in MongoDB**

*   [ACID](https://www.tutorialspoint.com/dbms/dbms_transaction.htm) consistency which includes a rollback of an update that is complicated when the files are stored outside the database.
*   Files will be in *sync* with the database so cannot be orphaned from it which gives you an upper hand in tracking transactions.
*   Backups automatically include file binaries.
*   More *Secure* than saving in a File System.

**Cons of saving files directly in MongoDB**

*   You may have to *convert* the files *to* *blob* in order to store it in db.
*   Database *Backups* will become more *hefty* and *heavy*.
*   *Memory ineffective*. To add more, often RDBMS’s are RAM driven. So all data has to go to RAM first.

* * *

**How MongoDB stores large files**

> One word, **GridFS**.

MongoDB stores all documents as **BSON,** which is just a binary encoding of the good old JSON format.

The maximum BSON document size in MongoDB is **16 MB.** Which is nothing when we want to store large files like videos and songs. They might easily exceed the limit. [GridFS](https://docs.mongodb.com/manual/reference/glossary/#term-gridfs) is a specification for storing and retrieving files that exceed the BSON document size limit of 16 MB.

![](/images/Large-Document-Storage-in-MongoDB/1*6UMoh-zZ4R1AFXMSVYqQ0g.jpeg)

<figcaption>The idea behind&nbsp;GridFS</figcaption>

Instead of storing a file in a single document, GridFS divides the file into parts, or chunks, and stores each chunk as a separate document.

By default, GridFS uses a default chunk size of 255 kB; that is, GridFS divides a file into chunks of 255 kB with the exception of the last chunk. The last chunk is only as large as necessary.

GridFS uses two collections to store files. One collection stores the file chunks, and the other stores file metadata.

*   `fs.chunks`: Used to store the file data itself. In binary format.
*   `fs.files`: Stores file metadata.

<figcaption>See the whole gist <a href="https://gist.github.com/L04DB4L4NC3R/4cc82310fc6c39aa0cc9654bf6d41fe4" data-href="https://gist.github.com/L04DB4L4NC3R/4cc82310fc6c39aa0cc9654bf6d41fe4" class="markup--anchor markup--figure-anchor" rel="noopener" target="_blank">here</a></figcaption>

![](/images/Large-Document-Storage-in-MongoDB/1*8KA8NSuDVWX6fzAAytB_kA.png)

<figcaption>fs.files collection</figcaption>

When you query GridFS for a file, the driver will reassemble the chunks as needed. You can perform range queries on files stored through GridFS. You can also access information from arbitrary sections of files, such as to “skip” to the middle of a video or audio file.

Here is an example code of what retrieving files from GridFS looks like:

<figcaption>See the whole code <a href="https://github.com/L04DB4L4NC3R/gridfs-retrieve/blob/master/retrieve.py" data-href="https://github.com/L04DB4L4NC3R/gridfs-retrieve/blob/master/retrieve.py" class="markup--anchor markup--figure-anchor" rel="noopener" target="_blank">here</a></figcaption>

This program fetches the path to the `fs.files.bson` dump, gets the file IDs. Then performs a fetch call to GridFS for re-assembling and serving all of the files back to us.

We then take the data received and write it to a file in our local filesystem (in a folder called *files)*. Replace YOUR\_DB\_URI with the URI of your MongoDB instance to see this in action.

* * *

**Pros of GridFS**

*   GridFS can store as many files as needed.
*   It can be used to recall sections of files without reading the entire file into memory.
*   It can be used to keep your files and metadata automatically synced and deployed across a number of systems and facilities.
*   It can be indexed and sharded. Drivers that support the GridFS specification automatically create indexes for it.

**Cons of GridFS**

*   It does not support multi-document transactions.
*   It is not ideal for a system where you need to update the content of the entire file atomically. In this, it is cheaper to store multiple versions of the file.
*   If the files are smaller than 16 MB, it is a lot cheaper to store them using the BinData data type in MongoDB.

* * *

**Conclusion**

MongoDB has a great way of handling files that are above the specified document limit. GridFS, though not perfect, is still great for use cases where you want to keep your files and metadata consistent.

A typical use case of GridFS might be when using [geographically distributed replica sets](https://docs.mongodb.com/manual/core/replica-set-architecture-geographically-distributed/#replica-set-geographical-distribution), MongoDB can distribute files and their metadata automatically to a number of **mongod** instances and facilities.

**References**

[**mongodb/specifications**  
*GridFS is a convention drivers use to store and retrieve BSON binary data (type "\\x05") that exceeds MongoDB's…*github.com](https://github.com/mongodb/specifications/blob/master/source/gridfs/gridfs-spec.rst "https://github.com/mongodb/specifications/blob/master/source/gridfs/gridfs-spec.rst")[](https://github.com/mongodb/specifications/blob/master/source/gridfs/gridfs-spec.rst)

[**L04DB4L4NC3R/gridfs-retrieve**  
*You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…*github.com](https://github.com/L04DB4L4NC3R/gridfs-retrieve "https://github.com/L04DB4L4NC3R/gridfs-retrieve")[](https://github.com/L04DB4L4NC3R/gridfs-retrieve)

[**GridFS - MongoDB Manual**  
*is a specification for storing and retrieving files that exceed the -document of 16 MB. Instead of storing a file in a…*docs.mongodb.com](https://docs.mongodb.com/manual/core/gridfs/ "https://docs.mongodb.com/manual/core/gridfs/")[](https://docs.mongodb.com/manual/core/gridfs/)

[**Which is Better ? Saving Files in Database or in File System | Habile**  
*If you are indecisive in choosing the best way to save a file uploaded to your server, Then cheers mate because you are…*habiletechnologies.com](https://habiletechnologies.com/blog/better-saving-files-database-file-system/ "https://habiletechnologies.com/blog/better-saving-files-database-file-system/")[](https://habiletechnologies.com/blog/better-saving-files-database-file-system/)

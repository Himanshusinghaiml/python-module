Why are ACID transactions a good thing to have?
ACID transactions ensure the highest possible data reliability and integrity. They ensure that your data never falls into an inconsistent state because of an operation that only partially completes. 
For example, without ACID transactions, if you were writing some data to a database table, but the power went out unexpectedly, it's possible that only some of your data would have been saved, while some of it would not.
Now your database is in an inconsistent state that is very difficult and time-consuming to recover from.

https://www.databricks.com/glossary/acid-transactions

Delta Lake: Reliable, consistent data with the guarantees of ACID transactions

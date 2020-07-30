# elib
## Reusable Ideas
A simple summary notes and ideas in problems that I encountered during daily work, and reusability possibilities. Following:

### #20200730-01: password and connection string dilemma in pyspark scripts
It is a lot of times very difficult to balance the security requirements and dev progress. One example is when a project has strict security requirements due to compliance and other reasons, it is necessary to secure all the data sources by encryption of the password or database connection string, before they can be passed and used in programs. For PySpark and other Spark programs specifically, there doesn't seem to be a lot of options to secure all these credentials, maybe we can build a lib out of it to make it work securely with one command?

Some existing discussions on how to tackle these security problems in passing conn strings or passwords to pyspark:

[How to protect password and username in Spark (such as for JDBC connections/accessing RDBMS databases)?](https://stackoverflow.com/questions/54377938/secured-connection-to-data-sources-in-pyspark)
[Secured connection to Data sources in Pyspark](https://stackoverflow.com/questions/54377938/secured-connection-to-data-sources-in-pyspark)

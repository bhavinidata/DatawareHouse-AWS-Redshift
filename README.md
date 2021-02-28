# Datawarehouse - AWS Redshift

## Objective
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. This solution enables music stores to easily process loads of information efficiently.

## Project Summary
An implementation of a Data Warehouse leveraging AWS RedShift. This project builds an ETL pipeline for the database hosted on AWS Redshift that extracts their data from multiple S3 buckets, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

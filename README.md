Scripts for Insight Data Engineering coding challenge

This GitHub repository contains my solution to the coding challenge for the Fellows Program organized by Insight Data Science.


## Input
Below are the contents of an example `complaints.csv` file: 
```
Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
```

## Output
The lines in the output file should be sorted by product (alphabetically) and year (ascending)

Given the above `complaints.csv` input file, we'd expect an output file, `report.csv`, in the following format
```
"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100
```
Notice that because `debt collection` was only listed for 2019 and not 2020, the output file only has a single entry for debt collection. Also, notice that when a product has a comma (`,`) in the name, the name should be enclosed by double quotation marks (`"`). Finally, notice that percentages are listed as numbers and do not have `%` in them.

## Repo directory structure
The top-level directory structure for your repo should look like the following: (So that we can grade your submission, replicate this directory structure at the top-most level of your project repository. Do not place the structure in a subdirectory)

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── complaints.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── complaints.csv
                |── output
                    └── report.csv
                    
## Instructions
To execute the script move to the main directory of the project and run the following in the terminal:

```
python ./src/consumer_complaints.py ./input/complaints.csv ./output/report.csv
```

Last two arguments should be input and output files, respectively.

Alternatively, you can execute `./run.sh` script to run the codes for a sample file and perform a unit test.

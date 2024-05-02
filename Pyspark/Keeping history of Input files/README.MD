# Historizing files transfered by SFTP
## Task: 
##### Create dataset from the incoming files from the SFTP server. The file will be ingested daily at 4am UTC. File overwrites daily so we also need to keep history of the files in case we need to reference back to them.

## Steps to take:

- **Creating code that keeps history of the tables**: [Click here to see the code!](https://github.com/Kovaczso/Python/blob/main/Pyspark/Keeping%20history%20of%20Input%20files/History.py)
- **Choosing the latest file from the history**: [Click here to see the code!](https://github.com/Kovaczso/Python/blob/main/Pyspark/Keeping%20history%20of%20Input%20files/Latest_file.py)
- **Creating dataset from the latest file**: [Click here to see the code!](https://github.com/Kovaczso/Python/blob/main/Pyspark/Keeping%20history%20of%20Input%20files/Final_dataset.py)

#### **Note:** Codes are written and used on Palantir-Foundry

# ![diagram](diagram.jpge)

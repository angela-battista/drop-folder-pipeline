# Drop-Folder Pipeline – Roadmap
A python script watches a drop folder. When a CSV file lands there, the script checks it, sorts it into processed or rejected folders, loads completed files into a SQLite database, and writes a log line for all steps. 

# E-commerce Data Integrity Investigation
An investigation of a four-table synthetic e-commerce dataset (customers, orders, order items, returns) for data quality and integrity problems. The same investigation is done twice, once in **SQL Server (T-SQL)** and once in **Python (pandas)**, so the two approaches can be compared.

## Seven Stages (1-4 are complete and the remaining are in process)


| 1 | Set up the project. | Create the folders (drop, processed, rejected, logs, and sample_data). Open in VS code, start Git, make first commit and push to GitHub. |
| 2 | Extract | Write a script that finds the CSV files in drop folder and reads each one into pandas. |
| 3 | Validate | Check for nulls, duplicates and types. If a file fails, it is moved to a rejected folder with a status |
| 4 | Transform | Clean the passing files: standardize dates and text, fix a known casing issue. |
| 5 | Load |
| 6 | Log and archive |


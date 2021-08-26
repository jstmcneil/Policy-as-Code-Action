### Bash Scripts
There are two bash scripts used in this project.

**run-cfn-binary.sh**: Recursively searches the provided _CFM REPO_ for CloudFormation files to scan. It then scans those files and pipes their output to a named file into a /results/ directory.

**env-var-condition.sh**: Natively, the _cfn-guard_ binary does not produce stdout when no rule violations are found. This script evaluates if any output was produced for any of the scanned CloudFormation files, and then sets an enviroment variable in order to conditionally run one of the two python scripts.

**cfn-guard-data-wrangle.sh**: This was added so that any subsequent updates to the CFN-Guard command scheme could be addressed. This file isolates the actual calling of the binary in order for changes to be made quickly.

### Python Scripts
There are three python scripts used in this project.

**python-checkforcfn.py**: Uses tags to decide if a given file is a CloudFormation template. If it is, CFN-Guard will be run against it.

**failed-check-teams.py**: If any _cfn-guard_ rule-checks failed for any CloudFormation file, then this script will run. This script will send one Teams message for each CloudFormation file in the repository. If no violations were found for a given file, then affirmative message will be sent. If violations were found for a given file, a failing message with the specific failed policy, resource, and value will be sent. Finally, a digest report is sent to Teams describing a summary of the run. 

**passed-check-teams.py**: If all _cfn-guard_ rule-checks passed for all CloudFormation files, then this script will run. It will send a single affirmative Teams message stating that all files passed all checks. 

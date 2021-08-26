#!/bin/bash
cfn-guard validate -r $1 -d $2 --show-summary none  --type CFNTemplate -o single-line-summary | sed '/^Rule/d' | sed '/^--/d' | sed '/^Evaluation of rules/d'

import textfsm
import sys
import re
import os.path
from os import path

# Load the input file to a variable
input_file = open(sys.argv[1], encoding='utf-8')
raw_text_data = input_file.read()
input_file.close()

# Run the text through the FSM. 
# The argument 'template' is a file handle and 'raw_text_data' is a 
# string with the content from the show_inventory.txt file
template = open("intf_couters.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

for item in fsm_results:
   if item[0] == "reth0.3400":
        print (*item)

 
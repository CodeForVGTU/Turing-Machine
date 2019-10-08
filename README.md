# Turing-Machine
<u>Turing Machine Simulator created with Python</u>

Python version: Python 3.6.8
<i>Program is easily usable in CMD/Terminal.</i>

A Turing machine is a mathematical model of computation that definegs an abstract machine, which manipulates symbols on a strip of tape according to a table of rules.
THere are 5 commands: {current_state}{current_symbol}{next_symbol}{moving_position}{next_state}

# To set up program on Linux:
## Open terminal and enter commands:
  "python3 --version" - check python 3 version<br/>
  "sudo apt install python3-pip" - package required for installing modules<br/>
  "pip3 install console-menu"<br/>
  "pip3 install futures"<br/>
  "pip3 install keyboard"<br/>
  "pip3 install colorama"<br/>
  
  to open program go to file directory via terminal and execute file by typing:
    "sudo python3 TM.py" - sudo is required for keyboard module

  At this state file should work.
  Basically there are 4 different .txt files which contains data for TM simulator.
  .txt files structure:<br/>
    1 line - head position<br/>
    2 line - tape<br/>
    all the left lines - code for turing machine.

# Algorithm:
So our main task is to change tape by executing Turing code.
Simply open app and on menu select first option (by typing 1 and clicking enter).
Then enter file names (together with type). After you finish enter "Q".
Now turing machine will work until it stops automatically (halts) or until you stop it.

Application is working by using {current_state} & {current_state} as a key in dictionary.
By doing this we are getting our needed values - {next_symbol}{moving_position}{next_state}

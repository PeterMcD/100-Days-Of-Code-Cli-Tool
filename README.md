# 100 Days Of Code Cli Tool

### Description

This tool was my first project as part of the 100 Days Of Code challenge.

The script helps create your journal and keep it upto date as you go along. 

### Usage

The tool is a simple cli tool. Firstly you should install the package:

```bash
pip install git+https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool.git
```

Once downloaded:

To start the challenge;

```bash
// To start the challenge
doc --start

// To log days activity
doc -newday

// To display details of a given day
doc -display 1

// Restart challenge
doc --restart

// Deletes all files associated with a given day
doc --delete

// Getting help
doc --help
```

Additional arguments

```bash
// Specifies the path you would like the log to be located. Is only set when starting.
--path string
```

To maintain state (i.e. so the script knows where the project is) a file is created in ~. This currently contains the
path specified when creating the challenge. If none is specified this will be ~/Documents.

Although this has only been tested on Linux (specifically Ubuntu), this should also work on Windows.

### ToDo

1) Improve the tool to upload the log to the users own Github repository.
2) Enable choice in which log to use.
3) Better handling of errors (for example if a git commit fails).
4) Update so that DaysOfCode reflects structure of log

### Known Issues

1) --edit not currently implemented.
2) Some git files result in permissions issues when deleting
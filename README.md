# 100 Days Of Code Cli Tool

### Description

This tool was my first project as part of the 100 Days Of Code challenge.

The script

### Usage

The tool is a simple cli tool. Firstly you should clone this repository:

```bash
git clone https://github.com/PeterMcD/100-Days-Of-Code-Cli-Tool
cd 100-Days-Of-Code-Cli-Tool
```

Once downloaded:

To start the challenge;

```bash
// To start the challenge
python3 main.py --start

// To log days activity
python3 main.py -newday

// Restart challenge
python3 main.py --restart

// Getting help
python3 main.py --help
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
4) Test functionality on Windows.
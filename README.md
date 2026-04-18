# FPGA Alliance Scripts
----
[![Python CI](https://github.com/sikienzl/FPGA_Alliance_Scripts/actions/workflows/python-ci.yml/badge.svg)](https://github.com/sikienzl/FPGA_Alliance_Scripts/actions/workflows/python-ci.yml)

This repository contains helper scripts for a simple synthesis flow based on the Alliance toolchain.

## Contents

- `wrapper_synthese/synthese_ghdl.py`: Wrapper for the Alliance commands `vasy`, `boom`, `boog`, `loon`, and the chained command `all`.
- `wrapper_synthese/cleanup.py`: Removes generated artifacts (`.vbe`, `.vst`, `.xsc`) in the current directory.
- `wrapper_synthese/set_env.sh`: Adds the current directory to `PATH` (if `synthese_ghdl.py` is located there).
- `wrapper_synthese/StringBuilder.py`: Internal helper class used to build command strings.

## Requirements

- Linux/Unix shell (scripts are written for Bash/Python)
- Python 3
- Installed Alliance toolchain with available commands:
  - `vasy`
  - `boom`
  - `boog`
  - `loon`

Note: The project assumes the Alliance environment is already configured correctly.

## Quick Start

1. Change into the script directory:

```bash
cd wrapper_synthese
```

2. Optionally extend `PATH` for the current shell:

```bash
source set_env.sh
```

3. Run individual steps or the full flow:

```bash
python3 synthese_ghdl.py vasy -i design.vhdl -a vbe -p
python3 synthese_ghdl.py boom -i design_vasy
python3 synthese_ghdl.py boog -i design_boom
python3 synthese_ghdl.py loon -i design_boog -x 1
python3 synthese_ghdl.py all -i design
```

## Usage: synthese_ghdl.py

General help:

```bash
python3 synthese_ghdl.py --help
```

Help for a subcommand:

```bash
python3 synthese_ghdl.py <command> --help
```

Available commands:

- `vasy`
  - Important parser arguments:
    - `-i <file>` Input (VHDL)
    - `-a <value>` Alliance output format (internally handled by presence)
    - `-p` Power ports
    - `-o` Override output file (internally a switch)
    - `-C <value>` Carry-lookahead parameter
- `boom`
  - `-i <file>`, optional `-l <0..3>`, `-d <0..100>`, `-o <file>`
- `boog`
  - `-i <file>`, optional `-m <0..4>`, `-o <file>`
- `loon`
  - `-i <file>`, optional `-m <0..4>`, `-x <0|1>`, `-o <file>`
- `all`
  - `-i <base-name>`
  - Runs in sequence:
    - `vasy -a -p <i> <i>_vasy`
    - `boom <i>_vasy <i>_boom`
    - `boog <i>_boom <i>_boog`
    - `loon -x 1 <i>_boog <i>_final`

## Output Filenames (Automatic)

If no explicit output is set, the wrapper generates these suffixes:

- `vasy`: `<input>_vasy`
- `boom`: `<input>_boom` (or replace `_vasy` with `_boom`)
- `boog`: `<input>_boog` (or replace `_boom` with `_boog`)
- `loon`: `<input>_final` (or replace `_boog` with `_final`)

## Usage: cleanup.py

Help:

```bash
python3 cleanup.py --help
```

Delete interactively:

```bash
python3 cleanup.py
```

Delete directly without prompts:

```bash
python3 cleanup.py --force
```

The script deletes all files with the extensions `.vbe`, `.vst`, and `.xsc` in the current directory.
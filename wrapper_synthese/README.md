# Usage

## set_env.sh

To set the path of `synthese_ghdl.py` on
the PATH-Variable, you can do the following:
`$ source set_env.sh`

## synthese_ghdl.py
The wrapper script allows you to execute
the commands `vasy`, `boom`, `boog`, `loon` and `all`.
To see which parameters are possible type 
`synthese_ghdl.py <command> --help`.
Here are an example for vasy:
```bash
$ synthese_ghdl.py vasy --help
usage: synthese_ghdl.py vasy [-h] [-i I] [-a A] [-p] [-o] [-C C]

optional arguments:
  -h, --help  show this help message and exit
  -i I        input-file in .vhdl-format
  -a A        output in alliance-format (.vbe)
  -p          ports for power
  -o          overrides output-file
  -C C        blocksize; produce carry-lookahead-adder
$
```

If you use the command `all` the four commands `vasy`, `boom`, `boog` and `loon` will be executed.
Here are the default parameters `-a` and `-p` used for `vasy` and `-x 1` for loon. 
On the other commands no default parameters are set. 

"""Simple Tool that lists native function available in the shared object on Linux"""
import argparse
from python.runfiles import runfiles
from pathlib import Path
from typing import List
import platform
import subprocess

def SharedLibPath(rlocation: str) -> Path:
    """
    Validate path to .so object

    Parameters:
    rlocation: file path (or runfile path passed through Bazel $(rlocations))
    Returns:
    Path: absolute path to the .so file
    """
    if not rlocation.endswith(".so"):
        raise ValueError(f"Invalid file: {rlocation} is not a .so file") 
    absolute = Path(rlocation)
    if absolute.exists():
        return absolute.resolve(strict = True)
    _RUNFILES = runfiles.Create()
    return Path(_RUNFILES.Rlocation(rlocation)).resolve(strict = True)

def get_native_functions(lib: Path) -> List[str]:
    """
    Core Tool function to get the list of native functions available in shared object:
    - list all native (standard) C functions available on the machine (taken from /lib/<machine>-linux-gnu/libc.so.6)
    - objdump .so library to list all available functions
    - output matches of these lists as a result

    Parameters:
    Path: .so file path
    Returns:
    List[str]: list of C native functions available in shared object
    """
    result = []
    native_functions = []
    shared_lib_functions = []
    try:
        # list all native functions symbols and versions as bash command
        cmd = f"readelf -Ws /lib/{platform.uname().machine}-linux-gnu/libc.so.6 | grep FUNC"
        output = subprocess.check_output(cmd, shell=True, text=True).strip().split("\n")
        for line in output:
            function = line.split()[7]
            function = [x for x in function.split("@") if x]
            native_functions.append((function[0], f"({function[1]})"))
    except Exception:
        raise RuntimeError("Cannot retrieve native libc functions.")

    try:  
        # list all .so available functions symbols and versions as bash command
        cmd = f"objdump -TC {lib} | grep DF | grep GLIBC"
        output = subprocess.check_output(cmd, shell=True, text=True).strip().split("\n")
        for line in output:
            func = line.split()
            func_symbol = func[-1]
            func_symbol_version = func[-2]
            # filter out internal functions
            if not func_symbol.startswith("__"):
                shared_lib_functions.append((func_symbol, func_symbol_version))
    except Exception:
        raise RuntimeError("Cannot retrieve shared library object functions.")

    # if function from .so is native - add to result
    for func in shared_lib_functions:
        if func in native_functions:
            result.append(func[0])
    # sort resulted list fot the easier tests and further usage of this data
    result.sort()
    return result

def main():
    # Define command line interface for the tool
    parser = argparse.ArgumentParser(description = "Tool to get native functions used in shared library object")
    parser.add_argument("--lib", type=SharedLibPath, required = True, help = "shared library .so file.")
    args = parser.parse_args()
    print(get_native_functions(args.lib))

if __name__ == "__main__":
    main()

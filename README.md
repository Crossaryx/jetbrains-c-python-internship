# JetBrains C-Python coding challenge

**Task**  
Implement a simple Python tool that lists native function available in the shared object on Linux.  
It should work with .so files on Linux.  
There should be unittests verifying that tool output is correct.  

> [!IMPORTANT]
> Since task does not specify whether we need to consider internal compiler functions as
> available native functions (like __libc_start_main),
> in the implementation only public native functions are considered (printf, atoi, etc.).

**Overview**  

For reproducibility and compatability reasons Docker VS Code devcontainer with Ubuntu 24.04 and minimum set of tooling (git, gcc, python) was used.  
Bazel is used as a build system.  
Therefore no specific compiler setup was required, Bazel picks default system one (GCC 13.3.0).
*rules_cc* usage simplifies shared library object generation.
*rules_python* usage simplifies python binary and script execution.

**Design**

- used Bazel macro *cc_shared_library* to generate .so shared object to be able to test and debug the tool
- created [demo/example functions and libraries](./shared_libs/)
- [Tool implementation](./tool/tool.py)
- [Tests](./tool/tests/) - used generic test script that calls Tool on given .so shared object and validates result based on given expected functions, both .so and expected functions are passed as arguments through cc_tests targets

**Development environment**  

Prerequisites:  
- Docker Desktop
- VS Code + Dev Containers extension

To use repository in container:  
- Open VS Code (with DevContainers extension installed)
- Ctrl (or Cmd) + Shift + P and type "Clone Repository into container volume..."
- paste https://github.com/Crossaryx/jetbrains-c-python-internship.git

**Build, Run, Test**  

Build and test all:
```
bazel test ...
```

Run Tool --help:
```
bazel run tool -- --help
```

Run Tool (on "time" libary by default):
```
bazel run tool
```

Run Tool on another demo libary:
```
bazel run tool --  --lib <absolute path to .so>
```

Run Tool with memory library (or another library from [BUILD](./shared_libs/BUILD))
```
bazel build //shared_libs:memory
bazel run tool -- --lib $(pwd)/bazel-bin/shared_libs/memory.so
```

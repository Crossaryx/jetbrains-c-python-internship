py_test(
    name = "string",
    srcs = ["tests.py"],
    main = "tests.py",
    args = [
        "--lib", "$(rlocationpath //shared_libs:string)", 
        "--expected_functions", "printf,strcat,strcpy",
    ],
    data = ["//shared_libs:string"],
    deps = ["//tool:lib"]
)

py_test(
    name = "file",
    srcs = ["tests.py"],
    main = "tests.py",
    args = [
        "--lib", "$(rlocationpath //shared_libs:file)", 
        "--expected_functions", "fopen,fprintf,fclose,printf",
    ],
    data = ["//shared_libs:file"],
    deps = ["//tool:lib"]
)

py_test(
    name = "memory",
    srcs = ["tests.py"],
    main = "tests.py",
    args = [
        "--lib", "$(rlocationpath //shared_libs:memory)", 
        "--expected_functions", "malloc,free,atoi,printf",
    ],
    data = ["//shared_libs:memory"],
    deps = ["//tool:lib"]
)

py_test(
    name = "time",
    srcs = ["tests.py"],
    main = "tests.py",
    args = [
        "--lib", "$(rlocationpath //shared_libs:time)", 
        # Time shared library uses string library, so it should include 
        # native functions used there as well (not only time)
        "--expected_functions", "time,printf,strcat,strcpy",
    ],
    data = ["//shared_libs:time"],
    deps = ["//tool:lib"]
)

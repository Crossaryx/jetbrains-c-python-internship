package(default_visibility = ["//visibility:public"])

py_library(
    name = "lib",
    srcs = ["tool.py"],
    deps = ["@rules_python//python/runfiles"]
)

# use this library as deafult input for tool for demo purposes
shared_obj = "//shared_libs:time"
py_binary(
    name = "tool",
    srcs = ["lib"],
    args = ["--lib", "$(rlocationpath {})".format(shared_obj)],
    data = [shared_obj],
)

load("@rules_cc//cc:cc_library.bzl", "cc_library")
load("@rules_cc//cc:cc_shared_library.bzl", __cc_shared_library = "cc_shared_library")

def cc_shared_library(name, visibility = ["//visibility:public"],  **kwargs):
    "Provide shared library"
    copts = kwargs.pop("copts", [])
    cc_library(
        name = name + "_lib",
        # emit calls to builtin functions so they are visible in objdump of .so
        copts = ["-fno-builtin"] + copts,
        visibility = visibility, 
        **kwargs,
    )
    # generate .so shared object
    __cc_shared_library(
        name = name,
        shared_lib_name = name + ".so",
        deps = [name + "_lib"],
        visibility = visibility,
    )

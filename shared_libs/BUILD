load("//:defs.bzl", "cc_shared_library")

cc_shared_library(
    name = "file",
    srcs = ["file.c"],
)

cc_shared_library(
    name = "memory",
    srcs = ["memory.c"],
)

cc_shared_library(
    name = "string",
    hdrs = ["string.h"],
    srcs = ["string.c"],
)

cc_shared_library(
    name = "time",
    srcs = ["time.c"],
    deps = ["string_lib"],
)

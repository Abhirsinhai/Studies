const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdout();
    try stdout.print("Hello, {s}!\n", .{"world"});
}
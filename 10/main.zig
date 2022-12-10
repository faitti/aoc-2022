const std = @import("std");
const fs = std.fs;

pub fn part_1(file_name: []const u8) !void {
    var file: fs.File = try fs.cwd().openFile(file_name, .{});
    defer file.close();

    var file_buffer = std.io.bufferedReader(file.reader());
    var input_stream = file_buffer.reader();
    var buffer: [2048]u8 = undefined;

    var register: i32 = 1;
    var op_count: i32 = 1;
    var sum: i32 = 0;

    while (try input_stream.readUntilDelimiterOrEof(&buffer, '\n')) |line| {
        if (std.mem.eql(u8, line, "noop")) {
            op_count += 1;
            if (@mod(op_count - 20, 40) == 0) {
                sum += op_count * register;
            }
        } else {
            var value: i32 = try std.fmt.parseInt(i32, line[5..line.len], 10);
            op_count += 1;
            if (@mod(op_count - 20, 40) == 0) {
                sum += op_count * register;
            }
            register += value;
            op_count += 1;
            if (@mod(op_count - 20, 40) == 0) {
                sum += op_count * register;
            }
        }
    }

    std.debug.print("Part 1: {d}\n", .{sum});
}

pub fn crt(op_count: i32, register: i32) !void {
    if (try std.math.absInt(register - @mod(op_count - 1, 40)) <= 1) {
        std.debug.print("#", .{});
    } else {
        std.debug.print(" ", .{});
    }

    if (@mod(op_count, 40) == 0) {
        std.debug.print("\n", .{});
    }
}

pub fn part_2(file_name: []const u8) !void {
    var file: fs.File = try fs.cwd().openFile(file_name, .{});
    defer file.close();

    var file_buffer = std.io.bufferedReader(file.reader());
    var input_stream = file_buffer.reader();
    var buffer: [2048]u8 = undefined;

    var op_count: i32 = 1;
    var register: i32 = 1;

    std.debug.print("Part 2: \n", .{});

    while (try input_stream.readUntilDelimiterOrEof(&buffer, '\n')) |line| {
        if (std.mem.eql(u8, line, "noop")) {
            try crt(op_count, register);
            op_count += 1;
        } else {
            var value: i32 = try std.fmt.parseInt(i32, line[5..line.len], 10);
            try crt(op_count, register);
            op_count += 1;
            try crt(op_count, register);
            register += value;
            op_count += 1;
        }
    }
}

pub fn main() !void {
    try part_1("input");
    try part_2("input");
}
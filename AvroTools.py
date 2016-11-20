# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

import os
import subprocess


"""
Avro package for Sublime Text
"""


COMMAND_NOT_FOUND_MSG = """
* Please make sure 'avro-tools' is executable and is on your PATH
* In linux you can create file in /usr/local/bin/avro-tools with following content:
#!/bin/bash
java -jar /usr/local/bin/avro-tools-1.7.7.jar "$@"%

* /usr/local/bin/avro-tools-1.7.7.jar can downloaded from http://central.maven.org/maven2/org/apache/avro/avro-tools/1.7.4/avro-tools-1.7.4.jar
and then add exec permissions with "chmod u+x /usr/local/bin/avro-tools-1.7.7.jar"

* Verify that it works with opening new terminal and submitting avro-tools
"""
COMMAND_LINE = "avro-tools tojson {0}"


def run_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


class AvroCommand(sublime_plugin.TextCommand):
    def run(self, edit, filename=None):
        if filename is None or not filename.endswith('.avro'):
            return

        pos = 0
        command = COMMAND_LINE.format(filename).split()

        try:
            for line in run_command(command):
                pos += self.view.insert(edit, pos, line.rstrip().decode("utf-8") + "\n")
        except FileNotFoundError as e:
            pos += self.view.insert(edit, pos, str(e)+COMMAND_NOT_FOUND_MSG)

        self.view.set_name(os.path.basename(filename))
        self.view.set_read_only(True)


class OpenAvroFile(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name()
        if filename.endswith('.avro'):
            sublime.status_message("opening avro file: " + filename)
            print("opening avro file: " + filename)
            avro_view = view.window().new_file()
            view.close()
            avro_view.run_command('avro', {'filename': filename})

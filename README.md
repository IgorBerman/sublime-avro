# sublime-avro
Reads Apache Avro files in Sublime Text. The records are shown in JSON format, one JSON object per line. Avro files are opened in read-only mode. Tested with Sublime 3.

# Based on https://github.com/yuj/sublime-parquet

# Requirement
This sublime package depends on the [avro-tools jar](http://central.maven.org/maven2/org/apache/avro/avro-tools/1.7.4/avro-tools-1.7.4.jar):
* In linux you can create file in /usr/local/bin/avro-tools with following content:
```
#!/bin/bash
java -jar /usr/local/bin/avro-tools-1.7.7.jar "$@"
```
* /usr/local/bin/avro-tools-1.7.7.jar can be downloaded from http://central.maven.org/maven2/org/apache/avro/avro-tools/1.7.4/avro-tools-1.7.4.jar
and then add exec permissions with "chmod u+x /usr/local/bin/avro-tools"
* Verify that it works with opening new terminal and submitting 'avro-tools'

# Plugin installation
via Package Control

* Make sure you have Package Control installed.
* Open the Command Palette (command-shift-P on macOS; ctrl-shift-P on Ubuntu) and choose Install Package.
* Choose Avro-reader from the list.

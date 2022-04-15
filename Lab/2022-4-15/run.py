#!/usr/bin/env python

import os

os.system(' javac -d . -classpath ".:/mnt/d/Repository/infuq-others/Lab/lib/*" DirectMemory.java ')

os.system(' java -classpath ".:/mnt/d/Repository/infuq-others/Lab/lib/*" -Xms50M -Xmx50M -XX:MaxDirectMemorySize=132M -XX:MetaspaceSize=12M -XX:MaxMetaspaceSize=16M -XX:-UseCompressedClassPointers -XX:-UseCompressedOops  -XX:NativeMemoryTracking=detail com.infuq.memory.DirectMemory ')

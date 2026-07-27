import jpype
from pathlib import Path


def start_jvm():
    if jpype.isJVMStarted():
        return

    jars = [
        str(jar)
        for jar in Path(__file__).parent.parent.joinpath("lib").glob("*.jar")
    ]

    jpype.startJVM(classpath=jars)
import jpype
from pathlib import Path

JAVA_DIRECTORY = Path(__file__).parent / "java"

def start_jvm():
    if jpype.isJVMStarted():
        return

    jars = [str(jar) for jar in JAVA_DIRECTORY.glob("*.jar")]

    if not jars:
        raise RuntimeError(f"No Java libraries found in {JAVA_DIRECTORY}")

    jpype.startJVM(classpath=jars)
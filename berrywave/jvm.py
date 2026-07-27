import jpype
from pathlib import Path

JAVA_RUNTIME = Path(__file__).parent / "runtime" / "java"

def start_jvm():
    if jpype.isJVMStarted():
        return

    jars = [str(jar) for jar in JAVA_RUNTIME.glob("*.jar")]

    if not jars:
        raise RuntimeError(f"No Java libraries found in {JAVA_RUNTIME}")

    jpype.startJVM(classpath=jars)
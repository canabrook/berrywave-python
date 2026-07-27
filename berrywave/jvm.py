import jpype
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LIB_DIRECTORY = PROJECT_ROOT / "lib"

def start_jvm():
    if jpype.isJVMStarted():
        return

    jars = [str(jar) for jar in LIB_DIRECTORY.glob("*.jar")]

    jpype.startJVM(classpath=jars)
import jpype
from pathlib import Path

from berrywave.exceptions import BerryWaveError

JAVA_RUNTIME = Path(__file__).parent / "runtime" / "java"


def start_jvm():
    if jpype.isJVMStarted():
        return

    jars = [str(jar) for jar in JAVA_RUNTIME.glob("*.jar")]

    if not jars:
        raise RuntimeError(f"No Java libraries found in {JAVA_RUNTIME}")

    verify_java_available()
    jpype.startJVM(classpath=jars)


def verify_java_available():
    try:
        jpype.getDefaultJVMPath()
    except Exception as e:
        raise BerryWaveError(
            "Java runtime not found. "
            "BerryWave EDI requires Java 17 or later."
        ) from e

"""news-image-20261120 entry (Python 3.13, standard library only).

Copies the pre-rendered infographic entry.png beside this file to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic:
the same bytes are written on every run.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

# sha256 of the rendered entry.png (verified 20 Nov 2026, two runs
# byte-identical). The copy must match it, or the image is corrupt.
EXPECTED_SHA256 = "32feac99f4bc8714bdb848bbe37d35beb3cf1831bc37f5c7f3d4282bc3c42af7"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
# The gate requires both runs to write the same bytes; a copy of a fixed
# file is byte-identical by construction. Confirm the write landed and
# that the destination is the expected 1024x1024 PNG (99,134 bytes).
assert os.path.getsize(DST) == os.path.getsize(SRC) == 99134
with open(DST, "rb") as f:
    assert hashlib.sha256(f.read()).hexdigest() == EXPECTED_SHA256
print("wrote", DST, os.path.getsize(DST), "bytes")

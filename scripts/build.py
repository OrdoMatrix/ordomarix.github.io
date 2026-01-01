from pathlib import Path
from datetime import datetime
import json
import zipfile

# ---------- PUBLIC SITE OUTPUT (GitHub Pages) ----------
docs = Path("docs")
docs.mkdir(parents=True, exist_ok=True)

(docs / ".nojekyll").write_text("", encoding="utf-8")

(docs / "index.html").write_text(
    f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Ordomatrix</title>
</head>
<body>
  <h1>Ordomatrix</h1>
  <p>Last rebuilt: {datetime.utcnow().isoformat()}Z</p>
  <p><strong>Pro Pack:</strong> generated automatically as <code>pro/pro_pack.zip</code></p>
</body>
</html>
""",
    encoding="utf-8",
)

# ---------- PRO ARTIFACT OUTPUT (Paid) ----------
pro_dir = Path("pro")
pro_dir.mkdir(parents=True, exist_ok=True)

version = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

(pro_dir / "README.txt").write_text(
    f"Ordomatrix Pro Pack\nVersion: {version}\n",
    encoding="utf-8",
)

(pro_dir / "data.json").write_text(
    json.dumps(
        {"project": "Ordomatrix", "version": version, "generated": True},
        indent=2,
    ),
    encoding="utf-8",
)

zip_path = pro_dir / "pro_pack.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(pro_dir / "README.txt", arcname="README.txt")
    z.write(pro_dir / "data.json", arcname="data.json")

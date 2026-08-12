---
name: jupyter-notebook
description: ใช้เมื่อผู้ใช้ร้องขอให้สร้าง จัดโครงร่าง หรือแก้ไข Jupyter notebooks
  (`.ipynb`) สำหรับการทดลอง การสำรวจ หรือบทแนะนำ; ควรใช้เทมเพลตที่มาพร้อมและรันสคริปต์ช่วยเหลือ
  `new_notebook.py` เพื่อสร้างโน้ตบุ๊กเริ่มต้นที่สะอาด
---
# ทักษะ Jupyter Notebook

สร้างโน้ตบุ๊ก Jupyter ที่สะอาดและทำซ้ำได้สำหรับสองโหมดหลัก:

- การทดลองและการวิเคราะห์เชิงสำรวจ
- บทช่วยสอนและการแนะนำสำหรับการสอน

ให้ใช้เทมเพลตที่มาพร้อมและสคริปต์ช่วยเหลือเพื่อโครงสร้างที่สม่ำเสมอและลดความผิดพลาดของ JSON.

## เมื่อใดควรใช้
- สร้างโน้ตบุ๊ก `.ipynb` ใหม่จากศูนย์.
- แปลงบันทึกหรือสคริปต์ร่างให้เป็นโน้ตบุ๊กที่มีโครงสร้าง.
- รีแฟกเตอร์โน้ตบุ๊กที่มีอยู่ให้ทำซ้ำได้ง่ายขึ้นและอ่านผ่านได้ง่ายขึ้น.
- สร้างการทดลองหรือบทช่วยสอนที่ผู้อื่นจะอ่านหรือรันซ้ำได้.

## แผนผังการตัดสินใจ
- หากคำขอเป็นเชิงสำรวจ เชิงวิเคราะห์ หรือขับเคลื่อนด้วยสมมติฐาน ให้เลือก `experiment`.
- หากคำขอเป็นเชิงสอน ทีละขั้นตอน หรือระบุผู้ชม ให้เลือก `tutorial`.
- หากแก้ไขโน้ตบุ๊กที่มีอยู่ ให้ถือว่าเป็นการรีแฟกเตอร์: รักษาจุดประสงค์เดิมและปรับปรุงโครงสร้าง.

## เส้นทางทักษะ (ตั้งครั้งเดียว)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## เวิร์กโฟลว์
1. ยืนยันความตั้งใจ.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. สร้างโครงจากเทมเพลต.
Use the helper script to avoid hand-authoring raw notebook JSON.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. เติมโน้ตบุ๊กด้วยขั้นตอนขนาดเล็กที่รันได้.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
หลีกเลี่ยงผลลัพธ์ขนาดใหญ่ที่รกเมื่อสรุปสั้นๆ ก็เพียงพอ.

4. ใช้รูปแบบที่เหมาะสม.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. แก้ไขอย่างปลอดภัยเมื่อทำงานกับโน้ตบุ๊กที่มีอยู่.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. ตรวจสอบผลลัพธ์.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## เทมเพลตและสคริปต์ช่วยเหลือ
- เทมเพลตอยู่ใน `assets/experiment-template.ipynb` และ `assets/tutorial-template.ipynb`.
- สคริปต์ช่วยเหลือจะโหลดเทมเพลต อัปเดตเซลล์ชื่อเรื่อง และเขียนโน้ตบุ๊ก.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## แบบแผนสำหรับไฟล์ชั่วคราวและเอาต์พุต
- ใช้ `tmp/jupyter-notebook/` สำหรับไฟล์ชั่วคราว; ลบเมื่อเสร็จ.
- เขียนผลลัพธ์สุดท้ายภายใต้ `output/jupyter-notebook/` เมื่อทำงานในรีโปนี้.
- ใช้ชื่อไฟล์ที่คงที่และมีคำอธิบาย (ตัวอย่างเช่น `ablation-temperature.ipynb`).

## การพึ่งพา (ติดตั้งเฉพาะเมื่อจำเป็น)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## สภาพแวดล้อม
ไม่มีตัวแปรสภาพแวดล้อมที่จำเป็น.

## แผนที่อ้างอิง
- `references/experiment-patterns.md`: โครงสร้างการทดลองและหลักเกณฑ์เชิงประสบการณ์.
- `references/tutorial-patterns.md`: โครงสร้างบทช่วยสอนและลำดับการสอน.
- `references/notebook-structure.md`: รูปแบบ JSON ของโน้ตบุ๊กและกฎการแก้ไขอย่างปลอดภัย.
- `references/quality-checklist.md`: เช็คลิสต์การตรวจสอบขั้นสุดท้าย.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
คำปฏิเสธ:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลด้วยปัญญาประดิษฐ์ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะมุ่งมั่นให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ ฉบับต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งอ้างอิงหลัก สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
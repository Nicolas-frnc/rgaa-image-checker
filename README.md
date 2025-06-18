
# 🔍 RGAA image accessibility checker

## 🧭 Context

This script helps quickly audit web pages for accessibility (RGAA/WCAG) compliance.  
It highlights all `<img>` elements that are **hidden from assistive technologies** (using `aria-hidden="true"`) by adding a red border around them.

This makes it easier to:
- ✅ Verify that decorative images are properly hidden
- ❌ Detect important images that may be wrongly hidden

> 💡 You can reverse the logic to highlight *non-hidden* images instead by editing one line in the script.

---

## 🚀 How to use

### Prerequisites

- Python 3.x
- Selenium (`pip install selenium`)
- Google Chrome or Chrome Canary installed
- Update `chrome_options.binary_location` in the script with your Chrome path if needed

### Run the script

1. Edit the `urls` list in `highlight_hidden_images.py` to target your pages.
2. Run the script:

```bash
python highlight_hidden_images.py
```

3. For each URL:
   - A browser tab opens
   - Images with `aria-hidden="true"` are outlined in red
   - The number of hidden images is printed in the terminal
   - Press Enter to close when finished

---

## 🛠️ Optional: Reverse the highlighting

To highlight images that are *not* hidden modify this line in the script:

```javascript
if (img.getAttribute('aria-hidden') === 'true')
```

to:

```javascript
if (img.getAttribute('aria-hidden') === 'false' || img.getAttribute('aria-hidden') === null) {
```

---

## Result
![image](https://github.com/user-attachments/assets/3fc8386d-ef21-433e-9fa9-86d1193c7898)

---


## 📄 License

MIT License – see [LICENSE](./LICENSE) for details.


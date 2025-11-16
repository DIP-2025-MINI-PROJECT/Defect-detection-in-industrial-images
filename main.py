import cv2
import numpy as np
import os
from pathlib import Path

# paths (change if needed)
INPUT_FOLDER = r"C:\Users\Admin\Desktop\image-pro-final\images"
OUTPUT_FOLDER = r"C:\Users\Admin\Desktop\image-pro-final\output" 


# make output dir if not there
Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

# some params (tweak if results bad)
WIN_SIZE = 21
THRESH = 20
MIN_AREA = 10   # min blob size


def process_image(img_path, outdir):
    img = cv2.imread(str(img_path))
    if img is None:
        print("Error loading:", img_path)
        return 0

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # local variance calc
    f = gray.astype(np.float32)
    mean = cv2.blur(f, (WIN_SIZE, WIN_SIZE))
    mean2 = cv2.blur(f * f, (WIN_SIZE, WIN_SIZE))
    variance = mean2 - (mean * mean)

    # normalize for thresholding
    norm = cv2.normalize(variance, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # threshold
    _, mask = cv2.threshold(norm, THRESH, 255, cv2.THRESH_BINARY)

    # cleanup mask (worked best in my test)
    mask = cv2.medianBlur(mask, 5)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k)

    # cc
    n, lbl, stats, cent = cv2.connectedComponentsWithStats(mask)
    out = img.copy()
    cnt = 0

    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if area < MIN_AREA:
            continue
        cv2.rectangle(out, (x,y), (x+w, y+h), (0,0,255), 2)
        cnt += 1

    # save
    fname = Path(img_path).stem
    cv2.imwrite(os.path.join(outdir, fname + "_mask.png"), mask)
    cv2.imwrite(os.path.join(outdir, fname + "_detected.png"), out)

    return cnt



# batch processing
exts = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.tif"]
files = []

for e in exts:
    files.extend(Path(INPUT_FOLDER).glob(e))

if not files:
    print("No images found?? Check folder path.")
    exit()

print("Total images found:", len(files))

total = 0

for i, f in enumerate(files, start=1):
    c = process_image(f, OUTPUT_FOLDER)
    print(f"[{i}/{len(files)}] {f.name} -> {c} defects")
    total += c

print("\nAll done.")
print("Total defects across all images:", total)
print("Saved outputs to:", OUTPUT_FOLDER)
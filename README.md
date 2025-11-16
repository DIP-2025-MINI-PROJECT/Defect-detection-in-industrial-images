# Project Name
Defect detection in industrial images

### Project Description:

This project detects defects in fabric and textile images using a classical image-processing pipeline. Local variance highlights irregularities in the weave pattern, followed by morphological filtering to refine defect regions. Connected components are then used to isolate and mark defects such as holes, stains, broken yarns, and misweaves.

#### Summary - 

This project detects defects in fabric images using classical digital image processing techniques. By computing local variance, the system highlights abnormal texture regions such as holes, stains, broken yarns, and misweaves. Morphological filtering refines the segmentation, and connected component analysis identifies and marks the defects. The pipeline automatically processes an entire dataset and outputs defect masks and annotated images.

#### Course concepts used - 
1. Grayscale Conversion: Converts the input image to grayscale so that defect detection can focus purely on intensity and texture variations instead of color information.
2. Local Variance Calculation: Measures texture irregularity within a sliding window; high variance indicates abnormal fabric regions where defects are likely present.
3. Thresholding: Transforms the variance map into a binary mask by separating high-variance defect pixels from normal fabric regions.
4. Median Filtering & Morphological Operations: Removes noise and refines the defect mask using median blur along with closing and opening to clean and isolate defect blobs.
   
#### Additional concepts used -
1. Batch Image Processing: The system automatically loads all images from the dataset folder and processes them sequentially, enabling large-scale fabric defect inspection.
2. Connected Components Analysis: Identifies and labels defect regions, allowing the system to locate, draw bounding boxes, and count individual defects.
   
#### Dataset - 
https://github.com/SimonThomine/IndustrialTextileDataset

#### Novelty - 
1. Local-variance-based defect detection specifically optimized for repetitive textile textures.
2. Morphological filtering pipeline designed to suppress natural weave patterns and remove noise.
3. Automated batch processing workflow that detects, counts, and marks defects for all images in a folder.
   
### Contributors:
1. Hardik Gupta (PES1UG23EC115)
2. Sinchana M (PES1UG23EC299)
3. Monal Reddy P (PES1UG23EC180)


### Outputs:
* Refer the outputs folder

### References:
1. https://www.geeksforgeeks.org/python-opencv-median-blurring
2. https://github.com/avishkakavindu/defect-detection-opencv-python
3. https://www.geeksforgeeks.org/erosion-dilation-image-processing-python-opencv
   
### Limitations and Future Work:
Limitations

1. The method is sensitive to lighting variations and may produce noise on unevenly illuminated fabric images.
2. Highly patterned or textured fabrics can cause false positives due to naturally high variance regions.
3. Fixed thresholding may not adapt well to different fabric types or varying defect sizes.

Future Work

1. Implement adaptive or multi-scale thresholding to handle different fabric textures automatically.
2. Integrate advanced texture filters (Gabor, LBP) to improve defect separation in complex patterns.
3. Extend the system with deep-learning models for more robust detection and defect classification.
import fitz 
import hashlib
import os
from PIL import Image
import io

def get_image_hash(image_bytes):
    return hashlib.md5(image_bytes).hexdigest()

def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    image_data = []
    for page_num, page in enumerate(doc, start=1):
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_hash = get_image_hash(image_bytes)
            
            image_data.append({
                "image_bytes": image_bytes,
                "image_hash": image_hash,
                "page_num": page_num
            })
    
    return image_data

def find_and_save_duplicates(pdf_path, output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


































    if len(occurrences) > 1:  # Only process if there are duplicates
            for i, occurrence in enumerate(occurrences[1:], start=1):  # Skip the first occurrence
                duplicate_image = Image.open(io.BytesIO(occurrence['image_bytes']))
                duplicate_filename = os.path.join(output_folder, f"duplicate_image_{duplicate_count + 1}.png")
                duplicate_image.save(duplicate_filename)
                duplicate_count += 1
                print(f"Saved duplicate {duplicate_count}: Page {occurrence['page_num']}")

    print(f"Total duplicate images found: {duplicate_count}")

# Example usage
pdf_path = 'testing.pdf'
find_and_save_duplicates(pdf_path)

    image_data = extract_images_from_pdf(pdf_path)
    seen = {}
    duplicate_count = 0

    for idx, data in enumerate(image_data):
        image_hash = data['image_hash']
        if image_hash in seen:
            duplicate_image = Image.open(io.BytesIO(data['image_bytes']))
            duplicate_filename = os.path.join(output_folder, f"duplicate_image_{duplicate_count + 1}.png")
            duplicate_image.save(duplicate_filename)
            duplicate_count += 1
        else:
            seen[image_hash] = True

    print(f"Total duplicate images found: {duplicate_count}")

pdf_path = 'testing.pdf'
find_and_save_duplicates(pdf_path)

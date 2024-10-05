import os

def verify_files(main_directory):
    all_verified = True
    

    for subdir, _, files in os.walk(main_directory):
        image_files = set() 
        pdf_files = set()
        
        # Separate files into image and pdf sets
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.add(file[:-5])
            elif file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.JPEG', '.JPG')):
                image_files.add(file[:file.rfind('.')])

        missing_pdfs = image_files - pdf_files
        missing_images = pdf_files - image_files
        
        if missing_pdfs or missing_images:
            all_verified = False
            print(f"In directory '{subdir}':")
            if missing_pdfs:
                print(f"  Missing pdf files for images: {missing_pdfs}")
            if missing_images:
                print(f"  Missing image files for pdfs: {missing_images}")
    
    if all_verified:
        print("All image files have corresponding pdf files in all directories.\nYou can now progress with the rest of the training process")

main_directory = r"Path/to/check"
verify_files(main_directory)

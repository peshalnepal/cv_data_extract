
import pathlib
from pdf2image import convert_from_path

import os
import json
import shutil
# Get the list of all files and directories
path = "/home/peshal/projects/cv_data_extract/cv_pdf"
dir_list = os.listdir(path)


data = {
    "gt_parse": {
        "Skills": {"Programming Languages,Libraries and frameworks":[""],"Database":[""],"others":[""]},
        "User_Name": "",
        "Company": [{"name":"","experience years":"","Roles":""}],
        "Education": [{"years":"","institute":"","programme":""}],
        "awards": [""],
        "mail": "",
        "number": "",
        "Address": "",
        "projects":[""],
        "Linkedln_Links": [""],
        "Certificates": [""],
        "leadership": [""],
        "voluntare": [""],
        "Reference": [{"name":"","Company name":"","number":""}],
        "github_links": [""],
        "portfolio_links": [""],
        "other_links": [""]
    }
}

# print("Files and directories in '", path, "' :")
 
# # prints all files
# print(dir_list)
# creating a pdf reader 
data_collectors=["Narayan","Peshal","Bishal_Gupta","Bishal_Adhikari"]
number_users=len(data_collectors)
number_cv=len(dir_list)
cv_for_each=number_cv//number_users
for i in range(number_cv) :
    file_path="/".join([path,dir_list[i]])
    # print(file_path)
    p = pathlib.Path(file_path)

    if pathlib.Path(file_path).suffix == ".pdf":
        file_name="".join(list(os.path.splitext(dir_list[i])[0:-1]))
        
        # Convert PDF/DOC to images
        images = convert_from_path(file_path)
        id_user=i//cv_for_each
        # Create a directory to save the images and text file
        output_dir_pdf = f"/home/peshal/projects/cv_data_extract/data/{data_collectors[id_user]}/pdf"
        os.makedirs(output_dir_pdf, exist_ok=True)
        shutil.copy(file_path, output_dir_pdf)

        output_dir_label = f"/home/peshal/projects/cv_data_extract/data/{data_collectors[id_user]}/labels"
        os.makedirs(output_dir_label, exist_ok=True)

        output_dir_image = f"/home/peshal/projects/cv_data_extract/data/{data_collectors[id_user]}/images"
        os.makedirs(output_dir_image, exist_ok=True)

        output_dir_label = f"/home/peshal/projects/cv_data_extract/data/{data_collectors[id_user]}/labels"
        os.makedirs(output_dir_label, exist_ok=True)
        
    # Iterate over the images and save as JPEG files
        for i, image in enumerate(images):
            image_name = f"{file_name}_{i+1}"
            image_path = os.path.join(output_dir_image, f"{image_name}.jpg")
            image.save(image_path, "JPEG")

            image_path = os.path.join(output_dir_image, f"page_{i+1}.jpg")
            image.save(image_path, "JPEG")

            # Save the extracted text as a txt file with the same name as the image
            json_file_path = os.path.join(output_dir_label, f"{image_name}.json")
            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file,indent=4)
            print(f"Saved image and text file for page {i+1}")

        # reader = PdfReader(file_path)
        
        # # # printing number of pages in pdf file
        # # # print(len(reader.pages))
        
        # # # getting a specific page from the pdf file
        
        # final_text=""
        # # # extracting text from page 
        # for page in reader.pages:
        #     text = page.extract_text()
        #     final_text=" ".join([final_text,text])
        # final_text=final_text.replace("\n"," ").strip(" ")
        # text_path=file_path.split(".")[:-1]
        # text_path="".join(text_path)
        # text_path=".".join([text_path,"txt"])

        # f = open(text_path, "a")
        # f.write(final_text)
        # f.close()
        
# {"gt_parse": {"Skills": [], "User_Name": [], "Company_names": [], "Education": [], "awards": [], "mail": [], "number": [], "Address": [], "Linkedln_Links": [], "Experience_year": [], "Education_years": [], "Roles": [], "Certificates": [], "Programming Languages, Libraries and frameworks": [], "leadership": [], "Education college_school": [], "voluntare": [], "Database": [], "Reference": [], "github_links": [], "portfolio_links": [], "other_links": []}}
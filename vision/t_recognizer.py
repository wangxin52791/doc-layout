import os, sys
# sys.path.insert(
#     0,
#     os.path.abspath(
#         os.path.join(
#             os.path.dirname(
#                 os.path.abspath(__file__)),
#             '../../')))
# import sys
# sys.path.append("..")
from .seeit import draw_box
from vision import Recognizer, LayoutRecognizer, TableStructureRecognizer, OCR, init_in_out
import base64
from io import BytesIO
from .utils.file_utils import get_project_base_directory
import argparse
import re
import numpy as np
import os

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('ascii')



os.environ['CURL_CA_BUNDLE'] = ''




# def main(args):
#     images, outputs = init_in_out(args)
#     output_images_base64=[]
#     if args.mode.lower() == "layout":
#         labels = LayoutRecognizer.labels
#         detr = Recognizer(
#             labels,
#             "layout",
#             os.path.join(
#                 get_project_base_directory(),
#                 "rag/res/deepdoc/"))
#     if args.mode.lower() == "tsr":
#         labels = TableStructureRecognizer.labels
#         detr = TableStructureRecognizer()
#         ocr = OCR()

#     layouts = detr(images, float(args.threshold))
#     for i, lyt in enumerate(layouts):
#         # if args.mode.lower() == "tsr":
#         #     #lyt = [t for t in lyt if t["type"] == "table column"]
#         #     html = get_table_html(images[i], lyt, ocr)
#         #     with open(outputs[i] + ".html", "w+") as f:
#         #         f.write(html)
#         #     lyt = [{
#         #         "type": t["label"],
#         #         "bbox": [t["x0"], t["top"], t["x1"], t["bottom"]],
#         #         "score": t["score"]
#         #     } for t in lyt]
#         img = draw_box(images[i], lyt, labels, float(args.threshold))
#         output_images_base64.append(image_to_base64(img))
#         #img.save(outputs[i], quality=95)
#         print("save result to: " + outputs[i])







# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI()

# class Item(BaseModel):
#     inputs: str
#     output_dir: Optional[str] = "./layouts_outputs"
#     threshold: Optional[float] = 0.5
#     mode: Optional[str] = "layout"


# @app.post("/process")
# async def process(item: Item):
#     # Replace "main" with your function that would process the item
#     result = main(item.inputs, item.output_dir, item.threshold, item.mode)
#     return {"message": "Processing Successful", "result": result}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)




def main(input,output_dir,threshold):
    images, outputs = init_in_out(input,output_dir)
    output_images_results=[]
    index=0
    labels = LayoutRecognizer.labels
    detr = Recognizer(
        labels,
        "layout",
        os.path.join(
            get_project_base_directory(),
            "rag/res/deepdoc/"))


    layouts = detr(images, float(threshold))
    for i, lyt in enumerate(layouts):
        # if args.mode.lower() == "tsr":
        #     #lyt = [t for t in lyt if t["type"] == "table column"]
        #     html = get_table_html(images[i], lyt, ocr)
        #     with open(outputs[i] + ".html", "w+") as f:
        #         f.write(html)
        #     lyt = [{
        #         "type": t["label"],
        #         "bbox": [t["x0"], t["top"], t["x1"], t["bottom"]],
        #         "score": t["score"]
        #     } for t in lyt]

        img,crop_image = draw_box(images[i], lyt, labels, float(threshold))
        
        if crop_image != []:
            for j in range(len(crop_image)):
                # crop_image[j]["image"].save(f"table{j+1}_{outputs[i]}", quality=95)
                #保存文件
                # crop_image[j]["image"].save(f"./results/page_{i}_table_{j}.jpg", quality=95)
                crop_image[j]["image"]=image_to_base64(crop_image[j]["image"])
                crop_image[j]["page"]=i +1
                crop_image[j]["index"]=index
                index +=1
                output_images_results=output_images_results +crop_image 
                print("save result to: " + outputs[i])
    return output_images_results





# if __name__ == "__main__":
#     outputdir= 

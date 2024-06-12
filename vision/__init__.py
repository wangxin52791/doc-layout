import pdfplumber

from .ocr import OCR
from .recognizer import Recognizer
from .layout_recognizer import LayoutRecognizer
from .table_structure_recognizer import TableStructureRecognizer
from PIL import Image
import os
import traceback

# def init_in_out(args):
#     from PIL import Image
#     import os
#     import traceback
#     from utils.file_utils import traversal_files
#     images = []
#     outputs = []

#     if not os.path.exists(args.output_dir):
#         os.mkdir(args.output_dir)

#     def pdf_pages(fnm, zoomin=3):
#         nonlocal outputs, images
#         pdf = pdfplumber.open(fnm)
#         images = [p.to_image(resolution=72 * zoomin).annotated for i, p in
#                             enumerate(pdf.pages)]

#         for i, page in enumerate(images):
#             outputs.append(os.path.split(fnm)[-1] + f"_{i}.jpg")

#     def images_and_outputs(fnm):
#         nonlocal outputs, images
#         if fnm.split(".")[-1].lower() == "pdf":
#             pdf_pages(fnm)
#             return
#         try:
#             images.append(Image.open(fnm))
#             outputs.append(os.path.split(fnm)[-1])
#         except Exception as e:
#             traceback.print_exc()

#     if os.path.isdir(args.inputs):
#         for fnm in traversal_files(args.inputs):
#             images_and_outputs(fnm)
#     else:
#         images_and_outputs(args.inputs)

#     for i in range(len(outputs)): outputs[i] = os.path.join(args.output_dir, outputs[i])

#     return images, outputs




# def init_in_out(input,output_dir):
#     from PIL import Image
#     import os
#     import traceback
#     from .utils.file_utils import traversal_files
#     images = []
#     outputs = []

#     if not os.path.exists(output_dir):
#         os.mkdir(output_dir)

#     def pdf_pages(fnm, zoomin=3):
#         nonlocal outputs, images
#         pdf = pdfplumber.open(fnm)
#         images = [p.to_image(resolution=72 * zoomin).annotated for i, p in
#                             enumerate(pdf.pages)]

#         for i, page in enumerate(images):
#             outputs.append(os.path.split(fnm)[-1] + f"_{i}.jpg")

#     def images_and_outputs(fnm):
#         nonlocal outputs, images
#         if fnm.split(".")[-1].lower() == "pdf":
#             pdf_pages(fnm)
#             return
#         try:
#             images.append(Image.open(fnm))
#             outputs.append(os.path.split(fnm)[-1])
#         except Exception as e:
#             traceback.print_exc()

#     if os.path.isdir(input):
#         for fnm in traversal_files(input):
#             images_and_outputs(fnm)
#     else:
#         images_and_outputs(input)

#     for i in range(len(outputs)): outputs[i] = os.path.join(output_dir, outputs[i])

#     return images, outputs


def init_in_out(file_object, output_dir):
    images = []
    outputs = []
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if isinstance(file_object, pdfplumber.PDF):
        images = [p.to_image(resolution=72*3).annotated for p in file_object.pages]
        for i, _ in enumerate(images):
            outputs.append(f"page_{i}.jpg")

    elif isinstance(file_object, Image.Image):
        images.append(file_object)
        outputs.append("output_image.jpg")  # You might want to change this based on your requirement

    else:
        return "Invalid file_object. It must be a pdfplumber.PDF or PIL.Image object."

    for i in range(len(outputs)):
        outputs[i] = os.path.join(output_dir, outputs[i])

    return images, outputs
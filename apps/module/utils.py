import io
import os
import random
import string
# from pathlib import Path
#
# import qrcode
# from pdf2image import convert_from_path
# from qrcode.image.svg import SvgImage
# from weasyprint import HTML
#
# from django.conf import settings
# from django.core.files import File
# from django.template.loader import get_template

COURSE_HTML_CERTIFICATE_HELP_TEXT = """
<br />
<div style="padding: 8px 12px; border-radius: 8px; background-color: #54b4d3; display: flex; gap: 8px">
    <i>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke="white" stroke-width="1.5"/>
            <path d="M12 17V11" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
            <path d="M12 7C12.5523 7 13 7.44772 13 8C13 8.55228 12.5523 9 12 9C11.4477 9 11 8.55228 11 8C11 7.44772 11.4477 7 12 7Z" fill="white"/>
        </svg>
    </i>
    <p style="color: black; color: white; font-style: normal; margin: 0">
        {}
    </p>
</div>
"""  # noqa: E501


def randomize_certificate_number():
    from .models import Certificate

    cids = Certificate.objects.values_list("cid", flat=True)
    while True:
        random_cid = "".join(random.choice(string.digits + string.ascii_uppercase) for _ in range(7))
        if random_cid not in cids:
            return random_cid


# def generate_certificate(user_course, full_name):
#     from apps.module.models import Certificate
#
#     certificate_obj = Certificate.objects.create(course.py=user_course.course.py, user=user_course.user, full_name=full_name)
#     if not certificate_obj.full_name:
#         full_name = user_course.user.full_name
#
#     template = get_template(user_course.course.py.certificate_html_template.path)
#     context = {
#         "full_name": full_name,
#         "course_title": user_course.course.py.title,
#         "author": user_course.course.py.author,
#         "author_signature": user_course.course.py.author_signature.path,
#         "absolute_path": os.getcwd(),
#         "qrcode_url": get_qrcode_url(certificate_obj.cid),
#     }
#
#     html = template.render(context)
#     output = io.BytesIO()
#
#     HTML(string=html, base_url=os.getcwd()).write_pdf(
#         output, stylesheets=[f"{os.getcwd()}/staticfiles/certificate/style.css"]
#     )
#     certificate = File(output)
#     certificate_obj.file.save(
#         name=f"{user_course.course.py.title}_{full_name}_{certificate_obj.cid}.pdf", content=certificate
#     )
#
#     # save as image
#     images = convert_from_path(certificate_obj.file.path)
#     output_image = io.BytesIO()
#     images[0].save(output_image, format="JPEG")
#     certificate_obj.image.save(
#         name=f"{user_course.course.py.title}_{full_name}_{certificate_obj.cid}.JPEG", content=File(output_image)
#     )
#     return certificate_obj
#
#
# def get_qrcode_url(cid):
#     data = f"{settings.CERTIFICATE_QR_CODE_BASE_URL}?cid={cid}"
#     img = qrcode.make(data, image_factory=SvgImage, border=4)
#     img_name = f"certificate_{cid}.svg"
#
#     Path(f"{settings.MEDIA_ROOT}/certificate_qr_codes/").mkdir(parents=True, exist_ok=True)
#
#     qrcode_url = f"{settings.MEDIA_ROOT}/certificate_qr_codes/{img_name}"
#     img.save(qrcode_url)
#
#     return qrcode_url

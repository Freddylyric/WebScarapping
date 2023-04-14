# # import requests

# # url = "https://authoraditiagarwal.com/wpcontent/uploads/2018/05/MetaSlider_ThinkBig-1080x180.jpg"

# # r = requests.get(url, allow_redirects=True)

# # for headers in r.headers:
# #     print(headers)

# # print(r.status_code)
# # print(r.headers.get('content-type'))
# # print(r.headers.get('ETag'))
# # print(r.headers.get('Server'))


# # import requests

# # url = "https://authoraditiagarwal.com/wpcontent/uploads/2018/05/MetaSlider_ThinkBig-1080x180.jpg"

# # r = requests.get(url)

# # with open("ThinkBig.jpeg", "wb") as f:
# #     f.write(r.content)


# import glob

# from PIL import Image
# for infile in glob.glob("ThinkBig.jpeg"):
#     img = Image.open(infile)
#     img.thumbnail((128, 128), Image.ANTIALIAS)

#     if infile[0:2] != "Th_":
#         img.save("Th_" + infile, "png")

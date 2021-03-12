#提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=225,height=225):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
        
for jpgfile in glob.glob("C:\\Users\86177\Pictures\picture\\*.jpg"): #图片目录
    convertjpg(jpgfile,"E:\\picture")        #保持目录
    print("finish")

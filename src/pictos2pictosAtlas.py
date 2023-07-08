import os, json, time, shutil
from PIL import Image

os.makedirs("pictos", exist_ok=True)
os.makedirs("pictosAtlas", exist_ok=True)

print("pictos2pictosAtlas for Just Dance Now Modding by JustDanceModding (Tool By Sen)")
CoachCount = int(input("CoachCount -> "))

width = 0
height = 0
if CoachCount > 1:
    pictoWidth = 370
    pictoHeight = 256
if CoachCount == 1:
    pictoWidth = 256
    pictoHeight = 256
pictoAtlas = {
    "imageSize": {
        "width": pictoWidth,
        "height": pictoHeight
    },
    "images": {

    }
}

os.makedirs("temp/pictos", exist_ok=True)

pictoAtlas_png = Image.new("RGBA", (256, 256))
pictoAtlas_png.save("temp/atlas.png")
pictoAtlas_png = Image.open("temp/atlas.png")

pictoAtlas_height = 256
pictoAtlas_width = 0

for picto in os.listdir("pictos"):
    print(f"Adding {picto}")
    pictoAtlas_width += pictoWidth
    oldPictogram = Image.open(f"pictos/{picto}")
    newPictogram = oldPictogram.resize((pictoWidth, pictoHeight))
    newPictogram.save(f"temp/pictos/{picto}")
    pictoJson = [
        width, 
        height
    ]

    width += pictoWidth
    if width % (pictoWidth * 10) == 0:
        width = 0
        height += pictoHeight

    pictoName = picto.split(".")[0]
    pictoAtlas["images"][pictoName] = pictoJson

newAltas = pictoAtlas_png.resize((pictoAtlas_width, pictoAtlas_height))

width = 0
height = 0

for i, picto in enumerate(os.listdir("temp/pictos")):
    newPictogram = Image.open(f"temp/pictos/{picto}")
    newPictoCopy = newPictogram.copy()
    
    if i > 0:
        width += pictoWidth
        if width % (pictoWidth * 10) == 0:
            width = 0
            height += pictoHeight
    else:
        pass

    newAltas.paste(newPictoCopy, (width, height))

newAltas.save("pictosAtlas/pictos-atlas.png")
with open("pictosAtlas/pictos-atlas.json", "w") as atlas:
    json.dump(pictoAtlas, atlas)

shutil.rmtree("temp")

print("Done!")
time.sleep(3)



